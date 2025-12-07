import tkinter as tk
import config
import tkinter.messagebox as msb
import dijkstra

# Instance variable globale
l, c = 0, 0
nb_case = 0

def move(event, plateau):
    global l, c
    global nb_case

    match(event.keysym):
        case 'Up':
            if (c-1 >= 0):
                if (plateau[l][c-1] == 5):
                    plateau[l][c] = 0
                    nb_case -= 1
                if (plateau[l][c-1] != 1):
                    c -= 1
        case 'Down':
            if (c+1 < config.HEIGHT ):
                if (plateau[l][c+1] == 5):
                    plateau[l][c] = 0
                    nb_case -= 1
                if (plateau[l][c+1] != 1):
                    c += 1
        case 'Left':
            if (l-1 >= 0):
                if (plateau[l-1][c] == 5):
                    plateau[l][c] = 0
                    nb_case -= 1
                if (plateau[l-1][c] != 1):
                    l -= 1
        case 'Right':
            if (l+1 < config.WIDTH):
                if (plateau[l+1][c] == 5):
                    plateau[l][c] = 0
                    nb_case -= 1
                if (plateau[l+1][c] != 1):
                    l += 1

    if (plateau[l][c] == 0):
        plateau[l][c] = 5
        nb_case += 1

    config.draw_plateau(plateau)

    # Trouve la dernière case
    if ((l, c) == config.ARRIVEE):
        l = 0
        c = 0
        message = f"Resolution du labyrinthe avec succès !\nNombre de case : {nb_case}"

        if (nb_case == len(dijkstra.court_chemin)):
            message += f"\nVous avez en plus trouvé le chemin le plus court !"
        elif (nb_case > len(dijkstra.court_chemin) and len(dijkstra.court_chemin) != 0):
            message += f"\nchemin plus court : {len(dijkstra.court_chemin)}"
        msb.showinfo('Resolution Labyrinthe', message)


color = 'orange'
button = tk.Button(config.affichage, text="Resolution Joueur", state='disabled', width=config.btn_size, 
                   bd=1, relief='solid', command=lambda : deplacement())

def deplacement():
    # reset nb_case
    global nb_case
    nb_case = 1 # prend en compte la case de départ

    plateau = config.empty_lab()
    plateau[config.DEPART[0]][config.DEPART[1]] = 5 # colorié au départ la première case
    
    config.affichage.bind("<Key>", lambda event : move(event, plateau))
    config.draw_plateau(plateau) # affichage case de départ
    