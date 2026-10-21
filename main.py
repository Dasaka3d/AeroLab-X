'''
open main.py and run the program. this is terminal only for now. this only calculates lift. you will need to add the following as shown in the teminal. A graph will appear after the input. but i could not show it as it was not available on xbox game bar recording. 

'''
import matplotlib.pyplot as plt

print("Welcome to the areodynamic lift calculator!")
'''
the equation for lift is : 0.5 * air density * speed^2 * wing area * lift coefficient
'''
#inputs 
air_density = float(input("Enter the air density (in kg/m^3): "))
wing_area = float(input("Enter the wing area (in m^2): "))  
lift_coefficient = float(input("Enter the lift coefficient (dimensionless): "))


#error message
if air_density <= 0 or wing_area <= 0 or lift_coefficient <= 0:
    print("Error: All input values must be positive numbers.")
#rest of the code 
else:
    #Global variables
    lift_values = []
    speed_values = []
    drag_values = []
    #looping to find drag and lift.
    for speed in range(1,21):
        lift = 0.5 * air_density * speed**2 * wing_area * lift_coefficient
        lift_values.append(lift)
        speed_values.append(speed)

    #printing everything for the user to see the results
    print(f"the lift is {lift_values}")
    plt.plot(speed_values , lift_values , color = "green")
    plt.title("AeroLab X - Lift vs Wind Speed")
    plt.xlabel("Wind Speed (m/s)")
    plt.ylabel("Lift Force (N)")
    plt.grid(True)
    plt.savefig("lift_graph.png")
    plt.show()