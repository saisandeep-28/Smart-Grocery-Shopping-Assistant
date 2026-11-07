
# bfs.py

from collections import deque
from supermarket_map import get_neighbors, locations


def bfs(start, selected_sections, checkout):

    # Number of selected sections
    k = len(selected_sections)

    # All sections visited mask
    all_visited = (1 << k) - 1

    # Initial state: (position, visited_mask)
    initial_state = (start, 0)

    # Queue for BFS
    queue = deque([initial_state])

    # Visited states
    visited = {initial_state}

    # Parent dictionary for path reconstruction
    parent = {initial_state: None}

    nodes_explored = 0

    goal_state = None

    # BFS traversal
    while queue:

        current_state = queue.popleft()
        nodes_explored += 1

        position, mask = current_state

        # Check goal condition
        if position == checkout and mask == all_visited:
            goal_state = current_state
            break

        # Explore neighbouring positions
        for neighbor in get_neighbors(position):

            new_mask = mask

            # Check whether neighbor is a selected section
            for i, section in enumerate(selected_sections):

                if neighbor == section:
                    new_mask |= (1 << i)

            new_state = (neighbor, new_mask)

            # Add unexplored state to queue
            if new_state not in visited:

                visited.add(new_state)

                parent[new_state] = current_state

                queue.append(new_state)

    # No valid route found
    if goal_state is None:
        return None, nodes_explored

    # Reconstruct path
    path = []

    current = goal_state

    while current is not None:

        position, mask = current

        path.append(position)

        current = parent[current]

    # Reverse path to get start-to-goal order
    path.reverse()

    return path, nodes_explored


# Test BFS independently
if __name__ == "__main__":

    start = locations["Entrance"]
    checkout = locations["Checkout"]

    selected_sections = [
        locations["Dairy"],
        locations["Grains"],
        locations["Personal Care"]
    ]

    path, explored = bfs(
        start,
        selected_sections,
        checkout
    )

    print("BFS Result")

    if path:
        print("Path:", path)
        print("Path length:", len(path) - 1)
    else:
        print("No valid route found")

    print("Nodes explored:", explored)
