def earning(hrs,rate):
    wage=hrs*rate
    return wage
def output(wage, hrs, rate):
    if hrs <= 40:
        print(wage)
    elif hrs > 40:
        print(40*rate + (hrs - 40)* 1.5*rate)
def main():
    
    hrs = float(input('Enter hours:'))
    rate = float(input('enter the rate:'))
    wage=(earning(hrs,rate))
    output(wage, hrs, rate)
main()  
