
# supermarket_map.py

ROWS = 8
COLS = 8

# 0 = Walkable cell
# 1 = Obstacle

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Positions of obstacles
obstacles = {
    (1, 1), (1, 4), (1, 6),
    (3, 2),
    (4, 1), (4, 4),
    (6, 2)
}

# Mark obstacles in the grid
for row, col in obstacles:
    grid[row][col] = 1

# Supermarket locations
locations = {
    "Entrance": (0, 0),
    "Dairy": (0, 3),
    "Bakery": (2, 0),
    "Grains": (2, 5),
    "Fruits": (5, 0),
    "Personal Care": (5, 6),
    "Checkout": (7, 7)
}


# Find all valid neighbouring cells
def get_neighbors(position):

    row, col = position

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbors = []

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if (0 <= new_row < ROWS and
            0 <= new_col < COLS and
            grid[new_row][new_col] == 0):

            neighbors.append((new_row, new_col))

    return neighbors


# Display the supermarket map
def display_map(path=None):

    visual = [["." for _ in range(COLS)]
              for _ in range(ROWS)]

    # Display obstacles
    for row, col in obstacles:
        visual[row][col] = "X"

    # Display important locations
    symbols = {
        "Entrance": "S",
        "Dairy": "D",
        "Bakery": "B",
        "Grains": "G",
        "Fruits": "F",
        "Personal Care": "P",
        "Checkout": "C"
    }

    for name, position in locations.items():
        row, col = position
        visual[row][col] = symbols[name]

    # Display calculated path
    if path:
        for row, col in path:
            if visual[row][col] == ".":
                visual[row][col] = "*"

    for row in visual:
        print(" ".join(row))


# Test the map
if __name__ == "__main__":

    print("SMART GROCERY SHOPPING ASSISTANT")
    print("--------------------------------")

    display_map()

    print("\nNeighbours of Entrance:")
    print(get_neighbors(locations["Entrance"]))
