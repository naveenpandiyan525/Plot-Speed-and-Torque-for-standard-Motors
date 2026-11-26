import matplotlib.pyplot as plot
import csv


rpm, torque = [],[] 

with open ("nema23_torque_vs_rpm.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for i in reader:
        rpm.append(i[0])
        torque.append(i[1])

plot.title("Speed and Torque relationo of Motor")
plot.plot(rpm,torque, label="Legend", color="red")
plot.xlabel("Speed (rpm)")
plot.ylabel("Torque (nm)")
plot.legend()
plot.grid()
plot.ioff()
plot.show()