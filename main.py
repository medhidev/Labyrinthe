# Modules externes
import tkinter as tk

# Modules du projet
import dijkstra
import labyrinthe
import blinky
import dfs
import config
import manual
import comparaison

# Liste des boutons
labyrinthe.button.pack(ipady=4, pady=5)    # Labyrinthe
dfs.button.pack(ipady=4, pady=5)           # DFS
dijkstra.button.pack(ipady=4, pady=5)      # Dijkstra
blinky.button.pack(ipady=4, pady=5)        # Blinky
manual.button.pack(ipady=4, pady=5)        # Joueur
comparaison.button.pack(ipady=4, pady=5)   # Comparaison

# Lancer la boucle principale de l'application 
config.frame.mainloop() # permet de garder la fenêtre ouverte en attendant les interactions de l'utilisateur.
