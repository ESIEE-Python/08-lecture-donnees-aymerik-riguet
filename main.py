#### Imports et définition des variables globales
"""importation des modules"""
import csv

FILENAME = "listes.csv"

# Fonctions secondaires
def read_data(filename):
    """
    Retourne le contenu du fichier <filename> sous forme d'une liste de listes d'entiers.

    Args:
        filename (str): Nom du fichier à lire.

    Returns:
        list: Le contenu du fichier (1 liste par ligne).
    """
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        return [[int(value) for value in row] for row in reader]

def get_list_k(data, k):
    """Retourne la k-ième liste."""
    return data[k]

def get_first(lst):
    """Retourne le premier élément d'une liste."""
    return lst[0] if lst else None

def get_last(lst):
    """Retourne le dernier élément d'une liste."""
    return lst[-1] if lst else None

def get_max(lst):
    """Retourne la valeur maximum d'une liste."""
    return max(lst, default=None)

def get_min(lst):
    """Retourne la valeur minimum d'une liste."""
    return min(lst, default=None)

def get_sum(lst):
    """Retourne la somme des valeurs d'une liste."""
    return sum(lst)

# Fonction principale
def main():
    """Fonction principale"""
    data = read_data(FILENAME)
    for index, row in enumerate(data):
        print(index, row)

    k = 37
    if 0 <= k < len(data):
        print(k, get_list_k(data, k))
    else:
        print(f"Index {k} hors limites pour les données fournies.")

if __name__ == "__main__":
    main()
