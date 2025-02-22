import numpy as np

def get_graph_from_file():

    """
    Asks the user for a file, extracts the graph, and returns an adjacency matrix.
    """

    # Ask user for the file name
    file_name = input("Enter the graph file name: ")
    
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        
        num_vertices = 0
        adj_matrix = None
        problem_set = False  # Ensures we process the problem line before edges
        
        # Read the file line by line
        for line in lines:
            parts = line.strip().split()
            
            # Ignore comment lines
            if not parts or parts[0] == "c":
                continue
            
            # Read the number of vertices
            if parts[0] == "p" and parts[1] == "edge":
                num_vertices = int(parts[2])
                # Initialize adjacency matrix with zeros (0-based index)
                adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
                problem_set = True
            
            # Read edges and populate the adjacency matrix
            elif parts[0] == "e":
                if not problem_set:
                    raise RuntimeError("Error: Edge descriptor found before problem line")
                v1, v2 = int(parts[1]) - 1, int(parts[2]) - 1  # Convert to 0-based index
                adj_matrix[v1][v2] = 1
                adj_matrix[v2][v1] = 1  # Since the graph is undirected
        
        return adj_matrix
    
    except FileNotFoundError:
        print("Error: File not found!")
        return None
    except RuntimeError as e:
        print(e)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None