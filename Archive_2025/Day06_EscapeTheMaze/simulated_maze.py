# Day 6 - Simulated Maze in pure Python
# This is a simple text-based version of the Reeborg maze
# so you can run the algorithm locally in PyCharm.

import time

# Maze legend:
# "S" = start
# "G" = goal
# "#" = wall
# " " = open space
maze_map = [
    "###########",
    "#S   #   G#",
    "# # # # # #",
    "# #   #   #",
    "# ### ### #",
    "#         #",
    "###########",
]

ROWS = len(maze_map)
COLS = len(maze_map[0])

# Find start and goal positions
start_pos = None
goal_pos = None
for r in range(ROWS):
    for c in range(COLS):
        if maze_map[r][c] == "S":
            start_pos = (r, c)
        elif maze_map[r][c] == "G":
            goal_pos = (r, c)

# Directions: up, right, down, left
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_index = 1  # start facing right

row, col = start_pos


def is_wall(r, c):
    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return True
    return maze_map[r][c] == "#"


def at_goal():
    return (row, col) == goal_pos


def turn_left():
    global dir_index
    dir_index = (dir_index - 1) % 4


def turn_right():
    # three left turns = right turn
    for _ in range(3):
        turn_left()


def front_is_clear():
    dr, dc = DIRS[dir_index]
    nr, nc = row + dr, col + dc
    return not is_wall(nr, nc)


def right_is_clear():
    # look at the direction you'd face if you turned right
    right_dir = (dir_index + 1) % 4
    dr, dc = DIRS[right_dir]
    nr, nc = row + dr, col + dc
    return not is_wall(nr, nc)


def move():
    global row, col
    if front_is_clear():
        dr, dc = DIRS[dir_index]
        row += dr
        col += dc
    else:
        raise RuntimeError("Tried to move into a wall!")


def print_maze():
    """Print the maze with the robot's current position."""
    for r in range(ROWS):
        line = ""
        for c in range(COLS):
            if (r, c) == (row, col):
                line += "R"  # robot
            else:
                line += maze_map[r][c]
        print(line)
    print()
    time.sleep(0.1)


# --- Maze-solving algorithm (same logic as Reeborg) ---

steps = 0
while not at_goal() and steps < 1000:
    print_maze()

    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

    steps += 1

print_maze()
if at_goal():
    print("🎉 Reached the goal!")
else:
    print("⚠️ Gave up after too many steps.")