import networkx as nx
import matplotlib.pyplot as plt

# Constantes
INFINI = 1000

# Création des sommets et arêtes
nodes = {
    'a': {'b':{'weight': 1}, 'c':{'weight': 2}},
    'b': {},
    'c': {'d':{'weight': 1}},
    'd': {'e':{'weight': 2}, 'f':{'weight': 1}, 'g':{'weight': 20}, 'b':{'weight': 1}},
    'e': {'g':{'weight': 3}},
    'f': {'g':{'weight':1}},
    'g': {}
}

# Création des positions 
positions = {
    'a': (0, 0.25),
    'b': (1, 0.5),
    'c': (1, 0),
    'd': (2, 0.25),
    'e': (3, 0.5),
    'f': (3, 0),
    'g': (4, 0.25)
}

# Etape 0
sin = 'a' # sommet depart (reste constant)
send = 'b' # sommet d'arrivée

dist = {} # taille par defaut de chaque sommet
for n in nodes.keys():
    if (n == sin):
        dist[n] = 0
    else:
        dist[n] = INFINI

pred = {} # prédécesseur par defaut de chaque sommet
for n in nodes.keys():
    pred[n] = None

Q = [] # pile sommet non visité
for s in nodes.keys():
    Q += [s]

# Etape 1
u = sin # sommet à poid minimale (prend par défaut le sommet initial)

tour = 1
print(dist)
while(len(Q) > 0):

    dist_min = INFINI # distance la plus courte

    print('\ntour', tour)
    # recherche du sommet avec la distance minimale
    for s in Q:
        if (dist[s] < dist_min):
            dist_min = dist[s] 
            u = s

    print('marqué (supprimé) le sommet', u)

    Q.remove(u)
    print(Q)

    for v in nodes[u]:
        if (dist[u] + nodes[u][v]['weight'] < dist[v]):
            dist[v] = dist[u] + nodes[u][v]['weight']
            pred[v] = u

    tour+=1

# Par du sommet de fin vers le sommet de départ avec ses prédécesseurs
chemin = [send]
while (chemin[0] != sin and [pred[chemin[0]]] != None):
    chemin = [pred[chemin[0]]] + chemin

#  ----------------- CREATION DU GRAPHE (matplot.lib) -----------------

# Colorier les sommets
color_graphe = []
for n in nodes:
    if (n == sin):
        color_graphe += ["blue"]
    elif (n == send):
        color_graphe += ["red"]
    else:
        color_graphe += ["gray"]

# Colorier les arrêtes (celle du chemin minimale)
edge_chemin = []
for n in nodes.keys():
    for e in nodes[n]:
        color = False
        for i in range(len(chemin)-1):
            if (n == chemin[i] and e == chemin[i+1]):
                color = True

        if (color):
            edge_chemin += ["lime"]
        else:
            edge_chemin += ["black"]


# Taille de la fenetre
plt.figure(figsize=(5,5))

# Créer l'objet NetworkX 
G = nx.DiGraph(nodes)
poids = nx.get_edge_attributes(G,'weight')

# Titre
plt.title(f'chemin min de {sin} → {send} : {chemin}')

# Dessiner le graphe avec les positions définies
nx.draw(G, pos=positions, with_labels=True, node_color=color_graphe, edge_color=edge_chemin, node_size=800, font_weight='bold')
nx.draw_networkx_edge_labels(G,positions,edge_labels=poids)

plt.show()