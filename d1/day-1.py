from collections import defaultdict

def part1(l1, l2):
  score = 0
  l1 = sorted(l1)
  l2 = sorted(l2)
  for i in range(len(l1)):
    score += abs(l1[i] - l2[i])
  print("part1: ", score)
  return score

def part2(l1, l2):
  score = 0
  m = defaultdict(int)
  for n in l2:
    m[n] += 1
  for n in l1:
    score += n*m[n]
  print("part2: ", score)
  return score

def main():
  l1, l2 = [], []
  with open("input.txt", "r") as input:
    for line in input.readlines():
      splits = line.split()
      l1.append(int(splits[0]))
      l2.append(int(splits[1]))
  p1 = part1(l1, l2)
  p2 = part2(l1, l2)




if __name__ == "__main__":
  main()