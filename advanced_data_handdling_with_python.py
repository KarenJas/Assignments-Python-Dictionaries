#2. Advanced Data Handling with Python
    #display roooms available to person
    #if none display message saying non available
    #ask is they would like to take the room
    #if yes update dictionary and take variable
    #if no break loop
        #variables from customers:
            #name
            #room number


hotel_rooms = {
    "101": {"status": "booked", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"},
    "103": {"status": "booked", "customer": ""},
    "104": {"status": "booked", "customer": ""},
}

#prints available rooms
def available_rooms():
    print('Rooms Available:')
    available = False  # Flag to track if any rooms are available
    available_rooms_list = []

    for room_number, room_info in hotel_rooms.items():
        if room_info["status"] == "available":
            print(room_number)
            available_rooms_list.append(room_number)
            available = True  # Set the flag to True if at least one room is available
            
    if not available:  # If no rooms are available, print a message
        print('There are no rooms available currently')
        return None, None, None
    
    if available == True: 
        room = input("What room would you like: ")
        customer_name = input("what is ur name: ")
    return customer_name, room, available_rooms_list



def book_room (availability):
    name,room_number, available_rooms_list = availability()
    if room_number in available_rooms_list:
        hotel_rooms[room_number]["status"] = "booked"
        hotel_rooms[room_number]["customer"] = name
        #test: print(hotel_rooms)


book_room(available_rooms)

#test: book_room(customer_name,room)

#ask customer if they are ready to check out 
#if no break loop?
#if yes check out function activate 
# finish off by displaying status of all the rooms 
