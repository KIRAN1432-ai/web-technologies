def greet(name,prefix='Hello',formatter=lambda x:x):
    return formatter(f"{prefix} {name}")
print(greet("kiran"))
print(greet("kiran",formatter=str.upper))