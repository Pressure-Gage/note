import math

angle1 = int(input("what is the angle of incidence?: "))
angle2 = 90
dis = int(input("How far are you from the tree?: "))

to_rads = math.radians(angle1)
opp = (math.tan(to_rads)) * dis
ans = opp + 1.67

print("The tree is", ans, 'm')