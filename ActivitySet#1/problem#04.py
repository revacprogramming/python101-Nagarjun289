sh =  float(input("Enter Hours:"))
sr = float(input("Enter Rate:"))


if sh<=40 :
  
   print(sh*sr)
elif sh>40:
   print(40*sr+(sh-40)*1.5*sr)
  
