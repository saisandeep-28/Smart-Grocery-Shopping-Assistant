
import heapq
from math import inf
from supermarket_map import get_neighbors, locations


def heuristic(position, mask, selected_sections, checkout):

    targets = []

    # Collect all sections that are not yet visited
    for i, section in enumerate(selected_sections):
        if not (mask & (1 << i)):
            targets.append(section)

    # Checkout is always a required destination
    targets.append(checkout)

    # Maximum Manhattan distance to any remaining destination
    return max(
        abs(position[0] - target[0]) +
        abs(position[1] - target[1])
        for target in targets
    )


def astar(start, selected_sections, checkout):

    k = len(selected_sections)
    all_visited = (1 << k) - 1

    initial_state = (start, 0)

    # Priority queue stores (f, g, state)
    priority_queue = []

    initial_h = heuristic(
        start, 0, selected_sections, checkout
    )

    heapq.heappush(
        priority_queue,
        (initial_h, 0, initial_state)
    )

    g_score = {initial_state: 0}
    parent = {initial_state: None}

    nodes_explored = 0
    goal_state = None

    while priority_queue:

        f, current_g, current_state = heapq.heappop(
            priority_queue
        )

        # Ignore outdated entries
        if current_g != g_score.get(current_state):
            continue

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

            tentative_g = current_g + 1

            if tentative_g < g_score.get(new_state, inf):

                g_score[new_state] = tentative_g
                parent[new_state] = current_state

                h = heuristic(
                    neighbor,
                    new_mask,
                    selected_sections,
                    checkout
                )

                new_f = tentative_g + h

                heapq.heappush(
                    priority_queue,
                    (new_f, tentative_g, new_state)
                )

    if goal_state is None:
        return None, nodes_explored

    # Reconstruct the path
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

    path, explored = astar(
        start, selected_sections, checkout
    )

    print("A* Search Result")

    if path:
        print("Path:", path)
        print("Path length:", len(path) - 1)
    else:
        print("No valid route found")

    print("Nodes explored:", explored)
