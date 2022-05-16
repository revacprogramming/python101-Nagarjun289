# Variables, Expressions & Statements

def earning(hrs,rate):
  wage=hrs*rate
  return wage
def output(wage):
  print('Pay:',wage)
def main():
  hrs=float(input("enter hours:"))
  rate=float(input("enter rate"))
  wage=earning(hrs,rate)
  output(wage)
main()
  
  