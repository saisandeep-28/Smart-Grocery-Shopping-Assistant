
import time
import matplotlib.pyplot as plt

from supermarket_map import locations, display_map
from product_mapping import get_shopping_sections

from bfs import bfs
from dfs import dfs
from greedy_best_first import greedy_best_first
from astar import astar


def main():

    print("=" * 55)
    print("       SMART GROCERY SHOPPING ASSISTANT")
    print("=" * 55)

    # Display supermarket map
    display_map()

    # Get shopping list
    shopping_input = input(
        "\nEnter products separated by commas: "
    )

    shopping_list = shopping_input.split(",")

    # Convert products into supermarket sections
    selected_sections = get_shopping_sections(shopping_list)

    # Validate shopping list
    if not selected_sections:
        print("Please enter a valid shopping list.")
        return

    start = locations["Entrance"]
    checkout = locations["Checkout"]

    print("\nSelected sections:", selected_sections)

    # Algorithms to compare
    algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("Greedy Best First", greedy_best_first),
        ("A*", astar)
    ]

    results = []

    print("\nRunning search algorithms...")

    for name, algorithm in algorithms:

        start_time = time.perf_counter()

        path, explored = algorithm(
            start, selected_sections, checkout
        )

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        if path:
            path_length = len(path) - 1
        else:
            path_length = None

        results.append({
            "name": name,
            "path": path,
            "path_length": path_length,
            "explored": explored,
            "time": execution_time
        })

    # Display individual results
    print("\n" + "=" * 55)
    print("                 SEARCH RESULTS")
    print("=" * 55)

    for result in results:

        print(f"\n{result['name']}")

        if result["path"]:
            print("Path:", result["path"])
            print("Path length:", result["path_length"])
        else:
            print("No valid route found.")

        print("Nodes explored:", result["explored"])
        print(f"Execution time: {result['time']:.8f} seconds")

    # Display comparison table
    print("\n" + "=" * 75)
    print("                  PERFORMANCE COMPARISON")
    print("=" * 75)

    # Prepare data for graphs
    algorithm_names = [result["name"] for result in results]
        
    path_lengths = [
        result["path_length"] for result in results
        ]
    
    nodes_explored = [
        result["explored"] for result in results
        ]
    
    execution_times = [
        result["time"] for result in results
    ]
    
        # Graph 1: Path Length
    plt.figure()
    plt.bar(algorithm_names, path_lengths)
    plt.title("Path Length Comparison")
    plt.xlabel("Search Algorithm")
    plt.ylabel("Path Length")
    plt.show()
    
        # Graph 2: Nodes Explored
    plt.figure()
    plt.bar(algorithm_names, nodes_explored)
    plt.title("Nodes Explored Comparison")
    plt.xlabel("Search Algorithm")
    plt.ylabel("Nodes Explored")
    plt.show()
    
    # Graph 3: Execution Time
    plt.figure()
    plt.bar(algorithm_names, execution_times)
    plt.title("Execution Time Comparison")
    plt.xlabel("Search Algorithm")
    plt.ylabel("Time (seconds)")
    plt.show()

    print(
        f"{'Algorithm':<22}"
        f"{'Path Length':<15}"
        f"{'Nodes Explored':<18}"
        f"{'Time (seconds)':<18}"
    )

    print("-" * 75)

    for result in results:

        path_length = (
            str(result["path_length"])
            if result["path_length"] is not None
            else "N/A"
        )

        print(
            f"{result['name']:<22}"
            f"{path_length:<15}"
            f"{result['explored']:<18}"
            f"{result['time']:<18.8f}"
        )

    print("=" * 75)


    # Display the A* route on the supermarket map
    print("\n" + "=" * 55)
    print("              OPTIMAL SHOPPING ROUTE")
    print("=" * 55)

    astar_result = results[3]

    if astar_result["path"]:
        print("Displaying A* route:")
        display_map(astar_result["path"])
    else:
        print("No route available to display.")

if __name__ == "__main__":
    main()
