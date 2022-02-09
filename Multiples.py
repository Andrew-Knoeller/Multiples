# Program to take a number and print any number of multiples you decide of that number.
# includes a try/except to validate user input

multiple = input("Enter number: ")
while True:
    try:
        multiple = int(multiple)
        break
    except:
        multiple = input("Sorry, please enter a number: ")

max = input("Enter how many multiples of the number you want: ")
while True:
    try:
        max = int(max)
        max += 1
        break
    except:
        max = input("Sorry, please enter a number: ")


 print("The multiples are of ", multiple, " are:")
for i in range(1,max):
    print(multiple, "*", i, "=", multiple*i)

print("Thanks for trying my program!")
input("Press any key to exit")

