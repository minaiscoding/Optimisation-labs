import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

def generate_distinct_colors(n):
    """
    Génère n couleurs distinctes en utilisant HSV color space.
    """
    colors = []
    for i in range(n):
        # Variation de la teinte (hue)
        h = i / n
        # Saturation fixe à 0.7 pour des couleurs vives mais pas trop
        s = 0.7
        # Luminosité fixe à 0.9 pour des couleurs claires
        v = 0.9
        # Conversion HSV vers RGB
        rgb = colorsys.hsv_to_rgb(h, s, v)
        colors.append(rgb)
    return colors

def represent_graph(adj_matrix, colors=None):
    """
    Représente le graphe avec sa coloration.
    Supporte un grand nombre de sommets avec des couleurs distinctes.
    
    Args:
        adj_matrix: Matrice d'adjacence du graphe
        colors: Liste des couleurs assignées aux sommets (optionnel)
    """
    plt.close('all')  # Ferme toutes les figures précédentes
  # Nettoie la figure courante
    
    num_nodes = adj_matrix.shape[0]
    num_edges = np.sum(adj_matrix) // 2

    print("\n Statistiques du Graphe ")
    print(f"Nombre de nœuds : {num_nodes}")
    print(f"Nombre d'arêtes : {num_edges}\n")

    # Création du graphe
    G = nx.Graph()
    G.add_nodes_from(range(1, num_nodes + 1))
    
    # Ajout des arêtes
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adj_matrix[i][j] == 1:
                G.add_edge(i + 1, j + 1)

    if colors is not None:
        # Générer autant de couleurs distinctes que nécessaire
        num_colors_needed = max(colors) + 1
        color_palette = generate_distinct_colors(num_colors_needed)
        node_colors = [color_palette[c] for c in colors]
        title = "Graphe avec coloration"
        print(f"\n Utilisation de {num_colors_needed} couleurs distinctes")
    else:
        node_colors = ['lightblue' for _ in range(num_nodes)]
        title = "Graphe initial"

    # Dessin du graphe
    plt.figure(figsize=(15, 10))  # Agrandi pour les grands graphes
    
    # Utiliser un layout plus adapté aux grands graphes
    if num_nodes > 100:
        pos = nx.spring_layout(G, k=1/np.sqrt(num_nodes), iterations=100)
    else:
        pos = nx.spring_layout(G, k=1/np.sqrt(num_nodes), iterations=50)
    
    # Ajuster la taille des nœuds en fonction du nombre total
    node_size = max(50, 2000 / np.sqrt(num_nodes))
    
    # Dessiner les arêtes
    nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.2, width=0.5)
    
    # Dessiner les nœuds
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_colors)
    
    # Ajuster la taille des labels en fonction du nombre de nœuds
    font_size = max(4, 16 / np.sqrt(np.sqrt(num_nodes)))
    nx.draw_networkx_labels(G, pos, font_size=font_size)
    
    plt.title(title)
    
    # Légende pour les couleurs
    if colors is not None:
        unique_colors = sorted(set(colors))
        if len(unique_colors) <= 30:  # Limiter la légende si trop de couleurs
            legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
                             markerfacecolor=color_palette[c],
                             label=f'Couleur {c}', markersize=10)
                             for c in unique_colors]
            plt.legend(handles=legend_elements, loc='center left', 
                      bbox_to_anchor=(1, 0.5), fontsize=font_size)
        else:
            print(f"\nℹ️ Légende omise car trop de couleurs ({len(unique_colors)})")

    plt.tight_layout()
    plt.show()
    
    # Afficher les statistiques de coloration
    if colors is not None:
        print("\n Statistiques de coloration:")
        print(f"Nombre total de couleurs utilisées: {len(set(colors))}")
        if num_nodes <= 50:  # Limiter l'affichage détaillé pour les grands graphes
            print("\nDétails de la coloration:")
            for node, color in enumerate(colors):
                print(f"Nœud {node + 1}: Couleur {color}")
        else:
            print("\nℹ️ Détails de coloration omis car trop de nœuds")