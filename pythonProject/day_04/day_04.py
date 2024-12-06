def count_XMAS(X, n, m):
  # count the number of valid string "XMAS" in the matrix X
  # the string can be horizontal, vertical or diagonal
  # the string must be contiguous
  # the string can be reversed
  count = 0
  # horizontal
  for i in range(n):
    for j in range(m-3):
      if X[i][j] == 'X' and X[i][j+1] == 'M' and X[i][j+2] == 'A' and X[i][j+3] == 'S':
        count += 1
  # horizontal reversed
  for i in range(n):
    for j in range(m-3):
      if X[i][j] == 'S' and X[i][j+1] == 'A' and X[i][j+2] == 'M' and X[i][j+3] == 'X':
        count += 1
  # vertical
  for i in range(n-3):
    for j in range(m):
      if X[i][j] == 'X' and X[i+1][j] == 'M' and X[i+2][j] == 'A' and X[i+3][j] == 'S':
        count += 1
  # vertical reversed
  for i in range(n-3):
    for j in range(m):
      if X[i][j] == 'S' and X[i+1][j] == 'A' and X[i+2][j] == 'M' and X[i+3][j] == 'X':
        count += 1
  # first diagonal
  for i in range(n-3):
    for j in range(m-3):
      if X[i][j] == 'X' and X[i+1][j+1] == 'M' and X[i+2][j+2] == 'A' and X[i+3][j+3] == 'S':
        count += 1
  # first diagonal reversed
  for i in range(n-3):
    for j in range(m-3):
      if X[i][j] == 'S' and X[i+1][j+1] == 'A' and X[i+2][j+2] == 'M' and X[i+3][j+3] == 'X':
        count += 1
  # second diagonal
  for i in range(n-3):
    for j in range(3, m):
      if X[i][j] == 'X' and X[i+1][j-1] == 'M' and X[i+2][j-2] == 'A' and X[i+3][j-3] == 'S':
        count += 1
  # second diagonal reversed
  for i in range(n-3):
    for j in range(3, m):
      if X[i][j] == 'S' and X[i+1][j-1] == 'A' and X[i+2][j-2] == 'M' and X[i+3][j-3] == 'X':
        count += 1
  return count


def part_1(X, n, m):
  print(count_XMAS(X, n, m))


def verify_X_MAS(X, n, m, A_i, A_j):
  # verify the string "MAS" appears in the two diagonals centered at A_i, A_j
  # the string can be reversed
  first_diagonal = []
  second_diagonal = []
  if A_i - 1 >= 0 and A_j - 1 >= 0:
    first_diagonal.append(X[A_i-1][A_j-1])
  first_diagonal.append(X[A_i][A_j])
  if A_i + 1 < n and A_j + 1 < m:
    first_diagonal.append(X[A_i+1][A_j+1])
  if A_i - 1 >= 0 and A_j + 1 < m:
    second_diagonal.append(X[A_i-1][A_j+1])
  second_diagonal.append(X[A_i][A_j])
  if A_i + 1 < n and A_j - 1 >= 0:
    second_diagonal.append(X[A_i+1][A_j-1])
  return ((first_diagonal == ['M', 'A', 'S'] or first_diagonal == ['S', 'A', 'M'])
          and (second_diagonal == ['M', 'A', 'S'] or second_diagonal == ['S', 'A', 'M']))


def count_X_MAS(X, n, m):
  count = 0
  for i in range(n):
    for j in range(m):
      if X[i][j] == 'A':
        count += verify_X_MAS(X, n, m, i, j)
  return count


def part_2(X, n, m):
  print(count_X_MAS(X, n, m))


def main():
  input_path = '/home/pxd256/Workspace/aoc2024/pythonProject/day_04/input'
  # input is a matrix of characters of size n x m
  # parse the input into a list of lists of strings
  with open(input_path, 'r') as f:
    lines = f.readlines()
  X = []
  m = len(lines[0].strip())
  # join the lines into a single string, remove whitespaces
  joined = ''.join([line.strip() for line in lines])
  n = len(joined) // m
  for i in range(0, n*m, m):
    X.append(list(joined[i:i+m]))
  part_1(X, n, m)
  part_2(X, n, m)


if __name__ == '__main__':
  main()
