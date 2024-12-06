from collections import defaultdict

def isIncreasing(input: list[int], limit: int, dampener: int = 0):
  for i in range(1,len(input)):
    if input[i] <= input[i-1] or input[i] - input[i-1] > limit:
      if dampener:
        return isIncreasing(input[0:i]+input[i+1:], limit, dampener - 1) or isIncreasing(input[0:i-1] + input[i:], limit, dampener - 1)
      else:
        return False
  return True

def isDecreasing(input: list[int], limit: int, dampener: int = 0):
  for i in range(1,len(input)):
    if input[i] >= input[i-1] or input[i] - input[i-1] < limit:
      if dampener:
        return isDecreasing(input[i-1:i]+input[i+1:], limit, dampener - 1) or isDecreasing(input[0:i-1] + input[i:], limit, dampener - 1)
      else:
        return False
  return True


def part1(input: list[list[int]]):
  valids = [line for line in input if isIncreasing(line, 3) or isDecreasing(line, -3)]
  print(len(valids))
  return len(valids)

def part2(input: list[list[int]]):
  valids = [line for line in input if isIncreasing(line, 3, 1) or isDecreasing(line, -3, 1)]
  print(len(valids))
  return len(valids)

def main():
  with open("input.txt", "r") as input:
    inputs = [[int(i) for i in line.split()] for line in input.readlines()]
  p1 = part1(inputs)
  p2 = part2(inputs)




if __name__ == "__main__":
  main()