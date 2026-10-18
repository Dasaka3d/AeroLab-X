import matplotlib.pyplot as plt

print("Welcome to the areodynamic lift calculator!")
'''
the equation for lift is : 0.5 * air density * speed^2 * wing area * lift coefficient
'''

air_density = float(input("Enter the air density (in kg/m^3): "))
wing_area = float(input("Enter the wing area (in m^2): "))  
lift_coefficient = float(input("Enter the lift coefficient (dimensionless): "))
if air_density <= 0 or wing_area <= 0 or lift_coefficient <= 0:
    print("Error: All input values must be positive numbers.")

else:
    lift_values = []
    speed_values = []
    for speed in range(1,21):
        lift = 0.5 * air_density * speed**2 * wing_area * lift_coefficient
        lift_values.append(lift)
        speed_values.append(speed)
    print(speed_values)
    print(lift_values)
    plt.plot(speed_values , lift_values , color = "green")
    plt.title("AeroLab X - Lift vs Wind Speed")
    plt.xlabel("Wind Speed (m/s)")
    plt.ylabel("Lift Force (N)")
    plt.grid(True)
    plt.savefig("lift_graph.png")
    plt.show()