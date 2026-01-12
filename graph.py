import matplotlib.pyplot as plt
x = input('Enter the x-values separated by spaces: ');
y = input('Enter the y-values separated also by spaces: ')
x_values = list(map(int,x.split() ) )
y_values = list(map(int,y.split() ) )
plt.plot (x_values,y_values,color ="green", marker = 'x')
plt.title("This is a simple graph")
plt.xlabel("x values")
plt.ylabel("Y values")
plt.show()

