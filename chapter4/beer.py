

def get_bottle_text(num):
  return "bottle" if num == 1 else "bottles"

def print_song(bottles):
  for bottles in range(bottles, 0, -1):
    bottle_text = get_bottle_text(bottles)
    next_bottle_text = get_bottle_text(bottles - 1)

    print("{0} {1} of beer on the wall, {0} {1} of beer! \
\nTake one down pass it around, {2} {3} of beer \
on the wall!\n".format(bottles, bottle_text, bottles - 1, next_bottle_text))

def main():
  bottles = int(input("Enter number of bottles: "))
  print_song(bottles)

if __name__ == '__main__':
  main()