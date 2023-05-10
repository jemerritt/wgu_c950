import csv
import datetime

from packages import *

truck1_time = datetime.datetime(1, 1, 1, 8, 5, 00)     # Truck 1 departure time
truck2_time = datetime.datetime(1, 1, 1, 9, 5, 00)   # Truck 2 departure time
truck3_time = datetime.datetime(1, 1, 1, 10, 20, 00)   # Truck 3 departure time
truck1_miles = 0
truck2_miles = 0
truck3_miles = 0
truck1_location = 1
truck2_location = 1
truck3_location = 1

# Read distance info from csv file and insert into list
# O(N^2)
with open('./data/distances.csv') as csv_f:
    distance_list = list(csv.reader(csv_f, delimiter=';'))

    # Compare package and distance addresses to assign package address id
    for count in range(1, 41):
        check_value = get_value(count)
        for i in range(len(distance_list)):
            if check_value[1] in distance_list[i][1]:
                change_address_id(check_value[0], i + 1)
                break

    # Return distance from distance list for corresponding row and column
    # O(1)
    def get_distance(col, rw):
        distance = float(distance_list[col - 1][rw + 1])
        return distance

    # Using nearest neighbor algorithm determine the next location after each delivery and
    # mark package as delivered with timestamp
    # O(N)
    def shortest_route(package_list, current_location, truck):
        current_shortest = 20
        next_location = 0
        package_index = 0

        for index in package_list:
            chk_value = get_value(index)
            if chk_value[8] == 'en route     ':
                check_distance = get_distance(int(chk_value[7]), current_location)
                if check_distance < current_shortest:
                    current_shortest = check_distance
                    next_location = chk_value[7]
                    package_index = index
        if truck == 1:
            global truck1_miles
            global truck1_time
            truck1_miles += current_shortest
            truck1_time += datetime.timedelta(seconds=(current_shortest / 18 * 60 * 60))
            change_status(package_index, "Delivered at:", truck1_time.strftime("%H:%M:%S"))
        elif truck == 2:
            global truck2_miles
            global truck2_time
            truck2_miles = truck2_miles + current_shortest
            truck2_time += datetime.timedelta(seconds=(current_shortest / 18 * 60 * 60))
            change_status(package_index, "Delivered at:", truck2_time.strftime("%H:%M:%S"))
        elif truck == 3:
            global truck3_miles
            global truck3_time
            truck3_miles = truck3_miles + current_shortest
            truck3_time += datetime.timedelta(seconds=(current_shortest / 18 * 60 * 60))
            change_status(package_index, "Delivered at:", truck3_time.strftime("%H:%M:%S"))
        else:
            print('Error')
            exit()

        return int(next_location)

# Load trucks algorithmically using rules given in package info file
# O(N)
truck1 = []
truck2 = []
truck3 = []
for count in range(1, 41):
    check_value = get_value(count)
    if int(check_value[0]) == 6 or int(check_value[0]) == 25:
        change_status(count, "en route     ", truck2_time.strftime("%H:%M:%S"))
        truck2.append(check_value[0])
        continue
    if int(check_value[0]) == 9:
        change_status(count, "en route     ", truck3_time.strftime("%H:%M:%S"))
        truck3.append(check_value[0])
        continue
    if check_value[4] != 'EOD':
        if '' in check_value[6] or 'Must be' in check_value[6]:
            change_status(count, "en route     ", truck1_time.strftime("%H:%M:%S"))
            truck1.append(check_value[0])
            continue
    if 'Can only' in check_value[6] or 'Delayed on flight' in check_value[6]:
        change_status(count, "en route     ", truck2_time.strftime("%H:%M:%S"))
        truck2.append(check_value[0])
        continue
    if check_value[0] not in truck1 and check_value[0] not in truck2 and check_value[0] not in truck3:
        if len(truck2) < len(truck3):
            change_status(count, "en route     ", truck2_time.strftime("%H:%M:%S"))
            truck2.append(check_value[0])
            continue
        else:
            change_status(count, "en route     ", truck3_time.strftime("%H:%M:%S"))
            truck3.append(check_value[0])

# Deliver truck1 packages
# O(N^2)
for count in truck1:
    truck1_location = shortest_route(truck1, truck1_location, 1)

# Deliver truck2 packages
# O(N^2)
for count in truck2:
    truck2_location = shortest_route(truck2, truck2_location, 2)

# Deliver truck3 packages
# O(N^2)
for count in truck3:
    truck3_location = shortest_route(truck3, truck3_location, 3)

# Print total miles for all three trucks
# O(1)
print("\n        Total miles for today's route: ", truck1_miles + truck2_miles + truck3_miles)