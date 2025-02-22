import numpy as np
from get_graph_from_file import get_graph_from_file
from represent_graph import represent_graph
from branch_and_bound import branch_and_bound_coloration as branch_and_bound
from display_solution import display_solution

def main():
    """
    Main function that integrates all the modules:
    - Reads a graph from a file
    - Represents the graph
    - Runs the branch and bound algorithm
    - Displays the solution
    """
    # Load the adjacency matrix from the file
    adj_matrix = get_graph_from_file()
    if adj_matrix is None:
        print("Failed to load the graph. Exiting...")
        return

    # Represent the initial graph
    represent_graph(adj_matrix)

    # Run the branch and bound algorithm
    solution, chromatic_number, execution_time = branch_and_bound(adj_matrix)

    # Display the solution
    display_solution(solution, chromatic_number)

    # Represent the graph with its coloring
    represent_graph(adj_matrix, solution)

    print(f"\nExecution Time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    main()
