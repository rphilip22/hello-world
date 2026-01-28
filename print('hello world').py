#this program prompts the user for their name and greets them
name = input("What's your name? ").title()
clean = " ".join(name.split())
print(f"Hello, {clean}")
# or print("Hello," , name) or print(f"Hello, {name}")