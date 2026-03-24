def greet(name):
    return f"Hi, {name}!"   # changed line 💣

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(greet("Mehul"))
    print("Total:", add(5, 3))   # changed text
