
<h1 align="center">
  <br>
    <img src="image/icon.png" width="200">
  <br>
  Labyrinthe
  <br>
</h1>

<!-- Badges -->
<p align="center">
    <!-- Informations projet -->
    <img src="https://img.shields.io/badge/version-1.0-00994C">
    <img src="https://img.shields.io/badge/python-3.11.9-f5e042?logo=python">
    <img src="https://img.shields.io/github/license/medhidev/Labyrinthe">
    <br>
    <!-- Statistiques projet -->
    <!-- <img src="https://img.shields.io/github/v/release/medhidev/Labyrinthe"> -->
    <img src="https://img.shields.io/github/stars/medhidev/Labyrinthe">
    <img src="https://img.shields.io/github/watchers/medhidev/Labyrinthe">
    <img src="https://img.shields.io/github/issues/medhidev/Labyrinthe">
</p>

## Présentation

Ce projet propose une interface interactive de résolution de chemin sur une grille. L’utilisateur peut placer des murs, définir un point de départ et d’arrivée, puis visualiser le plus court chemin trouvé automatiquement selon l’algorithme choisi. L’objectif est de rendre l’exploration des algorithmes de pathfinding accessible, visuelle et intuitive.
<br><br>

<!-- Image de presentation -->
<!-- <p align="center">
    <img src="presentation/presentation.gif">
<p> -->

## Fonctionnalités

- Interface utilisateur avec Tkinter
- Implémentation d'algorithmes de résolution de plus court chemin
  - Dijkstra
  - A*
  - DFS
- Résolution manuel
- Comparaison efficacité de résolution (MatplotLib)

## Setup du projet

Pour utiliser cette application, il vous faut au préalable installer [Python](https://www.python.org/downloads/).<br>
Une fois installer lancer l'outil [Git](https://git-scm.com), puis taper les commandes suivantes.

```bash
# Téléchargement avec git du projet en local
$ git clone https://github.com/medhidev/path_solver

# Aller dans le dossier racine du projet
$ cd path_solver

# Installation des dépendances
$ pip install -r requirements.txt

# Lancement du projet
$ python -m main.py

```

<p align="center">
    <a href="https://github.com/medhidev/path_solver/releases/download/alpha/Path_Solver.exe">
      <img src="https://img.shields.io/badge/T%C3%A9l%C3%A9charger labyrinthe-00994C?style=for-the-badge">
    </a>
</p>

## Ressources

Pour réaliser cette application, je me suis appuyé sur les ressources suivantes :

#### Contexte d'utilisation
- [Sujet de départ](support/sujet_SAE01_S202.pdf)
- [Documentation Tkinter](https://docs.python.org/fr/3.13/library/tkinter.html)

#### Algorithmes
- [Algorithme Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)
- [Algorithme A*](https://fr.wikipedia.org/wiki/Algorithme_A*)
- [Algorithme DFS](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)


## Note de Soutien

Si vous appréciez l’idée de ce projet et souhaitez encourager mon travail ainsi que mes futurs projets, vous pouvez me soutenir en faisant un don. Votre retour et vos encouragements me motivent à partager et à innover.
Donc un immense merci d’avance à toutes celles et ceux qui prendront le temps de contribuer ¯\\\_(ツ)_/¯

<a href="http://coff.ee/medhidev" target="_blank"><img src="https://github.com/amitmerchant1990/electron-markdownify/raw/master/app/img/bmc-button.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

---
