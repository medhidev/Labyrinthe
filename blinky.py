import tkinter as tk
import config
import math
import time

blinky_time = 0
chemin_court = []

color = 'green'
button = tk.Button(config.affichage, text="Resolution Blinky", command=lambda: blinky(), state='disabled', width=config.btn_size, bd=1, relief='solid')

def blinky():

    # début du chrono
    global chemin_court
    global blinky_time
    start_time = time.perf_counter()
    plateau = config.empty_lab()

    # Constantes
    INFINI = 100000

    # Récupération des noeuds et adjacence
    nodes = config.liste_adj()
    
    # Étape 0 - Initialisation
    depart = config.DEPART
    arrivee = config.ARRIVEE
    
    Q = [depart]
    distances = {}
    for node in nodes:
        distances[node] = INFINI
    distances[depart] = 0

    predecesseurs = {}
    for node in nodes:
        predecesseurs[node] = None

    # Étape 1 Recherche
    while Q != []:  
        # Trouver le noeud avec la plus petite distance
        u = None
        for node in Q:
            if u is None or distances[node] < distances[u]:
                u = node

        Q.remove(u)
        
        # Vérifier les voisins de u
        for v in nodes[u]:
            dist_uv = math.sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2)
            dist_v_arrivee = math.sqrt((arrivee[0] - v[0])**2 + (arrivee[1] - v[1])**2)
            nouvelle_dist = distances[u] + dist_uv + dist_v_arrivee  
            
            if nouvelle_dist < distances[v]:
                distances[v] = nouvelle_dist
                predecesseurs[v] = u
                if v not in Q:
                    Q.append(v)
    
    # Étape 2 - Chemin
    if arrivee in predecesseurs and predecesseurs[arrivee] is not None:
        chemin = [arrivee]
        while chemin[0] != depart:
            chemin.insert(0, predecesseurs[chemin[0]])
        
        # Affichage progressif du chemin
        for x, y in chemin:
            if (x, y) in config.libres:
                plateau[x][y] = 4
                chemin_court.append((x, y))
                config.draw_plateau(plateau)
                config.affichage.update()
                time.sleep(0.05)
    else:
        print("Aucun chemin trouvé")

    # temps de résolution
    end_time = time.perf_counter()
    blinky_time = end_time - start_time