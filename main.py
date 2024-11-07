#Tableau de tableaux représentant une grille 3x3
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]

#Affiche la grille gameBoard de manière formatée; Une boucle va s'exécuter trois fois, ce qui correspond à chaque ligne de la grille. 
#Une seconde boucle intérieure permet de sélectionner la colonne. La combinaison des deux boucles permet donc de sélectionner chaque case de la grille.
def printGameBoard():
  for indexRows in range(3):
    print("\n|---|---|---|")
    print("|", end="")
    for indexColumns in range(3):
      print("", gameBoard[indexRows][indexColumns], end=" |") #end permet de remplacer le saut de ligne après un print par le caractère de notre choix, ici | pour formater la grille.
  print("\n|---|---|---|")

printGameBoard()
