document = open("93cars.dat.txt", "r")
city_MPG = 0
highway_MPG = 0
average_MRP = 0
num_cars = 0
count = 1
for i in document:
    if count % 2 == 1:
        city_MPG += float(i[52:54])
        highway_MPG += float(i[55:57])
        average_MRP += float(i[42:46])
        num_cars += 1
    count += 1
a = city_MPG/num_cars
b = highway_MPG/num_cars
c = average_MRP/num_cars

print("Average gas mileage in city: " + str(a))
print("Average gas mileage on highway: " + str(b))
print("Average midrange price of the vehicles: " + str(c))
