userVolt = input("Enter voltage: ")

userResist = input("Enter Resistence: ")

power = 0.0

userVolt = float(userVolt*userVolt)
power = userVolt/userResist

print('Your power is:' , power)