noleggio={'AA123BB':[('Giugno',9,1293),('Luglio',9,73231),('Agosto',7,4020),('Settembre',6,3928)],
           'AB345CD':[('Giugno',8,1391),('Luglio',6,1234),('Agosto',9,4932),('Settembre',8,2872)],
           'CD456FF':[('Giugno',7,2872),('Luglio',6,3273),('Agosto',4,3211),('Settembre',8,2827)]}

#2
aggiungi={"ZZ999DD":[('Giugno',10,6000),('Luglio',10,6000),('Agosto',10,6000),('Settembre',10,6000)]}
noleggio.update(aggiungi)
#3
print("Info di luglio della targa AA123BB "+str(noleggio["AA123BB"][1]))
#4
print("Numero di noleggi di luglio per la targa AA123BB "+str(noleggio["AA123BB"][1][0]))
#5
somma=0
for i in range(len(noleggio)):
  somma+=noleggio["AB345CD"][i][2]
print("Somma chilometri AB345CD "+str(somma))
#6
somma=0
for chiave in noleggio.keys():
  for i in range(len(noleggio)):
    somma+=noleggio[chiave][i][2]
print("Somma chilometri di tutti "+str(somma))
#7
max=0
for i in range(len(noleggio)):
    if noleggio["CD456FF"][i][2]>max:
      max=noleggio["CD456FF"][i][2]
      massimo=noleggio["CD456FF"][i]
print("Il mese che sono stati fatti più chilometri è: "+str(massimo))
