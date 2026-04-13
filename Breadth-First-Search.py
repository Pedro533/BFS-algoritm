# Linear Puzzle using Breadth-First Search (BFS)
from tree import Node


def bfs_solution(initial_state, goal_state):
    solved = False
    visited_nodes = []
    frontier_nodes = []

    initial_node = Node(initial_state)
    frontier_nodes.append(initial_node)

    while (not solved) and len(frontier_nodes) != 0:
        node = frontier_nodes.pop(0)

        # Remove node from frontier and add to visited
        visited_nodes.append(node)

        if node.get_data() == goal_state:
            # Solution found
            solved = True
            return node
        else:
            # Expand child nodes
            node_data = node.get_data()

            # Left operator
            child = [node_data[1], node_data[0], node_data[2], node_data[3]]
            left_child = Node(child)
            if not left_child.in_list(visited_nodes) and not left_child.in_list(frontier_nodes):
                frontier_nodes.append(left_child)

            # Middle operator
            child = [node_data[0], node_data[2], node_data[1], node_data[3]]
            middle_child = Node(child)
            if not middle_child.in_list(visited_nodes) and not middle_child.in_list(frontier_nodes):
                frontier_nodes.append(middle_child)

            # Right operator
            child = [node_data[0], node_data[1], node_data[3], node_data[2]]
            right_child = Node(child)
            if not right_child.in_list(visited_nodes) and not right_child.in_list(frontier_nodes):
                frontier_nodes.append(right_child)

            node.set_children([left_child, middle_child, right_child])

    return None


if __name__ == "__main__":
    initial_state = [4, 2, 3, 1]
    goal_state = [1, 2, 3, 4]

    solution_node = bfs_solution(initial_state, goal_state)

    # Show result
    result = []

    if solution_node is not None:
        node = solution_node

        while node.get_parent() is not None:
            result.append(node.get_data())
            node = node.get_parent()

        result.append(initial_state)
        result.reverse()
        print(result)
    else:
        print("No solution found.")
