with open("calculator.py","r")as f:
	for line in f:
		print(line.strip())


with open("py.py","r") as f:
	data = f.read()
	print (data)


with open("3a.py","r") as f:
	data = f.readlines()
	count = 1
	for line in data:
		print(f"{count} {line}")
		count +=1
