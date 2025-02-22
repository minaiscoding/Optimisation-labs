# display_solution.py
def display_solution(solution, chromatic_number):
  
    print("Nombre chromatique :", chromatic_number)
    print("affectation des couleurs :")
    color_groups = {}
    for vertex, color in enumerate(solution):
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(vertex)

    for color, vertices in sorted(color_groups.items()):
        print(f"Couleur {color}: {vertices}")