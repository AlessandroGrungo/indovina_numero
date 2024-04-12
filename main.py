# Esercizio “Indovina il Numero”
# Realizzare un programma Python utilizzando la libreria FLET che sia in grado di
# permettere all'utente di giocare ad "indovina il numero".
# In ogni partita, il programma deve inventare un numero casuale tra 1 e NMAX
# (estremi compresi), e l'utente deve tentare di indovinare il numero segreto. Ad ogni
# tentativo, il programma potrà rispondere in tre modi: "Numero esatto" (ed in tal caso
# la partita termina), "Troppo basso", "Troppo alto".
# L'utente ha un numero di tentativi limitato TMAX per poter indovinare il numero
# segreto. In ogni momento, il programma visualizza il numero di tentativi ancora
# disponibili.
# Una partita può terminare perché il numero è stato indovinato, oppure perché sono
# stati esauriti tutti i tentativi disponibili (ed in questo caso il programma mostra il
# numero segreto). Al termine di una partita se ne può iniziare una nuova, con un
# nuovo numero casuale.

import flet as ft
from controller import Controller
from view import View


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)
