import math

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

delta = b**2 - 4*a*c # discreminant

if delta > 0:
	x = (-b - math.sqrt(delta)) / (2*a)
	x2 = (-b + math.sqrt(delta)) / (2*a)

	if x == x2:
		print(x)
	else:
		print(f"x' = {x} et x\" = {x2}")

if delta < 0:
	print("Impossible")