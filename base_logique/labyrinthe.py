import config
import random

# Méthode de génération du labyrinthe
def generer_labyrinthe():
    plateau = [[1 for _ in range(config.WIDTH)] for _ in range(config.HEIGHT)] # reset plateau
    x = 0
    y = 0

    plateau[x][y] = 0
    directions = ['N', 'S', 'E', 'O']
    pile = []
    pile.append([x, y])

    # Tant que la pile n'est pas vide
    while (len(pile) > 0):
        
        possible = []

        # Regarde les position possibles (physiquement / Logiquement)
        for d in (directions):
            if (
                (d == 'N' and y - 2 >= 0 and
                plateau[x][y - 1] == 1 and
                plateau[x][y - 2] == 1) or
                (d == 'S' and y + 2 < config.HEIGHT and
                plateau[x][y + 1] == 1 and
                plateau[x][y + 2] == 1) or
                (d == 'E' and x + 2 < config.WIDTH and
                plateau[x + 1][y] == 1 and
                plateau[x + 2][y] == 1) or
                (d == 'O' and x - 2 >= 0 and
                plateau[x - 1][y] == 1 and
                plateau[x - 2][y] == 1)
                ):
                possible.append(d)

        # Directions possibles
        if (len(possible) > 0):
            rdm = random.choice(possible) # génère une direction

            # Nord
            if (rdm == 'N' ):
                plateau[x][y - 1] = 0
                plateau[x][y - 2] = 0
                pile.append([x, y - 2])
                y -= 2 # Maj pos Y

            # Sud
            elif (rdm == 'S' ):
                plateau[x][y + 1] = 0
                plateau[x][y + 2] = 0
                pile.append([x, y + 2])
                y += 2 # Maj pos Y

            # Est
            elif (rdm == 'E' ):
                plateau[x + 1][y] = 0
                plateau[x + 2][y] = 0
                pile.append([x + 2, y])
                x += 2 # Maj pos X

            # Ouest
            elif (rdm == 'O' ):
                plateau[x - 1][y] = 0
                plateau[x - 2][y] = 0
                pile.append([x - 2, y])
                x -= 2 # Maj pos X
            
            config.draw_plateau(plateau)

        # Dépiler
        else:
            pile.pop()
            if (len(pile) > 0):
                x = pile[len(pile) - 1][0]
                y = pile[len(pile) - 1][1]

        config.affichage.update()

    murs = []
    config.libre.clear()

    for l in range(len(plateau)):
        for c in range(len(plateau[l])):
            if (plateau[l][c] == 1):
                murs.append([l, c])
            elif (plateau[l][c] == 0):
                config.libre.append((l, c))
   
    # Récupère i valeurs du tableau mur (mélangé)
    random.shuffle(murs)
    for i in range(int(len(murs) * config.PROBA)):
        plateau[murs[i][0]][murs[i][1]] = 0

    # affichage.update()
    config.draw_plateau(plateau)

    print(config.matAdj(), '\n')