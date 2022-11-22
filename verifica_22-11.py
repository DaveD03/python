#1
atleti={"Giuseppe Gullo": [("Corsa campestre",(40,21,0),"Allievi"),("Corsa 100mt",(0,12,0),"Juniores mas"),("Corsa 200mt",(0,29,19),"Juniores mas")],
        "Antonia Barbera": [("Corsa campestre",(0,39,11),"Juniores fem"),("Corsa 100mt",(0,18,0),"Juniores fem"),("Corsa 200mt",(0,0,0),"Juniores fem")],
        "Nicola Esposito": [("Corsa campestre",(0,43,22),"Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas"),("Corsa 200mt",(0,36,19),"Juniores mas")]}
#2
atleti["Davide Dusini"]=[("Corsa campestre",(3,39,11),"Allievi"),("Corsa 100mt",(0,11,5),"Allievi"),("Corsa 200mt",(0,25,0),"Allievi")]
#3
atleti["Giuseppe Gullo"].insert(3,("Corsa ad ostacoli 400mt",(0,40,34),"Alievo"))
atleti["Antonia Barbera"].insert(3,("Corsa ad ostacoli 400mt",(0,39,10),"Alieva"))
atleti["Nicola Esposito"].insert(3,("Corsa ad ostacoli 400mt",(0,40,10),"Alievo"))
atleti["Davide Dusini"].insert(3,("Corsa ad ostacoli 400mt",(0,40,26),"Alievo"))
#4
print(atleti["Giuseppe Gullo"][0])
#controllato 9:29
#5
print("Valori Nicola Esposito")
for i in range(len(atleti["Nicola Esposito"][2])):
  print(atleti["Nicola Esposito"][2][i])
#6
print("Tempo Antonia Barbera: "+str(atleti["Antonia Barbera"][1][1]))
#7
max=0
key="Giuseppe Gullo"
for chiave in atleti.keys():
  if atleti[chiave][1][1][1]>max and atleti[chiave][1][2]=="Juniores mas":
    max=atleti[chiave][1][1][1]
    key=chiave
print(key+" "+str(atleti[key][1]))
#8
min=100
key="Giuseppe Gullo"
for chiave in atleti.keys():
  if(atleti[chiave][2][1][1]<min and atleti[chiave][2][2]=="Juniores mas"):
    min=atleti[chiave][2][1][1]
    key=chiave

print(key+" "+str(atleti[key][2]))
#controllato 9:50
#9
somma1=0
somma2=0
somma3=0
i=0
for chiave in atleti.keys():
  if atleti[chiave][0][2]=="Allievi":
    i+=1
    somma1+=atleti[chiave][0][1][0]
    somma2+=atleti[chiave][0][1][1]
    somma3+=atleti[chiave][0][1][2]

media1=somma1/i
media2=somma2/i
media3=somma3/i
print(str(media1)+","+str(media2)+","+str(media3))
#controllato 10:38
#10
def dati():
  disciplina=input("Inserisci la disciplina: ")
  min=int(input("Inserisci i minuti: "))
  while min<0 or min=="":
    min=int(input("Inserisci i minuti: "))
  sec=int(input("Inserisci i secondi: "))
  while sec<0 or sec=="":
    sec=int(input("Inserisci i secondi: "))
  mil=int(input("Inserisci i millisecondi: "))
  while mil<0 or mil=="":
    mil=int(input("Inserisci i millisecondi: "))
  categoria=input("Inserisci la categoria (Alievi, Juniores fem, Juniores mas) ")
  while categoria!="Alievi" or categoria!="Juniores fem" or categoria!="Juniores mas":
    categoria=input("Inserisci la categoria (Alievi, Juniores fem, Juniores mas) ")
  return (disciplina,(min,sec,mil),categoria)
def popola():
  chiave=input("Inserisci il nome dell'atleta: ")
  for i in range(len(atleti["Giuseppe Gullo"])):
    atleti[chiave].append(dati())
popola()
