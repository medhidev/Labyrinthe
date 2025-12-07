import tkinter as tk
import random

import config
import dijkstra
import dfs
import blinky
import manual

color = 'black'
button = tk.Button(config.frame, text="Générer un Labyrinthe", command=lambda : generer_labyrinthe(), width=config.btn_size, 
                   bd=1, relief='solid')
generer = False

# Méthode de génération du labyrinthe
def generer_labyrinthe():
    dijkstra.court_chemin = [] # reset court chemin dijkstra
    plateau = [[1 for _ in range(config.WIDTH)] for _ in range(config.HEIGHT)] # reset plateau
    l = config.DEPART[0]
    c = config.DEPART[1]

    plateau[l][c] = 0
    pile = []
    pile.append([l, c])

    murs = []
    libres = []
    teleport = []


    # Tant que la pile n'est pas vide
    while (len(pile) > 0):
        
        possible = []

        # Regarde les position possibles (physiquement / Logiquement)
        for d in (config.DIRECTIONS.keys()):
            if ((d == 'N' and c - 2 >= 0 and plateau[l][c - 1] == 1 and plateau[l][c - 2] == 1) or
                (d == 'S' and c + 2 < config.HEIGHT and plateau[l][c + 1] == 1 and plateau[l][c + 2] == 1) or
                (d == 'E' and l + 2 < config.WIDTH and plateau[l + 1][c] == 1 and plateau[l + 2][c] == 1) or
                (d == 'O' and l - 2 >= 0 and plateau[l - 1][c] == 1 and plateau[l - 2][c] == 1)):
                possible.append(d)

        if (len(possible) > 0):
            rdm = random.choice(possible) # choisi une direction parmis la liste des possibles

            # Nord
            if rdm == 'N':
                plateau[l][c - 1] = 0
                plateau[l][c - 2] = 0
                c -= 2 # Maj position colonne

            # Sud
            elif rdm == 'S':
                plateau[l][c + 1] = 0
                plateau[l][c + 2] = 0
                c += 2 # Maj position colonne

            # Est
            elif rdm == 'E':
                plateau[l + 1][c] = 0
                plateau[l + 2][c] = 0
                l += 2 # Maj position ligne

            # Ouest
            elif rdm == 'O':
                plateau[l - 1][c] = 0
                plateau[l - 2][c] = 0
                l -= 2 # Maj position ligne
            
            pile.append([l, c])
            config.draw_plateau(plateau)

        # Dépiler
        else:
            pile.pop()
            if (len(pile) > 0):
                l = pile[len(pile) - 1][0]
                c = pile[len(pile) - 1][1]

        config.frame.update()

    # Case 0 et 1
    for lm in range(len(plateau)):
        for cm in range(len(plateau[l])):
            if (plateau[lm][cm] == 1):
                murs.append([lm, cm])
            elif (plateau[lm][cm] == 0):
                libres.append((lm, cm))
   
    # Gestion des 2%
    random.shuffle(murs)
    for i in range(int(len(murs) * config.PROBA)):
        plateau[murs[i][0]][murs[i][1]] = 0
        libres.append((murs[i][0], murs[i][1]))

    # Amelioration 2 - Pastille

    config.pastille = []  # Réinitialise la liste des pastilles

    cases_possibles = []
    for case in libres:

        # Vérifie que la case n'est pas le départ ou l'arrivée
        if case != config.DEPART and case != config.ARRIVEE:
            cases_possibles.append(case)
            random.shuffle(cases_possibles)
    
    # Choisit 3 cases aléatoires pour les pastilles
    for i in range(min(config.PASTILLE, len(cases_possibles))):
        l, c = cases_possibles[i]
        plateau[l][c] = -2
        config.pastille.append((l, c))

    # Amelioration 1 - Teleportation
    if config.TP*2 <= len(libres):
        i = 0
        while (i < config.TP):
            tp1 = random.choice(libres)
            tp2 = random.choice(libres)

            if tp1 == tp2:
                tp2 = random.choice(libres)

            elif (tp1 not in teleport) and (tp2 not in teleport):
                teleport.append([tp1, tp2])
                i += 1

        for tp in (teleport):
            for l, c in (tp):
                plateau[l][c] = -1

        
    else:
        print('nombre de case de teleportation trop grande')


    # Maj des données (matrice, murs, lignes, tp)
    config.plateau = plateau
    config.murs = murs
    config.libres = libres
    config.teleport = teleport

    # frame → colorie la matrice
    config.draw_plateau(plateau)

    generer = True
    if (generer):
        # Changement etat
        dijkstra.button['state'] = 'normal'
        dfs.button['state'] = 'normal'
        blinky.button['state'] = 'normal'
        manual.button['state'] = 'normal'

        # Changement couleur
        dijkstra.button['foreground'] = dijkstra.color
        dfs.button['foreground'] = dfs.color
        blinky.button['foreground'] = blinky.color
        manual.button['foreground'] = manual.color