
dat =input("Ener the marks of the students separated by spaces:" )
data = list(map( int,dat.split() ))

for i in range (0,len(data)):
	if (data[i]>=80):
		print(f"{data[i]}: Grade A")
	elif (data[i]>=70 and data[i]<80):
		 print(f"{data[i]}: Grade B")
	elif (data[i]>=50 and data[i]<70):
		 print(f"{data[i]}: Grade C")
	else:
		 print(f"{data[i]}: Try harder next time please!")
