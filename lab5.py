import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
from data import Time
#Takes in two times then adds them, also ensuring it stays within 60 minutes
def time_add(time1:Time, time2:Time) -> Time:
    added_hours = time1.hour + time2.hour
    added_minutes = time1.minute + time2.minute
    added_seconds = time1.second + time2.second
    #Add each of the times together
    while added_minutes // 60 >= 1:
        added_hours += 1
        added_minutes -= 60

    while added_seconds // 60 >= 1:
        added_minutes += 1
        added_seconds -= 60
    #If minutes or seconds over 60 transfer it to an hour or minute
    return Time(added_hours, added_minutes, added_seconds)

# Part 4
#Checks if the list is descending
def is_descending(list:list[float]) -> bool:
    count = 0
    #Count used to check how many times it descends
    for x in range(len(list) - 1):
        if list[x] > list [x + 1]:
            count += 1
    if count == len(list) - 1:
        return True
    else:
        return False
    #If it consistently descends throughout the whole list, the count will equal the iterations

# Part 5
#Takes in a list and two indexes to compare to check which two ints in the list are larger
def largest_between(list:list[int], idx1:int, idx2:int):
    if idx1 > idx2:
        return None
    #Begins be checking if index is larger than other
    if list[idx1] > list[idx2]:
        return list[idx1]
    elif list[idx2] > list[idx1]:
        return list[idx2] #Returns the values as normal
    elif list[idx1] == None and list[idx2] == None:
        return None
    elif list[idx1] == None:
        return list[idx2]
    else:
        return list[idx1]
    #If the values are not real return None if only one idx works return that idx
# Part 6
from data import Point
def furthest_from_origin(points:list[Point]):
    if type(points) == type[list]:
        return None

    fP = points[0]
    for i in points:
        if abs(i.x + i.y) > abs(fP.x + fP.y):
            fP = i

    return fP
