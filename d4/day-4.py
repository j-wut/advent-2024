import re

def countXMASAtCoord(input, i, j):
  count = 0
  # Left -> Right
  if j < len(input[i]) - 3 and input[i][j:j+4] == "XMAS":
    count += 1
  # Right -> Left
  if j >= 3 and input[i][j-3:j+1] == "SAMX":
    count += 1
  
  # Up -> Down
  if i < len(input) - 3:
    if input[i][j] == "X" \
      and input[i+1][j] == "M" \
      and input[i+2][j] == "A" \
      and input[i+3][j] == "S":
      count += 1
  
  # Down -> Up:
  if i >= 3:
    if input[i][j] == "X" \
      and input[i-1][j] == "M" \
      and input[i-2][j] == "A" \
      and input[i-3][j] == "S":
      count += 1

  # Top Left -> Bot Right
  if i < len(input) - 3 and j < len(input[i]) - 3:
    if input[i][j] == "X" \
      and input[i+1][j+1] == "M" \
      and input[i+2][j+2] == "A" \
      and input[i+3][j+3] == "S":
      count += 1
  
  # Bottom Left -> Top Right:
  if i >= 3 and j < len(input[i]) - 3:
    if input[i][j] == "X" \
      and input[i-1][j+1] == "M" \
      and input[i-2][j+2] == "A" \
      and input[i-3][j+3] == "S":
      count += 1

  # Top Right -> Bot Left
  if i < len(input) - 3 and j >= 3:
    if input[i][j] == "X" \
      and input[i+1][j-1] == "M" \
      and input[i+2][j-2] == "A" \
      and input[i+3][j-3] == "S":
      count += 1
  
  # Bottom Right -> Top Left:
  if i >= 3 and j >=3:
    if input[i][j] == "X" \
      and input[i-1][j-1] == "M" \
      and input[i-2][j-2] == "A" \
      and input[i-3][j-3] == "S":
      count += 1
  
  return count


def isCrossMAS(input, i, j):
  if not (0 < i < len(input) - 1 and 0 < j < len(input[0]) - 1):
    return False
  if (input[i-1][j-1] == "M" and input[i+1][j+1] == "S" or input[i-1][j-1] == "S" and input[i+1][j+1] == "M") \
    and (input[i+1][j-1] == "M" and input[i-1][j+1] == "S" or input[i+1][j-1] == "S" and input[i-1][j+1] == "M"):
    return True


def part1(input):
  count = 0
  for i in range(len(input)):
    for j in range(len(input[i])):
      if input[i][j] == "X":
        count += countXMASAtCoord(input, i, j)
  
  print(f"part 1: {count}")
  return count


def part2(input):
  count = 0
  for i in range(len(input)):
    for j in range(len(input[i])):
      if input[i][j] == "A":
        count += 1 if isCrossMAS(input, i, j) else 0
  
  print(f"part 2: {count}")
  return count


def main():
  with open("input.txt", "r") as input:
    inputs = input.readlines()
  p1 = part1(inputs)
  p2 = part2(inputs)




if __name__ == "__main__":
  main()