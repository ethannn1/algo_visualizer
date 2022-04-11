ALGO VISUALIZER

Idée générale:
Faire un programme qui permet de visualiser des algorithmes de tri (ou autre) avec pygame

Structures de données:
-Listes 2D
-Liste 3D
-Liste chaînées

Décomposition en sous problèmes:
-Pour chaque structure de données faire une fonction qui permet de la visualiser
-Pour chaque algorithme, l'implémenter et faire qu'à chaque étape il appelle la fonction précédente
-Faire des fonctions permettant de mettre en pause/controler la vitesse de l'animation

A faire:
-Implémenter des différents algorithmes
-Faire une fonction permettant d'afficher chaque étape

MVP:
La possibilité de pouvoir visualiser quelques algorithmes de tri

Projet final:
Avoir un menu naviguable où on peut choisir le type d'algorithme à visualiser ainsi que l'algorithme en question.  

Fonctions et classes:
display_list(list, int, int) -> None:
  Permet d'afficher une liste qui est en train d'être triée à l'écran.
  
selection_sort(list) -> list:
  Permet d'effectuer le tri par selection d'une liste et afficher cette liste
  à chaque étape du tri grâce à display_list()
  
insertion_sort(list) -> list:
  Permet d'effectuer le tri par insertion d'une liste et afficher cette liste
  à chaque étape du tri grâce à display_list()
  
class Bouton:
  représente un bouton clickable 
  
  display():
    Permet d'afficher le bouton
  
  run():
    appelle constamment la fonction display() et vérifie les collisions avec le curseur de la souris
 
