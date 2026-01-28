#this program asks the user for a number and prints its square
#number = float(input("Please enter a number: "))
#square = number ** 2
#print(f"The square of {number} is {square}")

#def main():
#    number = float(input("Please enter a number: "))
#    square = number ** 2
#    print(f"The square of {number} is {square}")

#main()

def main():
    number = float(input("Please enter a number: "))
    print(f"The square of {number} is {square(number)}")

def square(n):
    return n * n

main()