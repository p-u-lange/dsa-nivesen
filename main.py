import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from plots import plot_symptome, plot_krankheitszustand
from helden import update_helden, start_helden
df_nivese = pd.read_csv('alle_nivesen.csv', sep=';')
df_helden = pd.read_csv('helden.csv', sep=';')

start_helden()
update_helden('astrid', 0, 0)
update_helden('esra', 0, 0)
update_helden('egil', 0, 0)
update_helden('ishannah', 0, 0)
update_helden('kili', 0, 0)
update_helden('johannes', 0, 0)
gekochte_rationen = 0
pflege_eintragen(df_nivese, df_helden, gekochte_rationen)
balsam(1, 0)

plot_symptome(df_nivese)
plot_krankheitszustand(df_nivese)


df['angepasst'] = (df['Krankheitstage'] - 2).clip(lower=0)
sns.countplot(data=df, y='angepasst', order=sorted(df['angepasst'].unique()))

plt.title("Anzahl der Tage, die die Nivesen schon Symptome zeigen")
plt.xlabel("Anzahl Nivesen")
plt.ylabel("Tage")
plt.savefig("krankheitstage.png", dpi=300, bbox_inches='tight')
plt.show()