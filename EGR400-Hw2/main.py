from sphere import Sphere

red = Sphere(1.7, .25)
print(dir(red))
print(red.volume)
print(red.surface_area)
print(red.density)

x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
for i in x:
    print(i[0], i[1], i[2], i[3], sep=' & ')
