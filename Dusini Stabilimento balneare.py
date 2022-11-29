stab={}

def popola():
  codice=input("Inserisci il codice dello stabilimento: ")
  fila=int(input("Inserisci il numero della fila: "))
  numero=int(input("Inserisci il numero dell'ombrellone: "))
  sdraio=int(input("Inserisci il numero di sdraio: "))
  lettini=int(input("Inserisci il numero di lettini: "))
  while sdraio+lettini>3:
    print("Hai inserito troppi lettini/sdraio (tot max 3) ")
    sdraio=int(input("Inserisci il numero di sdraio: "))
    lettini=int(input("Inserisci il numero di lettini: "))
  alta=int(input("Inserisci il prezzo in alta stagione: "))
  bassa=int(input("Inserisci il prezzo in bassa stagione: "))
  giorno=int(input("Giorno di prenotazione: "))
  mese=int(input("Mese di prenotazione: "))
  anno=int(input("Anno di prenotazione: "))
  while mese!=6 and mese!=7 and mese!=8 and mese!=9:
    print("Non si può prenotare in questa data reinserisci ")
    giorno=int(input("Giorno di prenotazione: "))
    mese=int(input("Mese di prenotazione: "))
    anno=int(input("Anno di prenotazione: "))
  g=int(input("Inserisci il numero di giorni che hai prenotato: "))
  totale=0
  if mese==8 or mese==7:
    totale+=alta*g+sdraio*1/3+lettini*1/2
  elif mese==6 or mese==9:
    totale+=bassa*g+sdraio*1/3+lettini*1/2

  stab[codice]=[(fila,numero),(bassa,alta),(giorno,mese,anno),g,(sdraio,lettini), totale]

def ombrellone():
  fila=int(input("Metti il numero della fila: "))
  numero=int(input("Metti il numero dell'ombrellone"))
  for chiave in stab.keys():
    if stab[chiave][0][0]==fila and stab[chiave][0][1]==numero:
      return chiave

def mostra():
  print(stab)
  
def riduzione():
  x=int(input("di quanto vuoi ridurre il prezzo?(%) "))
  for chiave in stab.keys():
    stab[chiave][5]=stab[chiave][5]*x/100

def totIncasso():
  tot=0
  x=int(input("Inserisci il mese per visualizzare il totale dell'incasso: "))
  for chiave in stab.keys():
    if stab[chiave][2][1]==x:
      tot+=stab[chiave][5]


scelta=1
while (scelta!=0):
  print('0) Esci')
  print('1) Popola')
  print('2) Mostra le prenotazioni di un ombrellone')
  print('3) Mostra tutte le prenotazioni')
  print('4) Riduzione prezzo percentuale')
  print("5) Calcolo l'incasso totale di un mese")
  print('6) Visualizza le prenotazioni di n mesi')
  scelta=int(input('Scegli :'))
  if scelta==1:
    popola()
  elif scelta==2:
    print(stab[ombrellone()])
  elif scelta==3:
    mostra()
  elif scelta==4:
    riduzione()
  elif scelta==5:
    totIncasso()

