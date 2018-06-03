def yell(text):
    return text.upper() + "!"

def whisper(text):
    return text.lower() + "..."

def greet(func):
    greeting = func("Hi, I'm a Python program")
    print(greeting)
