import numpy as np

def w_6():
    range = np.arange(0, 6)
    probabilities = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    probabilities = probabilities / probabilities.sum()
    return 1 + np.random.choice(range, p=probabilities)
def w_20():
    range = np.arange(0, 20)
    probabilities = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1])
    probabilities = probabilities / probabilities.sum()
    return 1 + np.random.choice(range, p=probabilities)
def halber_schaden(ko):
    range = np.arange(0, 2)
    probabilities = np.array([max(1, min(ko - 10, 19)), 20-max(1, min(ko - 10, 19))])
    probabilities = probabilities / probabilities.sum()
    return (np.random.choice(range, p=probabilities) + 1)/2
def krankheitsverlauf(nivese):
    schaden = 0
    if nivese['zustand'] == 'K':
        nivese['krankheitstage'] = nivese['krankheitstage'] + 1
        if 2 < nivese['krankheitstage'] < 13:
            schaden = int((w_6() + 2) * halber_schaden(nivese['ko']))
            if nivese['heilmittel'] == 'G':
                schaden = schaden - 1
            elif nivese['heilmittel'] == 'T':
                schaden = schaden - 2
            elif nivese['heilmittel'] == 'S':
                schaden = schaden - 1
            elif nivese['heilmittel'] == 'D':
                schaden = schaden - 2
            elif nivese['heilmittel'] == 'X':
                schaden = 0
        elif nivese['krankheitstage'] == 13:
            schaden = int((w_20() + 10) * halber_schaden(nivese['ko']))
            if nivese['heilmittel'] == 'G':
                schaden = schaden - 2
            elif nivese['heilmittel'] == 'T':
                schaden = schaden - 4
            elif nivese['heilmittel'] == 'S':
                schaden = schaden - 2
            elif nivese['heilmittel'] == 'D':
                schaden = int(schaden * 0.5)
            elif nivese['heilmittel'] == 'X':
                schaden = 0
        if nivese['pflege']:
            schaden = schaden - 2
        if schaden < 0:
            schaden = 0
        new_lp = min(nivese['start_lep'], nivese['aktuelle_lep'] - schaden + nivese['balsam'])
        if new_lp <= 0:
            nivese['aktuelle_lep'] = 0
            nivese['zustand'] = 'X'
            nivese['krankheitstage'] = 13
        else:
            nivese['aktuelle_lep'] = new_lp
        if (nivese['krankheitstage'] == 13 and nivese['aktuelle_lep'] > 0) or nivese['heilmittel'] == 'X':
            nivese['zustand'] = 'I'
            nivese['krankheitstage'] = 14
        nivese['pflege'] = 0
        nivese['balsam'] = 0
        nivese['heilmittel'] = 'N'
    elif nivese['zustand'] == 'I' or nivese['zustand'] == 'G':
        nivese['aktuelle_lep'] = min(nivese['start_lep'], (nivese['aktuelle_lep'] + nivese['balsam'] + w_6() + 1))
        nivese['pflege'] = 0
        nivese['balsam'] = 0
        nivese['heilmittel'] = 'N'
    return nivese
