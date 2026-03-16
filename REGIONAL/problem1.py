# Problem
# A delivery company has p parcels to deliver. Each parcel requires cost units of fuel.
# Fuel is stored across several checkpoints along a route.
# You are given:
# p → number of parcels
# cost → fuel needed per parcel
# fuel[] → fuel available at each checkpoint (visited in order)
# Implement a function that returns the minimum number of checkpoints needed to complete all
# deliveries.
# Rules
# Return -1 if fuel is empty
# Return 0 if total fuel is insufficient
# Stop once enough fuel is accumulated
# Example
# Input:
# p = 5
# cost = 3
# fuel = [4, 6, 3, 5, 2]
# Output:
# 3

def parcel_deliveries(parcel,cost,fuel):
    if not fuel:
        return -1
    max_deliveries = parcel*cost
    if sum(fuel)<max_deliveries:
        return 0
    for i,j in enumerate(fuel):
        max_deliveries -= j
        if max_deliveries <= 0:
            return i

def other_sol(parcel,cost,fuel):
    if not fuel: 
        return -1
    max_del = parcel*cost
    for i,j in enumerate(fuel):
        max_del -= j
        if max_del<1: return i
    return 0

print(parcel_deliveries(int(input('Enter Number of Parcels: ')),
                        int(input('Enter Cost of Fuel: ')),
                        list(map(int,input('Enter list of checkpoints: ').split()))))

print(other_sol(int(input('Enter Number of Parcels: ')),
                        int(input('Enter Cost of Fuel: ')),
                        list(map(int,input('Enter list of checkpoints: ').split()))))