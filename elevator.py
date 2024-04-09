import math


def time_elevator():
    elevator_capacity = int(input())
    floors = int(input())
    quantity_people = [0]

    for a in range(floors):
        quantity = int(input())
        quantity_people.append(quantity)

    remains = 0  # 1
    time = 0  # 0

    for b in range(floors, 0, -1):
        if quantity_people[b] != 0:
            people = quantity_people[b] - remains  # 1
            num_trips = math.ceil(people / elevator_capacity)  # 0
            time += num_trips * b * 2

            if people % elevator_capacity == 0:
                remains = 0
            else:
                remains = elevator_capacity - (people % elevator_capacity)

    print(time)
