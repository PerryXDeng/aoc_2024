import re

def part_1(line):
  # match pattern of form "mul(x,y)" where x and y are integers
  pattern = re.compile(r'mul\((\d+),(\d+)\)')
  # find all matches
  matches = pattern.findall(line)
  # sum the products of the matches
  sum = 0
  for match in matches:
    x = int(match[0])
    y = int(match[1])
    sum += x * y
  return sum

def part_2(line):
  line = "do()" + line
  pattern = re.compile(r'mul\((\d+),(\d+)\)')
  # sum the products of the matches
  sum = 0
  # split line into list of strings separated by "do()" and "don't()"
  # then join the parts that start with "do()"
  parts = line.split("do()")
  for part in parts:
    # emit the portions that start with "don't()"
    string_of_interest = part.split("don't()")[0]
    # find all matches
    matches = pattern.findall(string_of_interest)
    for match in matches:
      x = int(match[0])
      y = int(match[1])
      sum += x * y
  return sum


def main():
  input_path = '/home/pxd256/Workspace/aoc2024/pythonProject/day_03/input'
  with open(input_path, 'r') as f:
    lines = f.readlines()
  # join the lines into a single string
  joined_lines = ''.join(lines)
  print(part_1(joined_lines))
  print(part_2(joined_lines))


if __name__ == '__main__':
  main()
