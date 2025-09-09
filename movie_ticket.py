total_seats = int(input("total_seats= "))
booked_seats = list(map(int, input("booked_seats= ").split(',')))
book_seat = int(input("book_seat= "))
cancel_seat = int(input("cancel_seat= "))

def book_ticket(seat):
    if seat in booked_seats:
        print("seat booked")
    else:
        booked_seats.append(seat)

def cancel_ticket(seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
        print(f"Seat {seat} cancelled successful.")
    else:
        print(f"Seat {seat} didnt booked")

book_ticket(book_seat)
cancel_ticket(cancel_seat)
available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
print("\nAvailable seats:", available_seats)
print("Booked seats:", booked_seats)
