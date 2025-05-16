import pandas as pd
def start_helden():
    columns = ['name', 'hat gepflegt', 'tap_hkk', 'prio_alter', 'prio_zustand', 'alter_oder_zustand']
    helden_df = pd.DataFrame(columns=columns)
    #####   ASTRID
    astrid = {
        'name': 'astrid',
        'hat_gepflegt': 0,
        'tap_hkk': 0,
        'prio_alter': 0,
        'prio_zustand': 0,
        'alter_oder_zustand': 0
    }
    astrid_df = pd.DataFrame([astrid])
    helden_df = pd.concat([helden_df, astrid_df], ignore_index=True)
    #####   ESRA
    esra = {
        'name': 'esra',
        'hat_gepflegt': 0,
        'tap_hkk': 0,
        'prio_alter': 0,
        'prio_zustand': 0,
        'alter_oder_zustand': 0
    }
    esra_df = pd.DataFrame([esra])
    helden_df = pd.concat([helden_df, esra_df], ignore_index=True)
    #####   EGIL
    egil = {
        'name': 'egil',
        'hat_gepflegt': 0,
        'tap_hkk': 0,
        'prio_alter': 0,
        'prio_zustand': 0,
        'alter_oder_zustand': 0
    }
    egil_df = pd.DataFrame([egil])
    helden_df = pd.concat([helden_df, egil_df], ignore_index=True)
    #####   ISHANNAH
    ishannah = {
        'name': 'ishannah',
        'hat_gepflegt': 0,
        'tap_hkk': 0,
        'prio_alter': 0,
        'prio_zustand': 0,
        'alter_oder_zustand': 0
    }
    ishannah_df = pd.DataFrame([ishannah])
    helden_df = pd.concat([helden_df, ishannah_df], ignore_index=True)
    #####   KILI
    kili = {
        'name': 'kili',
        'hat_gepflegt': 0,
        'tap_hkk': 0,
        'prio_alter': 0,
        'prio_zustand': 0,
        'alter_oder_zustand': 0
    }
    kili_df = pd.DataFrame([kili])
    helden_df = pd.concat([helden_df, kili_df], ignore_index=True)
    #####   JOHANNES
    johannes = {
        'name': 'johannes',
        'hat_gepflegt': 0,
        'tap_hkk': 0,
        'prio_alter': 0,
        'prio_zustand': 0,
        'alter_oder_zustand': 0
    }
    johannes_df = pd.DataFrame([johannes])
    helden_df = pd.concat([helden_df, johannes_df], ignore_index=True)
    helden_df.to_csv('helden.csv', index=False, sep=';')
def update_helden(name, pflege, hkk)
    df = pd.read_csv('helden.csv', sep=';')
    df.loc[df['name'] == name, ['age', 'score']] = [pflege, hkk]
    df.to_csv('helden.csv', index=False, sep=';')
