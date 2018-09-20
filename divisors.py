print("This program will tell you the divisors of the number you type in")

the_number = input("What is you number?: ")

print("The divisors are")

for x in range(1, int(the_number)):
    if int(the_number) % x == 0:
        print(x)
