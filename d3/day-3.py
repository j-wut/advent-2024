import re

def part1(input: list[str]):
  accum = 0
  mulRegex = r"mul\((\d+),(\d+)\)"
  
  for line in input:
    matches = re.findall(mulRegex, line)
    for m in matches:
      accum += int(m[0]) * int(m[1])
  print(f"part 1: {accum}")
  return accum

def part2(input: list[str]):
  accum = 0
  mulRegex = r"mul\((\d+),(\d+)\)"
  validCommands = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"
  isdo = True
  
  for line in input:
    matches = re.findall(validCommands, line)
    for m in matches:
      if m[:5] == "don't":
        isdo = False
      elif m[:2] == "do":
        isdo = True
      else:
        if not isdo:
          continue
        nums = re.match(mulRegex, m).groups()
        accum += int(nums[0]) * int(nums[1])
  print(f"part 2: {accum}")
  return accum

def main():
  with open("input.txt", "r") as input:
    inputs = input.readlines()
  p1 = part1(inputs)
  p2 = part2(inputs)




if __name__ == "__main__":
  main()