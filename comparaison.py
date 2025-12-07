from numpy import *
import matplotlib.pyplot as plt

import tkinter as tk
import dijkstra
import dfs
import blinky
import config

color = 'gray'
button = tk.Button(config.affichage, text="Comparaison Algo", command=lambda : compare(), width=config.btn_size, bd=1, relief='solid')

def compare():

    # Légende
    labels = ['DFS', 'Dijkstra', 'Blinky']
    colors = ['b-o', 'r-o', 'g-o']
    plt.title("Comparaison des algos de recherche")
    plt.xlabel('nombre de cases parcouru')
    plt.ylabel('temps d\'execution')

    # Données
    nb_cases = [len(dfs.court_chemin), len(dijkstra.court_chemin), len(blinky.chemin_court)]
    temps = [dfs.dfs_time, dijkstra.dij_time, blinky.blinky_time]
    
    
    for i in range(len(temps)): # affiche chaque données des algos
        plt.plot([0, nb_cases[i]], [0, temps[i]], colors[i], label=labels[i], linewidth=2)
        plt.legend()

    plt.show()
