# part 1 functions
def first_difference(l):
  new_l = []
  for i in range(len(l)-1):
    new_l.append(l[i+1] - l[i])
  return new_l

def verify_differences_sign(differences):
  for i in range(len(differences)-1):
    if differences[i] * differences[i+1] < 0:
      return False
  return True

def verify_differences_bound(differences):
  for d in differences:
    abs_d = abs(d)
    if not (1 <= abs_d <= 3):
      return False
  return True

# part 2 functions
# this function assumes that previous_value is already verified - thus does not handle first value
def verify_with_one_level_of_tolerance_dp(values, previous_value, previous_difference, remaining_tolerance, debug=False):
  if remaining_tolerance < 0:
    return False
  if len(values) == 0:
    return True
  difference = values[0] - previous_value
  # this is only true when the current index has the same sign and the difference is within the bound
  # this accounts for having no previous difference to compare with, by setting previous_difference to 0
  current_index_verified = difference * previous_difference >= 0 and 1 <= abs(difference) <= 3
  # if the current index is verified, then we can move on to the next index
  # if the current index is not verified, then we try to skip the current one but reduce one level of tolerance
  if current_index_verified:
    if verify_with_one_level_of_tolerance_dp(values[1:], values[0], difference, remaining_tolerance):
      return True
  return verify_with_one_level_of_tolerance_dp(values[1:], previous_value, previous_difference, remaining_tolerance - 1)

def verify_with_one_level_of_tolerance(values):
  # starts from the first value
  if verify_with_one_level_of_tolerance_dp(values[1:], values[0], 0, 1):
    return True
  # starts from the second value
  return verify_with_one_level_of_tolerance_dp(values[2:], values[1], 0, 0)

def main():
  input_path = '/home/pxd256/Workspace/aoc2024/pythonProject/day_02/input'
  with open(input_path, 'r') as f:
    lines = f.readlines()
  num_verified_part_1 = 0
  num_verified_part_2 = 0
  for line in lines:
    values = [int(x) for x in line.split()]
    differences = first_difference(values)
    if verify_differences_sign(differences) and verify_differences_bound(differences):
      num_verified_part_1 += 1
    if verify_with_one_level_of_tolerance(values):
      num_verified_part_2 += 1
  print(num_verified_part_1)
  print(num_verified_part_2)

if __name__ == '__main__':
  main()
