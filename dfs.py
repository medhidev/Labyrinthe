import tkinter as tk
import config
import time
import math

# Données - Amélioration 
dfs_time = 0
court_chemin = []

color = 'blue'
button = tk.Button(config.frame, text="Resolution DFS", command=lambda : dfs(), state='disabled', width=config.btn_size, bd=1, relief='solid')

def dfs():
    global dfs_time
    global court_chemin
    start_time = time.perf_counter()

    plateau = config.empty_lab()

    # Initialisation
    x, y = config.DEPART
    sommet_arrivee = config.ARRIVEE
    pile = [(x, y)]

    while pile != 0 and (x, y) != sommet_arrivee: 
        x, y = pile[-1]

        # Marque la case comme visitée
        if plateau[x][y] == 0 or plateau[x][y] == -2:
            plateau[x][y] = 2

        # Directions de base
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  

        # Si sur pastille, on peut aller dans toutes les directions
        if (x, y) in config.pastille:
            dir = config.DIRECTION_PASTILLE
        
        case_disponible = False

        # Vérifie les cases adjacentes et ajoute à la pile
        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            # Vérifie les limites et les cases libres ou les pastilles
            if (0 <= nx < config.WIDTH and 0 <= ny < config.HEIGHT) and (plateau[nx][ny] == 0 or plateau[nx][ny] == -2 or plateau[nx][ny] == -1) :
                
                pile.append((nx, ny))
                court_chemin.append((nx, ny))
                
                plateau[x][y] = 2
                x, y = nx, ny
                case_disponible = True
                break

        # Si aucune case disponible on pop la pile
        if case_disponible == False:
            if len(pile) != 0:
                x, y = pile.pop()
                plateau[x][y] = 2

        if (x, y) == sommet_arrivee:
            plateau[x][y] = 2

        # Met à jour l'frame
        config.draw_plateau(plateau)
        config.frame.update()
        time.sleep(0.05)

    if len(pile) == 0:
        print("Aucun chemin trouvé")

    end_time = time.perf_counter()
    dfs_time = end_time - start_time