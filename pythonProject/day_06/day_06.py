_CURRENT_POSITION_FACING_UP = '^'
_CURRENT_POSITION_FACING_DOWN = 'v'
_CURRENT_POSITION_FACING_LEFT = '<'
_CURRENT_POSITION_FACING_RIGHT = '>'
_OBSTACLE = '#'
_EMPTY = '.'
_PREVIOUS_POSITION = 'X'


def cycle_direction(current_direction):
  if current_direction == _CURRENT_POSITION_FACING_UP:
    return _CURRENT_POSITION_FACING_RIGHT
  if current_direction == _CURRENT_POSITION_FACING_RIGHT:
    return _CURRENT_POSITION_FACING_DOWN
  if current_direction == _CURRENT_POSITION_FACING_DOWN:
    return _CURRENT_POSITION_FACING_LEFT
  if current_direction == _CURRENT_POSITION_FACING_LEFT:
    return _CURRENT_POSITION_FACING_UP


def move_forward(current_ij, current_direction):
  i, j = current_ij
  if current_direction == _CURRENT_POSITION_FACING_UP:
    return (i-1, j)
  if current_direction == _CURRENT_POSITION_FACING_DOWN:
    return (i+1, j)
  if current_direction == _CURRENT_POSITION_FACING_LEFT:
    return (i, j-1)
  if current_direction == _CURRENT_POSITION_FACING_RIGHT:
    return (i, j+1)


def position_obstructed(X, n, m, ij):
  i, j = ij
  return 0 <= i < n and 0 <= j < m and X[i][j] == _OBSTACLE


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
  while 0 <= i < n and 0 <= j < m:
    trace_ijs.append((i, j))
    next_ij, next_direction = get_next_position_and_direction(X, n, m, (i, j), direction)
    i, j = next_ij
    direction = next_direction
  return trace_ijs


def forward_trace_identify_loop(X, n, m, current_ij, current_direction):
  i, j = current_ij
  direction = current_direction
  trace_ijs_directions = []
  loop_identified = False
  while 0 <= i < n and 0 <= j < m:
    if (i, j, direction) in trace_ijs_directions:
      loop_identified = True
      break
    trace_ijs_directions.append((i, j, direction))
    next_ij, next_direction = get_next_position_and_direction(X, n, m, (i, j), direction)
    i, j = next_ij
    direction = next_direction
  # if loop_identified:
  #   Y = duplicate(X, n, m)
  #   for i, j, direction in trace_ijs_directions:
  #     Y[i][j] = '|' if direction == _CURRENT_POSITION_FACING_UP or direction == _CURRENT_POSITION_FACING_DOWN else '-'
  #   for i in range(n):
  #     for j in range(m):
  #       print(Y[i][j], end='')
  #     print()
  #   print()
  return loop_identified


def duplicate(X, n, m):
  Y = []
  for i in range(n):
    Y.append([X[i][j] for j in range(m)])
  return Y


def find_looping_obstacles(X, n, m, starting_ij, starting_direction):
  trace_ijs = forward_trace(X, n, m, starting_ij, starting_direction)
  candidates = trace_ijs[1:]
  obstacle_positions = []
  print('number of candidates:', len(candidates))
  print(n, m)
  for index, (i, j) in enumerate(candidates):
    if index % 50 == 0:
      print('checking:', index, i, j)
    if (i, j) not in obstacle_positions:
      X[i][j] = _OBSTACLE
      if forward_trace_identify_loop(X, n, m, starting_ij, starting_direction):
        obstacle_positions.append((i, j))
      X[i][j] = _EMPTY
  return obstacle_positions


def main():
  input_path = '/home/pxd256/Workspace/aoc2024/pythonProject/day_06/input_test'
  with open(input_path, 'r') as f:
    lines = f.readlines()
  X = []
  m = len(lines[0].strip())
  # join the lines into a single string, remove whitespaces
  joined = ''.join([line.strip() for line in lines])
  n = len(joined) // m
  for i in range(0, n*m, m):
    X.append(list(joined[i:i+m]))
  # part 1
  starting_ij = (0, 0)
  starting_direction = _CURRENT_POSITION_FACING_DOWN
  for i in range(n):
    for j in range(m):
      if X[i][j] == _CURRENT_POSITION_FACING_UP:
        starting_ij = (i, j)
        starting_direction = _CURRENT_POSITION_FACING_UP
      if X[i][j] == _CURRENT_POSITION_FACING_DOWN:
        starting_ij = (i, j)
        starting_direction = _CURRENT_POSITION_FACING_DOWN
      if X[i][j] == _CURRENT_POSITION_FACING_LEFT:
        starting_ij = (i, j)
        starting_direction = _CURRENT_POSITION_FACING_LEFT
      if X[i][j] == _CURRENT_POSITION_FACING_RIGHT:
        starting_ij = (i, j)
        starting_direction = _CURRENT_POSITION_FACING_RIGHT
  trace_ijs = forward_trace(X, n, m, starting_ij, starting_direction)
  Y = duplicate(X, n, m)
  for i, j in trace_ijs:
    Y[i][j] = _PREVIOUS_POSITION
  count = 0
  for i in range(n):
    for j in range(m):
      if Y[i][j] == _PREVIOUS_POSITION:
        count += 1
  print(count)
  # part 2
  obstacle_positions = find_looping_obstacles(X, n, m, starting_ij, starting_direction)
  print(len(obstacle_positions))



if __name__ == '__main__':
  main()

