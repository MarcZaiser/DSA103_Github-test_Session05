def greetings(name: str) -> str: #Defines function with an argument as a string
    """Greetings by python"""
    return f"Hello {name}!" #calling function and recalling valuable

if __name__ == "__main__": #below only recalled if main file is called
    name = input("What is your name? ")
    print(greetings(name))
