 
number=int(input("Money: "))


ten = 0
fiv = 0
two = 0
one = 0

if number//10>0:
    ten=number//10
    number=number-(ten*10)

if number//5>0:
    fiv=number//5
    number=number-(fiv*5)

if number//2>0:
    two=number//2
    number=number-(two*2)

if number//1>0:
    one=number//1
    number=number-(one*1)

if number == 0:

    
    print("Number of 10s: "+str(ten))
    print("Number of 5s: "+str(fiv))
    print("Number of 2s: "+str(two))
    print("Number of 1s: "+str(one))
