#this program prompts the user for their name and greets them

def main():
    #output greeting
    name = input("What's your name? ")
    hello(name)

    #output without passing the expected argument
    hello()

def hello(to=' '):
    print("Hello," , to)
