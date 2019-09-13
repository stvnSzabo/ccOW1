ora1 = int(input("Hour?"))
perc1 = int(input("Minute?"))
mp1 = int(input("Second?"))

ora2 = int(input("Hr2?"))
perc2 = int(input("Min2?"))
mp2= int(input("Sec2?"))

print(str((ora2*3600 + perc2*60 + mp2) -( ora1*3600 + perc1*60 + mp1)) )
