
from supermarket_map import get_neighbors, locations


def dfs(start, selected_sections, checkout):

    k = len(selected_sections)
    all_visited = (1 << k) - 1

    initial_state = (start, 0)

    stack = [initial_state]
    visited = {initial_state}
    parent = {initial_state: None}

    nodes_explored = 0
    goal_state = None

    while stack:

        current_state = stack.pop()
        nodes_explored += 1

        position, mask = current_state

        if position == checkout and mask == all_visited:
            goal_state = current_state
            break

        for neighbor in get_neighbors(position):

            new_mask = mask

            for i, section in enumerate(selected_sections):
                if neighbor == section:
                    new_mask |= (1 << i)

            new_state = (neighbor, new_mask)

            if new_state not in visited:

                visited.add(new_state)
                parent[new_state] = current_state
                stack.append(new_state)

    if goal_state is None:
        return None, nodes_explored

    path = []
    current = goal_state

    while current is not None:
        position, mask = current
        path.append(position)
        current = parent[current]

    path.reverse()

    return path, nodes_explored


if __name__ == "__main__":

    start = locations["Entrance"]
    checkout = locations["Checkout"]

    selected_sections = [
        locations["Dairy"],
        locations["Grains"],
        locations["Personal Care"]
    ]

    path, explored = dfs(start, selected_sections, checkout)

    print("DFS Result")

    if path:
        print("Path:", path)
        print("Path length:", len(path) - 1)
    else:
        print("No valid route found")

    print("Nodes explored:", explored)
