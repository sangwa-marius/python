import matplotlib.pyplot as plt

def get_values(prompt):
    while True:
        try:
            values = input(prompt)
            values_list = list(map(float, values.split()))
            if len(values_list) == 0:
                raise ValueError("You must enter at least one value.")
            return values_list
        except ValueError:
            print("Invalid input! Please enter numbers separated by spaces.")


x_values = get_values("Enter the x-values separated by spaces: ")
y_values = get_values("Enter the y-values separated by spaces: ")


if len(x_values) != len(y_values):
    print("Error: The number of x-values and y-values must be the same.")
    exit()


plt.plot(x_values, y_values, color="green", marker='o', linestyle='-', label="Line Plot")


plt.scatter(x_values, y_values, label="Data Points")


plt.title("This is a Simple Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)          
plt.legend()          
plt.tight_layout()      


plt.show()


