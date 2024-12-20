import numpy as np

# Define integer codes for directions and symbols
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
OBSTACLE = 4
EMPTY = 5
PREVIOUS_POSITION = 6

# Map from characters to integers
char_to_int = {
  '^': UP,
  'v': DOWN,
  '<': LEFT,
  '>': RIGHT,
  '#': OBSTACLE,
  '.': EMPTY,
  'X': PREVIOUS_POSITION
}


def cycle_direction(current_direction):
  return (current_direction + 1) % 4


def move_forward(current_ij, current_direction):
  i, j = current_ij
  if current_direction == UP:
    return (i - 1, j)
  if current_direction == DOWN:
    return (i + 1, j)
  if current_direction == LEFT:
    return (i, j - 1)
  if current_direction == RIGHT:
    return (i, j + 1)


def position_obstructed(X, n, m, ij):
  i, j = ij
  return 0 <= i < n and 0 <= j < m and X[i, j] == OBSTACLE


def get_next_position_and_direction(X, n, m, current_ij, current_direction):
  candidate_next_direction = current_direction
  candidate_next_position = move_forward(current_ij, current_direction)
  while position_obstructed(X, n, m, candidate_next_position):
    candidate_next_direction = cycle_direction(candidate_next_direction)
    candidate_next_position = move_forward(current_ij, candidate_next_direction)
  return candidate_next_position, candidate_next_direction


def forward_trace(X, n, m, current_ij, current_direction):
  i, j = current_ij
  direction = current_direction
  trace_ijs = []
  trace_ijs_directions = []
  while 0 <= i < n and 0 <= j < m:
    trace_ijs.append((i, j))
    trace_ijs_directions.append((i, j, direction))
    next_ij, next_direction = get_next_position_and_direction(X, n, m, (i, j),
                                                              direction)
    i, j = next_ij
    direction = next_direction
  return trace_ijs, trace_ijs_directions


def forward_trace_identify_loop(X, n, m, current_ij, current_direction):
  i, j = current_ij
  direction = current_direction
  loop_identified = False
  # trace_ijs_directions = []
  trace_ijs_directions_set = set()
  while 0 <= i < n and 0 <= j < m:
    next_ij, next_direction = get_next_position_and_direction(X, n, m, (i, j),
                                                              direction)
    i, j = next_ij
    direction = next_direction
    if (i, j, direction) in trace_ijs_directions_set:
    # if (i, j, direction) in trace_ijs_directions:
      # print('loop identified:', i, j, direction)
      loop_identified = True
      break
    trace_ijs_directions_set.add((i, j, direction))
    # trace_ijs_directions.append((i, j, direction))
  return loop_identified


def duplicate(X, n, m):
  return X.copy()


def find_looping_obstacles(X, n, m, starting_ij, starting_direction):
  trace_ijs, _ = forward_trace(X, n, m, starting_ij, starting_direction)
  candidates = trace_ijs
  # filter out repeated positions
  candidates = list(set(candidates))
  # filter out any candidate that overlaps with the starting position
  candidates = [candidate for candidate in candidates if candidate != starting_ij]
  obstacle_positions = []
  print('number of candidates:', len(candidates))
  # print(n, m)
  for index, (i, j) in enumerate(candidates):
    if index % 50 == 0:
      print('checking:', index, i, j)
    Y = duplicate(X, n, m)
    Y[i, j] = OBSTACLE
    if forward_trace_identify_loop(Y, n, m, starting_ij, starting_direction):
      obstacle_positions.append((i, j))
  return obstacle_positions


def main():
  input_path = '/home/pxd256/Workspace/aoc2024/pythonProject/day_06/input'
  with open(input_path, 'r') as f:
    lines = f.readlines()

  # Strip and join lines to form a continuous grid
  m = len(lines[0].strip())
  joined = ''.join([line.strip() for line in lines])
  n = len(joined) // m

  # Create a NumPy array from the joined characters
  X = np.zeros((n, m), dtype=int)
  for i in range(n):
    for j in range(m):
      ch = joined[i * m + j]
      X[i, j] = char_to_int[ch]

  # Find the starting position and direction
  starting_ij = (0, 0)
  starting_direction = DOWN
  for i in range(n):
    for j in range(m):
      if X[i, j] in [UP, DOWN, LEFT, RIGHT]:
        starting_ij = (i, j)
        starting_direction = X[i, j]
        break

  # Part 1
  trace_ijs, _ = forward_trace(X, n, m, starting_ij, starting_direction)
  Y = duplicate(X, n, m)
  for i, j in trace_ijs:
    Y[i, j] = PREVIOUS_POSITION

  count = np.sum(Y == PREVIOUS_POSITION)
  # print(count)

  # Part 2
  obstacle_positions = find_looping_obstacles(X, n, m, starting_ij,
                                              starting_direction)
  print(len(obstacle_positions))
  print(obstacle_positions) # should contain: (6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7) in test data


if __name__ == '__main__':
  main()
