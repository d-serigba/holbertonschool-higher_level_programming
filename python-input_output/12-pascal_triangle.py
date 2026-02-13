#!/usr/bin/python3

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of size n"""
    if n <= 0:
        return []

    triangle = [[1]]  # Première ligne du triangle

    for i in range(1, n):
        prev_row = triangle[i - 1]  # Ligne précédente
        row = [1]  # Chaque ligne commence par 1

        # Calcul des éléments internes
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Chaque ligne finit par 1
        triangle.append(row)

    return triangle
