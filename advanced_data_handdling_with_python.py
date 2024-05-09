#2. Advanced Data Handling with Python

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def available_rooms():
    print('\nRooms Available:')
    available = False  
    available_rooms_list = []  
    for room_number, room_info in hotel_rooms.items():
        if room_info["status"] == "available":
            print(room_number)
            available_rooms_list.append(room_number)  
            available = True  
            
    if not available:  
        print('There are no rooms available currently')
        return None, None, None  

    room = input("\nWhat room would you like: ")
    customer_name = input("What is your name: ")
    return room, customer_name, available_rooms_list  


def book_room(available_rooms_func):
    available, customer_name, available_rooms_list = available_rooms_func()  
    if available is not None:
        room_number = available
        if room_number in available_rooms_list:  
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print("Room", room_number, "has been booked for", customer_name)
        else:
            print("Room", room_number, "is not available or invalid")

def check_out():
    room = input('What is your room number? : ')
    hotel_rooms[room]['status'] = "available"
    customer_name = hotel_rooms[room]['customer']
    hotel_rooms[room]['customer'] = ""
    print(f"{customer_name}'s has been checked out")

def display_status():
    print("\n     Room Statuses")
    for rooms in hotel_rooms:
        print(f"\nRoom: {rooms}\nStatus: {hotel_rooms[rooms]['status']}")

answer = input("Would you like to:\n1) Book a room\n2) Check out\n3) See all room statuses\nEnter Number: ")
if answer == "1":
    book_room(available_rooms)
elif answer == "2":
    check_out()
elif answer == "3":
    display_status()



