import numpy as np

def sat_degree(adj_matrix, current_solution, node):
    """
    Computes the saturation degree of a node for the DSatur algorithm.

    Parameters:
    - adj_matrix (numpy.ndarray): The adjacency matrix of the graph.
    - current_solution (numpy.ndarray): A NumPy array where the index represents a node and 
      the value is its assigned color (-1 if uncolored).
    - node (int): The node for which we want to calculate the saturation degree.

    Returns:
    - int: The saturation degree of the node.
    """
    # Get the neighbors of the node (indices where adj_matrix[node] == 1)
    neighbors = np.where(adj_matrix[node] == 1)[0]
    
    # Extract the colors of neighboring nodes
    neighbor_colors = current_solution[neighbors]
    
    # Get unique colors excluding uncolored nodes (-1)
    unique_colors = np.unique(neighbor_colors[neighbor_colors != -1])
    
    return len(unique_colors)
