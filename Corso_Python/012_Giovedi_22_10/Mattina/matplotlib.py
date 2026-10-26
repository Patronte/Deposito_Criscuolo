# La visualizzazione è la capacità a livello grafico, di comunicare i dati
# e comunicare i dati, la visualizzazione dei dati è una delle 3 parti essenziali per l'analisi dei dati
# esistono due librerie matplotlib e suo figlio Seaborn
# matplotlib è l'elemento un po' + leggero, Seaborn è la sua evoluzione
# cosa cambia fra le due? PLT è la base, Seaborn introduce dei grafici + complessi
# La visualizzazione dei dati ha questi scopi: ha 3 punti importanti:
# l'informativo:, 
# l'esplorativo: è solo per noi programmatori, 
# Narrativo:ne esiste un terzo per chi deve vendere,spendere,spiegare quei grafici
import matplotlib as plt

x=[1,2,3,4,5]
y=[2,3,5,7,11]

plt.figure()
plt.plot(x,y)

#extra
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
