# total of cars available
cars = 100

# total passengers available per car
space_in_a_car = 4 # removed decimal

# total available drivers
drivers = 30

# total passengers to carpool
passengers = 90

# total cars without a driver
cars_not_driven = cars - drivers

# total cars with a driver
cars_driven = drivers

# total passengers we can transport
carpool_capacity = cars_driven * space_in_a_car

# average number of passengers per available car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today." # now is more readable without the decimal in 120.0 .
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
