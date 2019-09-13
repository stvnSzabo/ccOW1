sntnc = input("Enter Your Sentence: ")
sntncwows = ""

for i in sntnc:
    if i != " ":
        sntncwows = sntncwows + i
    elif i == " ":
        continue

print(sntncwows)