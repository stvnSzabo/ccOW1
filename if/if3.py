Even_count = 0
Odd_count = 0
Odd_Sum = 0


Number = int(input("How many numbers "))
for i in range(Number):
    num = int(input("Number: "))
    if num % 2 == 0:
        Even_count +=1

    else:
        Odd_count +=1
        Odd_Sum += num

    



print("\n Even numbers =  ", Even_count)
print("Odd numbers = ", Odd_count)
print("\n Sum of Odd Numbers = ", Odd_Sum)
