import numpy as np
import matplotlib.pyplot as plt

def scatter_plot():
    x = np.random.randn(100)
    y = np.random.randn(100)

    plt.scatter(x, y)
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

scatter_plot()



# Hill Climbing Function 
def hill_climbing(graph, start, goal, heuristic): 
    current_node = start 
    path = [current_node] 
    total_cost = 0 
 
    while current_node != goal: 
        neighbors = graph[current_node] 
        if not neighbors: 
            print(f"No path from {current_node} to {goal}") 
            return None 
 
        next_node, next_cost = min(neighbors, key=lambda x: heuristic[x[0]]) 
 
        if heuristic[next_node] >= heuristic[current_node]: 
            print("Stuck in local minima, cannot proceed further.") 
            return None 
 
        path.append(next_node) 
        total_cost += next_cost 
        current_node = next_node 
 
    return total_cost, path 
 
# Graph and Heuristic 
graph = { 
    'A': [('B', 11), ('C', 14), ('D', 7)], 
    'B': [('A', 11), ('E', 15)], 
    'C': [('A', 14), ('E', 8), ('D', 18), ('F', 10)], 
    'D': [('A', 7), ('F', 25), ('C', 18)], 
    'E': [('B', 15), ('C', 8), ('H', 9)], 
    'F': [('G', 20), ('C', 10), ('D', 25)], 
    'G': [], 
    'H': [('E', 9), ('G', 10)] 
} 
 
heuristic = { 
    'A': 40, 
    'B': 32, 
    'C': 25, 
    'D': 35, 
    'E': 19, 
    'F': 17, 
    'G': 0, 
    'H': 10 
} 
 
# Run Hill Climbing 
start = 'A' 
goal = 'G' 
result = hill_climbing(graph, start, goal, heuristic) 
 
if result: 
    print(f"Hill Climbing path from {start} to {goal}: {result[1]}") 
    print(f"Total cost: {result[0]}") 
else: 
    print("Goal not reachable with hill climbing.") 