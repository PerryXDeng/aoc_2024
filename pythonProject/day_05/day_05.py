def main():
  input_path = '/home/pxd256/Workspace/aoc2024/pythonProject/day_05/input'
  with open(input_path, 'r') as f:
    lines = f.readlines()
  # part 1
  inequalities = {} # key: LHS, value: list of RHS
  ordered_sequences = []
  for line in lines:
    # lines containing "|" are inequalities
    # lines containing "," are ordered sequences
    if "|" in line:
      lhs, rhs = line.strip().split("|")
      if lhs not in inequalities:
        inequalities[lhs] = []
      inequalities[lhs].append(rhs)
    else:
      if "," in line:
        ordered_sequences.append(line.strip().split(","))
  verified_sequences = []
  incorrect_sequences = []
  for sequence in ordered_sequences:
    verified = True
    for i in range(len(sequence)):
      for j in range(len(sequence)):
        x = sequence[i]
        y = sequence[j]
        if x in inequalities and y in inequalities[x] and i > j:
          verified = False
          break
    if verified:
      verified_sequences.append(sequence)
    else:
      incorrect_sequences.append(sequence)
  sum = 0
  for sequence in verified_sequences:
    middle = int(sequence[len(sequence) // 2])
    sum += middle
  print(sum)
  # part 2
  for sequence in incorrect_sequences:
    fixed = False
    while not fixed:
      error_discovered = False
      for i in range(len(sequence)):
        for j in range(len(sequence)):
          x = sequence[i]
          y = sequence[j]
          if x in inequalities and y in inequalities[x] and i > j:
            sequence[i], sequence[j] = sequence[j], sequence[i]
            error_discovered = True
      if not error_discovered:
        fixed = True
  sum = 0
  for sequence in incorrect_sequences:
    middle = int(sequence[len(sequence) // 2])
    sum += middle
  print(sum)



if __name__ == '__main__':
  main()