# Functions


def computepay(h, r):
    if sh<=40 :
       print(sh*sr)
    elif sh>40:
       print(40*sr+(sh-40)*1.5*sr)
  


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
