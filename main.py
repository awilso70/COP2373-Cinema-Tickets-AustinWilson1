def ask_ticket(tickets_left):
    #function for asking number of tickets, storing purchase data, and creating the 1-4 boundary for the purchases
    while True:
        try:
        #asks user for tickets
            tickets_question = int(input(f"There are {tickets_left} tickets left. How many tickets would you like (1-4): "))
        #Checks if the number is 1-4
            if tickets_question < 1 or tickets_question > 4:
                print("You can only buy 1-4 tickets.")
            elif tickets_question > tickets_left:
                print(f"There are only {tickets_left} tickets left.")
            else:
                #updates ticket remaining and saves tickets purchased total
                tickets_left -= tickets_question
                return tickets_question, tickets_left
        except ValueError:
            print("Only valid numbers allowed.")

def main():
    ticket_amount = 20
    buyer_amount = 0
    #Continues function until there are no tickets left
    while ticket_amount > 0:
        tickets_purchased, ticket_amount = ask_ticket(ticket_amount)
        buyer_amount += 1
        print(f"Tickets purchased: {tickets_purchased}. Tickets left: {ticket_amount}.\n")
    #finishes purchases
    print(f"No more tickets left! Total buyers: {buyer_amount}")

main()