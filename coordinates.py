coordinates = [(1,3),(3,2),(0,9),(1,2),(4,5)]
closest_point = coordinates[0]
closest_distance = coordinates[0][0]**2 + coordinates[0][1]**2
for coordinate in coordinates:
    x,y = coordinate 
    distance = x**2 +y**2

    if distance<closest_distance:
        closest_distance = distance
        closest_point = coordinate
print("closest point:",closest_point)
