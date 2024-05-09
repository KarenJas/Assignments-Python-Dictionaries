#3. Python Programming Challenges for Customer Service Data Handling

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_new_ticket():
    next_ticket_id = "Ticket" + str(len(service_tickets) + 1).zfill(3)
    
    print("\n    Open new service ticket\n")
    customer_name = input('Customer name:')
    issue_description = input("Product issue: ")
    status = input("Status (open/closed): ") 

    new_ticket = {
    "Customer": customer_name,
    "Issue": issue_description,
    "Status": status
    }

    service_tickets[next_ticket_id] = new_ticket

    print(f"\nNew Ticket:{next_ticket_id}")

def update_status(ticket_number):
    decision = input('Would you like to open or close the status: ')
    if decision == 'open':
        service_tickets[ticket_number]['Status'] = 'Open'
    elif decision == 'close':
        decision ='clos'
        service_tickets[ticket_number]['Status'] = 'Open'
        print(f"{service_tickets[ticket_number]['Customer']}'s ticket has been {decision}ed")

def display_ticket_status():
    print("\n    Tickets")
    for tickets in service_tickets:
        print(f"\nTicket Number: {tickets}\nIssue: {service_tickets[tickets]["Issue"]}\nStatus: {service_tickets[tickets]["Status"]}\n")




answer = input("what would you like to do:\n1)open new service ticket\n2)update the status of an existing ticket\n3)display all tickets\nEnter Number:  ")
if answer == "1":
    open_new_ticket()
elif answer == "2":
    ticket_number = input("\nWhat is your ticket number: ")
    update_status(ticket_number)
elif answer == '3':
    display_ticket_status()











