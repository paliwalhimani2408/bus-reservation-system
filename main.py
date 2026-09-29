# Bus Reservation System

buses = {
    101: {
        "route": "Bhopal to Udaipur",
        "time": "8:00 AM",
        "fare": 350,
        "seats": {}
    },
    102: {
        "route": "Udaipur to Kolar",
        "time": "10:00 AM",
        "fare": 250,
        "seats": {}
    },
    103: {
        "route": "Udaipur to Delhi",
        "time": "7:00 PM",
        "fare": 800,
        "seats": {}
    }
}

TOTAL_SEATS = 10


def view_buses():
    print("\n===== AVAILABLE BUSES =====")

    for bus_no, bus in buses.items():
        available = TOTAL_SEATS - len(bus["seats"])

        print("\nBus Number:", bus_no)
        print("Route:", bus["route"])
        print("Departure:", bus["time"])
        print("Fare: Rs.", bus["fare"])
        print("Available Seats:", available)


def view_seats():
    print("\n===== VIEW SEATS =====")

    try:
        bus_no = int(input("Enter bus number: "))

        if bus_no not in buses:
            print("Invalid bus number.")
            return

        print("\nBus:", bus_no)
        print("Route:", buses[bus_no]["route"])

        for seat in range(1, TOTAL_SEATS + 1):
            if seat in buses[bus_no]["seats"]:
                print("Seat", seat, "- BOOKED")
            else:
                print("Seat", seat, "- AVAILABLE")

    except ValueError:
        print("Please enter a valid bus number.")


def book_seat():
    print("\n===== BOOK A SEAT =====")

    try:
        bus_no = int(input("Enter bus number: "))

        if bus_no not in buses:
            print("Invalid bus number.")
            return

        if len(buses[bus_no]["seats"]) == TOTAL_SEATS:
            print("Sorry, all seats are booked.")
            return

        print("\nAvailable seats:")

        for seat in range(1, TOTAL_SEATS + 1):
            if seat not in buses[bus_no]["seats"]:
                print(seat, end=" ")

        print()

        seat_no = int(input("Enter seat number: "))

        if seat_no < 1 or seat_no > TOTAL_SEATS:
            print("Invalid seat number.")
            return

        if seat_no in buses[bus_no]["seats"]:
            print("Sorry, this seat is already booked.")
            return

        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        phone = input("Enter phone number: ")

        buses[bus_no]["seats"][seat_no] = {
            "name": name,
            "age": age,
            "phone": phone
        }

        print("\n===== BOOKING SUCCESSFUL =====")
        print("Passenger Name:", name)
        print("Bus Number:", bus_no)
        print("Route:", buses[bus_no]["route"])
        print("Seat Number:", seat_no)
        print("Fare: Rs.", buses[bus_no]["fare"])

    except ValueError:
        print("Please enter valid information.")


def cancel_booking():
    print("\n===== CANCEL BOOKING =====")

    try:
        bus_no = int(input("Enter bus number: "))

        if bus_no not in buses:
            print("Invalid bus number.")
            return

        seat_no = int(input("Enter seat number: "))

        if seat_no not in buses[bus_no]["seats"]:
            print("No booking found for this seat.")
            return

        passenger = buses[bus_no]["seats"][seat_no]

        print("\nBooking found!")
        print("Passenger:", passenger["name"])

        confirm = input("Do you want to cancel this booking? (yes/no): ")

        if confirm.lower() == "yes":
            del buses[bus_no]["seats"][seat_no]
            print("Booking cancelled successfully.")
        else:
            print("Booking was not cancelled.")

    except ValueError:
        print("Please enter valid information.")


def view_bookings():
    print("\n===== PASSENGER BOOKINGS =====")

    found = False

    for bus_no, bus in buses.items():
        for seat_no, passenger in bus["seats"].items():

            found = True

            print("\nBus Number:", bus_no)
            print("Route:", bus["route"])
            print("Seat Number:", seat_no)
            print("Passenger Name:", passenger["name"])
            print("Age:", passenger["age"])
            print("Phone:", passenger["phone"])

    if not found:
        print("No bookings available.")


def main():
    while True:

        print("\n================================")
        print("      BUS RESERVATION SYSTEM")
        print("================================")
        print("1. View Available Buses")
        print("2. View Bus Seats")
        print("3. Book a Seat")
        print("4. Cancel Booking")
        print("5. View Passenger Bookings")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_buses()

        elif choice == "2":
            view_seats()

        elif choice == "3":
            book_seat()

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            view_bookings()

        elif choice == "6":
            print("\nThank you for using the Bus Reservation System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()