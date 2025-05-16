import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def plot_ansteckung(df):
    sns.countplot(
        data=df,
        y='tag_der_erkrankung')
    plt.title("Anzahl der Tage, die an einem Tag erkrankt sind")
    plt.xlabel("Anzahl Nivesen")
    plt.ylabel("Tag")
    plt.show()
def plot_symptome(df):
    df['angepasst'] = (df['krankheitstage'] - 2).clip(lower=0)
    order = sorted(df['angepasst'].unique())
    farben_map = {
        11: 'black',  # 13 - 2
        12: 'green',  # 14 - 2
    }
    default_color = 'steelblue'
    df['farbgruppe'] = df['angepasst'].map(lambda x: x if x in farben_map else 'other')

    palette = {
        11: 'black',
        12: 'green',
        'other': default_color,
    }
    ax = sns.countplot(
        data=df,
        y='angepasst',
        hue='farbgruppe',
        order=order,
        palette=palette,
        dodge=False,
        legend=False
    )
    achse_labels = []
    for val in order:
        if val == 11:
            achse_labels.append('verstorben')
        elif val == 12:
            achse_labels.append('geheilt')
        else:
            achse_labels.append(str(val))
    plt.title("Anzahl der Tage, die die Nivesen schon Symptome zeigen")
    plt.xlabel("Anzahl Nivesen")
    plt.ylabel("Tage")
    ax.set_yticks(range(len(order)))
    ax.set_yticklabels(achse_labels)
#    plt.savefig("krankheitstage.png", dpi=300, bbox_inches='tight')
    plt.show()
def gruppenlabel(gruppe):
    untere_grenze = (gruppe - 1) * 5
    obere_grenze = gruppe * 5 - 1
    return f'{untere_grenze}–{obere_grenze}'
def plot_altersverteilung(df):
    max_alter = df['alter'].max()
    max_gruppe = (max_alter // 5 + 1)
    alle_gruppen = pd.Index(range(1, max_gruppe + 1))
    df['altersgruppe'] = (df['alter'] // 5 + 1).clip(lower=1)
    gruppen = df.groupby(['altersgruppe', 'geschlecht']).size().unstack(fill_value=0)
    gruppen = gruppen.reindex(alle_gruppen, fill_value=0)
    # Mach Männer negativ für die linke Seite
    gruppen['m'] = -gruppen.get('m', 0)
    gruppen['w'] = gruppen.get('w', 0)
    # Neu sortieren nach Gruppen
    gruppen = gruppen.sort_index()
    gruppen.index = gruppen.index.map(gruppenlabel)
    plt.figure(figsize=(10, 6))

    # Plot: horizontaler Balken für Männer (links) und Frauen (rechts)
    plt.barh(gruppen.index, gruppen['m'], color='skyblue', label='Männer')
    plt.barh(gruppen.index, gruppen['w'], color='lightpink', label='Frauen')
    xticks = plt.xticks()[0]
    xtick_labels = [str(abs(int(x))) for x in xticks]
    plt.xticks(xticks, xtick_labels)
    plt.axvline(0, color='black')  # Mittellinie

    plt.xlabel('Anzahl')
    plt.ylabel('Altersgruppe')
    plt.title('Alterspyramide')
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_zelte(df):
