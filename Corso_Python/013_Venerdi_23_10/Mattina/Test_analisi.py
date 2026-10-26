import pandas as pd
import numpy as np
# Percorso del file CSV
product_data = 'dati_caramelle.csv'

marketing_data = 'dati_vendita_caramelle.csv'

#Caricamento dei dati nel DataFrame

dfpd=pd.read_csv(product_data)

dfmd=pd.read_csv(marketing_data)

#le prime righe del DataFrame per confermare

#print(df.head())

# Visualizzazione delle statistiche descrittive

#print(df.describe())

# Rimozione dei valori mancanti

#df_clean = df.dropna()

#Unione dei DataFrame
 
df_merge = pd.merge(dfpd,dfmd , on='competitorname')

#riprovo a eliminare valori mancanti post unione (fatto una sola volta) 
#df_clean = dfpd.dropna()
#df_clean = dfmd.dropna()
#df_clean = df_merge.dropna()
df_clean = df_merge.dropna() #per sicurezza ho deciso di tenermelo ad ogni giro
#provo a creare una maschera booleana che mi veda 1 ==True 0==False alla colonna 'chocolate' e mi prende il dato solo se è true

# Selezione delle righe dove chocolate == 1
chocolaten = df_merge[df_merge['chocolate'] == 1]
#creo una tabella pivot con indice il nome comp, colonne le zone, e valori il numero di uni vendt
pivot_table1= df_merge.pivot_table(index='competitorname', columns='area_vendita', values='unita_vendute') #perfetto questo è quasi giusto mi manca il fattore cioccolata

#creo la tbpivot con la condizione di cioccolata, sembra aver funzionato, rispetto alla tabella precedente ho molte meno voci in competitorname
pivot_au_chocolat= chocolaten.pivot_table(index='competitorname', columns='area_vendita', values='unita_vendute') 
#print(pivot_table)

pivot_au_chocolat.to_html('tabella_vendite_di_competitor_per_area2.html')

