import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import config
import time

# Données - Amélioration 
dij_time = 0
court_chemin = []

color = 'red'
button = tk.Button(config.frame, text="Resolution Dijkstra", command=lambda : dijkstra(), state='disabled', width=config.btn_size,
                   bd=1, relief='solid')
def dijkstra():

    # début du chrono
    global dij_time
    start_time = time.perf_counter()

    # Constantes
    INFINI = 1000
    POID = 1

    nodes = config.liste_adj()

    # Etape 0
    sommet_depart = config.DEPART # sommet depart (reste constant)
    sommet_arrivee = config.ARRIVEE # sommet d'arrivée (en bas à droite)

    Q = []
    chemins = {}

    for node in nodes.keys():
        Q.append(node)
        if node != sommet_depart:
            chemins[node] = [INFINI, None]
        else:
            chemins[node] = [0, None]

    # Etape 1 (Resolution Dijkstra)
    u = sommet_depart
    while (len(Q) > 0):
        dist_min = INFINI

        for s in Q:
            if chemins[s][0] < dist_min:
                dist_min = chemins[s][0]
                u = s

        Q.remove(u)
        
        bonus = 0
        for v in nodes[u]:
            if chemins[u][0] in config.teleport:
                bonus = POID

            if chemins[u][0] + (POID - bonus) < chemins[v][0]:
                chemins[v][0] = chemins[u][0] + (POID - bonus)
                chemins[v][1] = u

    # Etape 2 (Calcul du chemin le plus court)
    global court_chemin
    court_chemin = [sommet_arrivee]

    # Par du sommet de fin vers le sommet de départ avec ses prédécesseurs
    while (court_chemin[0] != sommet_depart and [chemins[court_chemin[0]][1]] != None):
        court_chemin = [chemins[court_chemin[0]][1]] + court_chemin

    # Maj frame plateau
    for l, c in court_chemin:
        if (l, c) in config.libres:
            time.sleep(0.05)
            config.plateau[l][c] = 3

        # Met à jour l'frame
        config.draw_plateau(config.plateau)
        config.frame.update() # met à jour l'frame chaque frame

    # temps de résolution
    end_time = time.perf_counter()
    dij_time = end_time - start_time

    #  ----------------- CREATION DU GRAPHE (matplot.lib) -----------------

    # Colorier les sommets
    # color_graphe = []
    # for n in nodes:
    #     if n == sommet_depart:
    #         color_graphe += ["blue"]
    #     elif n == sommet_arrivee:
    #         color_graphe += ["red"]
    #     else:
    #         color_graphe += ["gray"]

    # # Colorier les arrêtes (celle du chemin minimale)
    # edge_chemin = []
    # for n in nodes.keys():
    #     for e in nodes[n]:
    #         color = False
    #         for i in range(len(court_chemin)-1):
    #             if n == court_chemin[i] and e == court_chemin[i+1]:
    #                 color = True

    #         if color:
    #             edge_chemin += ["lime"]
    #         else:
    #             edge_chemin += ["black"]


    # # Taille de la fenetre
    # plt.figure(figsize=(10,10))

    # # Créer l'objet NetworkX 
    # G = nx.Graph(nodes)

    # # Titre
    # plt.title(f'{court_chemin}')

    # # Dessiner le graphe avec les positions définies
    # pos = nx.spring_layout(G.subgraph(nodes))
    # nx.draw(G, pos, with_labels=True, node_color=color_graphe, edge_color=edge_chemin, node_size=500, font_weight='bold')
    # plt.show()