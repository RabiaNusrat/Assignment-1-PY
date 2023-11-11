# Task 2
Length = input("Enter the value of Length: ")
Breadth = input("Enter the value of Breadth: ")
length_1 = int(Length)
Breadth_1 = int(Breadth)
Area = length_1 * Breadth_1
Perimeter = 4 * length_1
a1 = str(Area)
p1 = str(Perimeter)
if Length == Breadth:
    print("this shape is Sqaure" + " " + "its Area is" + " " + a1 + "its Perimter is" + " " + p1 )
else:
    print("this shape is Rectangle" + " " + "its Area is" + " " + a1 + "its Perimter is" + " " + p1)