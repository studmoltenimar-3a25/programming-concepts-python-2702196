print("Dimmi quale prodotto vuoi comprare")
def applica_sconto_benvenuto(prezzo_iniziale, prezzo_maglietta, prezzo_scarpe, prezzo_pantaloni, prezzo_scontato):
  prezzo_maglietta=10
  prezzo_scarpe=80
  prezzo_pantaloni=50
  prezzo_iniziale=f"{prezzo_maglietta}"
  prezzo_iniziale=f"{prezzo_scarpe}"
  prezzo_iniziale=f"{prezzo_pantaloni}"
  prezzo_scontato=prezzo_iniziale-5
  print ("Il prezzo scontato è:",prezzo_scontato)
  return prezzo_scontato

