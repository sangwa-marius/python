squares = [ x**2 for x in range(5)]
evens = [x for x in range (21) if x%2==0]
pairs = [(x,y) for x in range(3) for y in range (4) ]

print(squares,evens,pairs)