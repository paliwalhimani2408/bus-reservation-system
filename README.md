# 🚌 Bus Reservation System

A simple **Bus Reservation System** developed using **Python**.
This project allows users to view available buses, check seat availability, book seats, cancel bookings, and view passenger details through a menu-driven program.

## 📌 Features

* View available buses and their details
* View available and booked seats
* Book a bus seat
* Cancel an existing booking
* View all passenger bookings
* Display fare, route, departure time, and seat details
* Input validation for invalid entries
* Menu-driven user interface

## 🛠️ Technologies Used

* **Python 3**
* Dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling
* User input/output

## 🚌 Bus Details

The system currently contains three buses:

| Bus No. | Route             | Departure | Fare |
| ------: | ----------------- | --------- | ---: |
|     101 | Bhopal to Udaipur | 8:00 AM   | ₹350 |
|     102 | Udaipur to Kolar  | 10:00 AM  | ₹250 |
|     103 | Udaipur to Delhi  | 7:00 PM   | ₹800 |

Each bus has **10 seats**.

## ⚙️ How the System Works

The program displays a menu with the following options:

1. **View Available Buses** – Shows bus number, route, departure time, fare, and available seats.
2. **View Bus Seats** – Shows which seats are available and which are booked.
3. **Book a Seat** – Allows the user to select a bus and an available seat and enter passenger details.
4. **Cancel Booking** – Allows the user to cancel an existing booking.
5. **View Passenger Bookings** – Displays all current passenger booking details.
6. **Exit** – Closes the program.

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Download or Clone the Repository

Clone the repository using:

```bash
git clone <your-repository-link>
```

### Step 3: Open the Project Folder

```bash
cd bus-reservation-system
```

### Step 4: Run the Program

```bash
python bus_reservation.py
```

## 📂 Project Structure

```text
Bus-Reservation-System/
│
├── bus_reservation.py
└── README.md
```

## 💡 Data Structure Used

The project uses **nested dictionaries** to store bus and passenger information.

Each bus contains:

* Route
* Departure time
* Fare
* Seat information

Passenger details stored for each booking include:

* Name
* Age
* Phone number

## 🔐 Input Validation

The program handles invalid inputs such as:

* Invalid bus numbers
* Invalid seat numbers
* Already booked seats
* Full buses
* Invalid numerical inputs

Python's `try-except` is used to handle `ValueError` exceptions.

## 🚀 Future Improvements

Some possible improvements for this project are:

* Add user login and registration
* Store bookings permanently using files or a database
* Generate booking tickets
* Add payment functionality
* Add more buses and routes
* Add date-wise reservations
* Provide an option to search buses by route

## 👩‍💻 Author

**Himani Paliwal**

### 📄 License

This project is created for **educational purposes** as a Python programming project.
