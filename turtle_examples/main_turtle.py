import turtle1
import turtle2
import turtle3

def main():
  check = input("Which turtle would you like to run? ")
  if check == "1":
    turtle1.main()
  elif check == "2":
    turtle2.main()
  elif check == "3":
    turtle3.main()

if __name__ == '__main__':
  main()