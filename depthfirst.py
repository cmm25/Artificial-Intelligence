def dfs_jug_problem(x, y, target_x=2, target_y=0, path=None):
    if path is None:
        path = []

    # Base case: If we reach the target state, return the path
    if (x, y) == (target_x, target_y):
        return path

    # Try all possible moves
    for move in ["fill_x", "fill_y", "empty_x", "empty_y", "pour_x_to_y", "pour_y_to_x"]:
        new_x, new_y = apply_move(x, y, move)
        if (new_x, new_y) not in path:
            new_path = dfs_jug_problem(new_x, new_y, target_x, target_y, path + [(new_x, new_y)])
            if new_path:
                return new_path

    return None

def apply_move(x, y, move):
    if move == "fill_x":
        return 3, y
    elif move == "fill_y":
        return x, 5
    elif move == "empty_x":
        return 0, y
    elif move == "empty_y":
        return x, 0
    elif move == "pour_x_to_y":
        transfer = min(x, 5 - y)
        return x - transfer, y + transfer
    elif move == "pour_y_to_x":
        transfer = min(y, 3 - x)
        return x + transfer, y - transfer

# Find the path from (0, 0) to (2, 0) or (0, 2)
dfs_path = dfs_jug_problem(0, 0)
if dfs_path:
    print("DFS Path:", dfs_path)
else:
    print("No solution found using DFS.")
