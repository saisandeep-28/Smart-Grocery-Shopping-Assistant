# 🛒 Smart Grocery Shopping Assistant Using AI Search Algorithms

A Python-based AI project that helps shoppers navigate a supermarket efficiently by finding routes to selected product sections and finally reaching the checkout.

The project demonstrates four classical AI search algorithms: **Breadth-First Search (BFS), Depth-First Search (DFS), Greedy Best-First Search, and A* Search.**

## 📌 Project Overview

Navigating a supermarket to collect multiple products can take time, especially when products are located in different sections.

The Smart Grocery Shopping Assistant models a supermarket as a 2D grid. Based on the user's shopping list, it identifies the required sections and applies AI search algorithms to find a route from the entrance, through the selected sections, to the checkout.

## 🎯 Objectives

- Represent a supermarket using a grid-based environment.
- Map grocery products to their respective supermarket sections.
- Implement different AI search algorithms in Python.
- Compare algorithms based on path length, nodes explored, and execution time.
- Visualize the supermarket layout and generated routes.

## 🧠 Algorithms Implemented

| Algorithm | Description |
|---|---|
| BFS | Explores nodes level by level using a FIFO queue. |
| DFS | Explores deeper paths first using a LIFO stack. |
| Greedy Best-First Search | Selects nodes based on a heuristic estimate. |
| A* Search | Uses actual path cost and heuristic cost to guide the search. |

### A* Evaluation Function

A* uses:

`f(n) = g(n) + h(n)`

- `g(n)`: Actual cost from the starting state.
- `h(n)`: Estimated remaining cost to reach the goal.
- `f(n)`: Estimated total path cost.

## 🏬 Supermarket Environment

The supermarket is represented as an **8 × 8 grid**.

- Entrance: `(0, 0)`
- Checkout: `(7, 7)`
- Movement: Up, Down, Left, Right
- Obstacles: Represent shelves or blocked locations.
- Product sections: Dairy, Bakery, Grains, Fruits, and Personal Care.

### Product Mapping

| Products | Section |
|---|---|
| Milk, Cheese, Butter | Dairy |
| Bread, Cake, Biscuits | Bakery |
| Rice, Wheat, Pasta | Grains |
| Apple, Banana, Orange | Fruits |
| Soap, Shampoo, Toothpaste | Personal Care |

## ⚙️ Technologies Used

- Python
- Matplotlib
- AI Search Algorithms
- Data Structures: Queues, Stacks, Priority Queues, and Sets

## 📂 Project Structure

```text
Smart-Grocery-Shopping-Assistant/
│
├── main.py
├── bfs.py
├── dfs.py
├── greedy_best_first.py
├── astar.py
├── supermarket_map.py
├── product_mapping.py
├── README.md
└── .gitignore
```

## 🚀 Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/saisandeep-28/Smart-Grocery-Shopping-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd Smart-Grocery-Shopping-Assistant
```

### 3. Install the required library

```bash
pip install matplotlib
```

### 4. Run the application

```bash
python main.py
```

### 5. Enter your shopping list

Example:

```text
milk, rice, soap, bread
```

The application maps the products to supermarket sections and runs the implemented search algorithms.

## 📊 Performance Analysis

The algorithms are evaluated using:

- **Path Length:** Number of movements in the generated route.
- **Nodes Explored:** Number of states explored during the search.
- **Execution Time:** Time taken by the algorithm to find a route.

### Sample Experimental Results

**Test Case 1:** Milk, Rice, Soap

| Algorithm | Path Length | Nodes Explored |
|---|---:|---:|
| BFS | 14 | 278 |
| DFS | 20 | 65 |
| Greedy Best-First | 14 | 126 |
| A* | 14 | 66 |

**Test Case 2:** Bread, Apple, Shampoo, Wheat

| Algorithm | Path Length | Nodes Explored |
|---|---:|---:|
| BFS | 20 | 723 |
| DFS | 88 | 90 |
| Greedy Best-First | 24 | 473 |
| A* | 20 | 270 |

*Results are from the project's tested configurations. Execution time may vary depending on the system.*

## 🔮 Future Enhancements

- Add a graphical user interface.
- Support dynamic supermarket layouts.
- Include product prices and shopping cart management.
- Optimize routes for larger supermarkets.
- Add real-time product availability.

## 👥 Team Members

- Sai Sandeep — CS25B1020
- Siddhu — CS25B2004
- Vamsi Nayak — CS25B1017
- Parthiv — CS25B2033

## 🎓 Academic Information

**Course:** Introduction to AI with Python  
**Academic Year:** 2026–2027

---

⭐ If you find this project interesting, feel free to explore the code and its implementations of classical AI search algorithms.