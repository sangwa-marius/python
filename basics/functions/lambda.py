greet = lambda name: f"Hello {name}"
square = lambda x : x**3
pow  = lambda a, b :a**b
add_any = lambda *args : sum(args)

print(greet("Marius"))
print(pow(4,3))
print(add_any(3,4,5,6))