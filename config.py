import tkinter as tk

# ----------------- CONFIGURATION DU LABYRINTHE -----------------
WIDTH = 17 # Largeur du plateau
HEIGHT = 17  # Hauteur du plateau
PROBA = 0.02 # remplissage de 2%
DIM_CASE = 20 # dimension des cases
TP = 0 # nombre de paire de case de teleportation
PASTILLE = 0 # nombre de pastille

DEPART = (0, 0) # case départ
ARRIVEE = (HEIGHT - 1, WIDTH - 1) # case d'arrivée

DIRECTIONS = { # Direction possibles
    #     y   x
    'N': [-2, 0],
    'S': [2, 0],
    'E': [0, 2],
    'O': [0, -2]
}

# Liste des directions possibles pour les pastilles
DIRECTION_PASTILLE = []

# Directions possibles pour les pastilles
for dx in range(-5, 6):
    for dy in range(-5, 6):
        if dx*dx + dy*dy <= 25:
            DIRECTION_PASTILLE.append((dx, dy))

murs = []
libres = []
plateau = [[1 for _ in range(WIDTH)] for _ in range(HEIGHT)]
teleport = []
pastille = []

# Fenêtre
affichage = tk.Tk()
affichage.title("Labyrinthe")
icon = tk.PhotoImage(file = 'image/icon.png') 
affichage.iconphoto(False, icon)
btn_size = 20

canvas = tk.Canvas(affichage, width=WIDTH * DIM_CASE, height=HEIGHT * DIM_CASE)
canvas.pack()

# ----------------- METHODES RESOLUTION / CONSTRUCTION LABYRINTHE -----------------

# Liste d'adjacence dynamique
def liste_adj():
    nodes = {}
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # N, S, E, O

    # Ajout des cases libres
    for l, c in libres:
        nodes[(l, c)] = []

        for dl, dc in dir:
            if (l + dl, c + dc) in libres:
                nodes[(l, c)].append((l + dl, c + dc))

    # Ajout des cases de teleportation
    for tp in teleport:
        nodes[tp[0]].append(tp[1])
        nodes[tp[1]].append(tp[0])


    return nodes


# Reset le labyrinthe (etat initiale)
def empty_lab():
    empty_lab = [[1 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for l, c in (libres):
        empty_lab[l][c] = 0

    for tp in (teleport):
        for l, c in (tp):
            empty_lab[l][c] = -1

    for l, c in pastille:
        empty_lab[l][c] = -2

    return empty_lab

# Fonction pour dessiner le plateau sur le Canvas (remplace les 0 et 1 par des cases noires et blanches)
def draw_plateau(plateau):
    canvas.delete("all") # permet d'effacer le contenu affiché sur la canvas (refresh)

    # Récupère tout les coordonnées des tp → liaison visuelle
    for tp in range(len(teleport)):
        canvas.create_text(teleport[tp][0][0], teleport[tp][0][1], text=f'{tp}', fill='lime')
        canvas.create_text(teleport[tp][1][0], teleport[tp][1][1], text=f'{tp}', fill='lime')

    for l in range(HEIGHT):
        for c in range(WIDTH):
            # Couleur par défaut
            color = 'gray'
            outline = 'black'

            match (plateau[l][c]):
                # CASE LIBRE
                case 0:
                    color = 'white'

                # MUR
                case 1:
                    color = 'black'

                # DFS
                case 2:
                    color = 'blue'
                
                # DIJKSTRA
                case 3:
                    color = 'red'
                
                # BLINKY
                case 4:
                    color = 'lime'

                # JOUEUR
                case 5:
                    color = 'yellow'

                # TP
                case -1:
                    color = 'purple'

                # PASTILLE
                case -2:
                    color = 'gray'

            canvas.create_rectangle(l * DIM_CASE, c * DIM_CASE, (l + 1) * DIM_CASE, (c + 1) * DIM_CASE, fill=color, outline=outline)
