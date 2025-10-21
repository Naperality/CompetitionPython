# Your task is to return the number of people who are still on the bus 
# after the last bus stop (after the last array). Even though it is 
# the last bus stop, the bus might not be empty and some people might still 
# be inside the bus, they are probably sleeping there :D

# Take a look on the test cases.

# Please keep in mind that the test cases ensure that the number of people 
# in the bus is always >= 0. So the returned integer can't be negative.

# The second value in the first pair in the array is 0, since the bus is empty 
# in the first bus stop.

def diff_pair(bus_stops):
    # return sum(first[0] for first in bus_stops) - sum(first[1] for first in bus_stops)
    return sum(first-second for first, second in bus_stops)

print(diff_pair([[10,0], [3,5], [5,8]]))