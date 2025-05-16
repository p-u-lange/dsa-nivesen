import pandas as pd
import numpy as np
import math
import random
from krankheitsverlauf import krankheitsverlauf, halber_schaden
def random_age():
    age_range = np.arange(0, 61)
    probabilities = np.array([
        0.03, 0.04, 0.04, 0.04, 0.04,  # Ages 0-4
        0.04, 0.04, 0.04, 0.04, 0.04,  # Ages 5-9
        0.04, 0.04, 0.04, 0.04, 0.04,  # Ages 10-14
        0.04, 0.04, 0.04, 0.04, 0.04,  # Ages 15-19
        0.04, 0.04, 0.04, 0.04, 0.04,  # Ages 20-24
        0.04, 0.04, 0.04, 0.04, 0.04,  # Ages 25-29
        0.04, 0.04, 0.04, 0.04, 0.04,  # Ages 30-34
        0.035, 0.03, 0.03, 0.025, 0.02,  # Ages 35-39
        0.02, 0.015, 0.015, 0.01, 0.009,  # Ages 40-44
        0.008, 0.008, 0.007, 0.006, 0.005,  # Ages 45-49
        0.004, 0.004, 0.003, 0.003, 0.002,  # Ages 50-54
        0.001, 0.001, 0.001, 0.001, 0.001,  # Ages 55-59
        0.001  # Age 60
    ])
    probabilities = probabilities / probabilities.sum()
    return np.random.choice(age_range, p=probabilities)

def random_gender():
    gender_range = np.arange(0, 2)
    probabilities = np.array([0.50, 0.50])
    probabilities = probabilities / probabilities.sum()
    number = np.random.choice(gender_range, p=probabilities)
    if number == 0:
        return 'w'
    if number == 1:
        return 'm'

def random_start_lp():
    range = np.arange(0, 6)
    probabilities  = np.array([0.1, 0.2, 0.2, 0.2, 0.1, 0.1])
    probabilities = probabilities / probabilities.sum()
    lp = 28 + np.random.choice(range, p=probabilities)
    return lp

def random_start_day():
    range = np.arange(0, 9)
    probabilities = np.array([1, 3, 4, 6, 6, 5, 2, 1, 0.5])
    probabilities = probabilities / probabilities.sum()
    day = 1 + np.random.choice(range, p=probabilities)
    return day

def get_name(gender):
    namen_w = [
    "Airaksela", "Amuri", "Auka", "Aukaju", "Baituri", "Bjanju", "Biniaki", "Burti", "Dakauju", "Dana", "Dionju",
    "Duri", "Eikaju", "Emela", "Eskola", "Falkja", "Ferturi", "Fidju", "Fidaju", "Gateiki", "Geika",
    "Godju", "Hauka", "Hirolja", "Hikia", "Hyvinga", "Ikaju", "Ila", "Irti", "Isalmi", "Jalani",
    "Jokela", "Jokja", "Jonuri", "Jutila", "Jyla", "Kajani", "Kantala", "Karenju", "Karra", "Katimäki",
    "Kaukalathi", "Keitakju", "Kela", "Kelva", "Kisa", "Koski", "Kuopi", "Kura", "Lahti", "Lappila",
    "Lauka", "Lieksa", "Liskaju", "Loja", "Lojmaa", "Murula", "Myrra", "Nakila", "Näljavena", "Nivilaukaju",
    "Nujala", "Ojakalla", "Olu", "Paukaja", "Peltju", "Pori", "Purolju", "Rael(a)", "Rauma", "Roika",
    "Rukosari", "Saari", "Sarela", "Saviharju", "Savolina", "Sievi", "Sjunda", "Sotkia", "Takoja", "Tiensu",
    "Tolsa", "Torhola", "Tuira", "Turi", "Ulu", "Ulvila", "Ura", "Usi", "Vaala", "Varpa",
    "Vatja", "Vedaju", "Vella", "Viala", "Vieki", "Vika", "Ylista", "Zurti"
    ]
    namen_m = [
    "Abjo", "Adjok", "Airujo", "Altanan", "Arjuk", "Arko", "Banuk", "Beranen", "Berko", "Binjok",
    "Danjuk", "Dernkjo", "Dragjo", "Ebnan", "Eikaljok", "Eiko",
    "Einuk", "Enan", "Enko", "Eno", "Enuk", "Erljuk", "Gaitjok",
    "Garnan", "Garnuk", "Genko", "Gjuternuk", "Gorfangnuk", "Gurjinen", "Hanko", "Hautan", "Hautanan", "Heimanuk",
    "Hietanen", "Honuk", "Horganan", "Hunjok", "Huno",
    "Janjuk", "Jorinen", "Jurtan", "Jurtanan", "Kaikanuk", "Kalkuk",
    "Kaunanan", "Kauno", "Keinjo", "Kervo", "Kilho", "Kilhjo", "Kinajo", "Kintan", "Kintanan", "Kuljuk", "Kumo", "Kylänjak", "Lanan",
    "Latu", "Leikinen", "Leksvalen", "Lieto", "Mada", "Madanan",
    "Maenan", "Matiljok", "Minkio", "Mouhuk", "Nantalin",
    "Nerkjo", "Niljo", "Nurmjo", "Nysjo", "Olainen", "Paimjo",
    "Parkanjuk", "Peltjo", "Pirtijok", "Rakjo", "Rasjuk", "Raumo",
    "Ruukjok", "Sandjo", "Seinuk", "Seinjuk", "Silkajok", "Simjok",
    "Svartjok", "Tamperen", "Toljok", "Tsaekal", "Turkunen",
    "Tyrjuk", "Uljok", "Ulo", "Valen", "Valjok", "Vik", "Ylsjok", "Zanuk", "Zeino"
    ]
    if gender == 'w':
        return random.choice(namen_w)
    else:
        return random.choice(namen_m)

def random_ko(age):
    ko_range = np.arange(0, 4)
    probabilities = np.array([5, 4, 4, 1])
    probabilities = probabilities / probabilities.sum()
    number = np.random.choice(ko_range, p=probabilities)
    if age < 6:
        return number + 7
    elif age < 11:
        return number + 8
    elif age < 16:
        return number + 9
    elif age < 35:
        return number + 10
    elif age < 42:
        return number + 9
    elif age < 48:
        return number + 8
    else:
        return number + 7

# def akt_start_lp(nivese):
#     lp = start_lp
#     i = 1
#     while i <= krank_tage:
#         if i != 1 and i != 2:
#             lp = krankheitsverlauf(nivese)
#         i += 1
#     return lp
def create_nivesenstamm():
    columns = ['nivese_ID', 'zelt', 'name', 'alter', 'geschlecht', 'start_lep', 'tag_der_erkrankung', 'aktuelle_lep', 'krankheitstage', 'ko', 'balsam', 'pflege', 'heilmittel', 'zustand', 'kranke_im_zelt']
    df = pd.DataFrame(columns=columns)
    kuljuk = [1, 1, 'Kuljuk', 39, 'm', 34, 13, 0, 13, 15, 0, 0, '', 'V', 0]
    new_row = pd.DataFrame([kuljuk], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    nirka = [2, 1, 'Nirka', 21, 'w', 36, 14, 36, 14, 15, 0, 0, '', 'I', 0]
    new_row = pd.DataFrame([nirka], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    roika = [3, 1, 'Roika', 39, 'w', 34, 13, 0, 13, 15, 0, 0, '', 'V', 0]
    new_row = pd.DataFrame([roika], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    for i in range(5,143):
        age = random_age()
        zelt = math.ceil((i+1)/5)
        start_lp = random_start_lp()
        ko = random_ko(age)
        gender = random_gender()
        name = get_name(gender)
        new_nivese = [i, zelt, name, random_age(), gender, start_lp, 0, start_lp, 0, ko, 0, 0, '', 'G', 0]
        new_row = pd.DataFrame([new_nivese], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
    df['heilmittel'] = df['heilmittel'].fillna('N').astype(str)
    df.to_csv('alle_nivesen.csv', index=False, sep=';')
    return df

def krankheitsausbruch(df):
    gesunde_nivesen = (df['zustand'] == 'G').sum()
    while gesunde_nivesen > 1:
        for index, row in df.iterrows():
            if row['zustand'] == 'G':
                if row['kranke_im_zelt'] == 0:
                    range = np.arange(0, 2)
                    probabilities = np.array([95 - 1.8 * row['tag_der_erkrankung'], 5 + 1.8 * row['tag_der_erkrankung']])
                    probabilities = probabilities / probabilities.sum()
                    if np.random.choice(range, p=probabilities) == 1:
                        if halber_schaden(row['ko']) == 1:
                            df.at[index, 'zustand'] = 'K'
                else:
                    range = np.arange(0, 2)
                    probabilities = np.array([55 - 2 * row['tag_der_erkrankung'], 45 + 2 * row['tag_der_erkrankung']])
                    probabilities = probabilities / probabilities.sum()
                    if np.random.choice(range, p=probabilities) == 1:
                        if halber_schaden(row['ko']) == 1:
                            df.at[index, 'zustand'] = 'K'
                df.at[index, 'tag_der_erkrankung'] = row['tag_der_erkrankung'] + 1
        for index, row in df.iterrows():
            if row['zustand'] == 'K' and row['kranke_im_zelt'] == 0:
                df.loc[df['zelt'] == row['zelt'], 'kranke_im_zelt'] = 1
        gesunde_nivesen = (df['zustand'] == 'G').sum()
    df.to_csv('alle_nivesen.csv', index=False, sep=';')
    return df

def simulate_start_lep(df):
    for index, row in df.iterrows():
        i = 0
        if row['zustand'] == 'K':
            while i < 10 - row['tag_der_erkrankung']:
                new_row = krankheitsverlauf(row)
                df.loc[index] = new_row
                i = i + 1
                if new_row['aktuelle_lep'] < 2:
                    df.at[index, 'aktuelle_lep'] = 2
                    df.at[index, 'zustand'] = 'K'
                    df.at[index, 'krankheitstage'] = 10 - row['tag_der_erkrankung']
    df.to_csv('alle_nivesen.csv', index=False, sep=';')
    return df