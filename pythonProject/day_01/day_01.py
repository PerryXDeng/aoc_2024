def sorted_vec_distance(list1, list2):
  list1.sort()
  list2.sort()
  distances = [abs(x - y) for x, y in zip(list1, list2)]
  return sum(distances)

def similarity_score_naive(list1, list2):
  score = 0
  for x in list1:
    for y in list2:
      if x == y:
        score += x
  return score

def main():
  input_path = '/home/pxd256/Workspace/aoc2024/pythonProject/day_01/input'
  with open(input_path, 'r') as f:
    lines = f.readlines()
  list1 = []
  list2 = []
  for line in lines:
    x_y = line.split()
    x = int(x_y[0])
    y = int(x_y[1])
    list1.append(x)
    list2.append(y)
  dist = sorted_vec_distance(list1, list2)
  print(dist)
  score = similarity_score_naive(list1, list2)
  print(score)

if __name__ == '__main__':
  main()
