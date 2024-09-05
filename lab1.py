import math
circle_area = math.pi * 5 ** 2
print(circle_area)
sphere_volume = (4 / 3) * math.pi * 3 ** 3
print(sphere_volume)
triangle = 3 ** 2 + 4 ** 2
triangle_hyp = math.sqrt(triangle)
print(triangle_hyp)
name = "Zoe Myers"
print(len(name))
last_name = "Myers"
first_name ="Zoe"
full_name = (first_name) + " " + (last_name)
print(full_name)
age = "20 years old"
print(age)
print(type(age))
height_ft = 5.25
height_in = 63
print(height_ft)
print(type(height_ft))
weight = 135
print(str(weight) + " lbs")
print(type(weight))
BMI = weight / height_in ** 2 * 703
print(round(BMI, 2))