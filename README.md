# 🚌 Bus Ticket Booking System (Python GUI)

## 📌 Project Overview

This project is a **graphical bus ticket booking application** developed using **Python and Tkinter**. It allows users to select travel dates, check ticket availability, and book tickets through an interactive interface.

The system dynamically manages ticket availability for upcoming days and provides instant booking confirmation.

---

## 🎯 Main Features

* 📅 Display booking options for the next 7 days
* 🎟️ Real-time ticket availability tracking
* 👤 User input for name and number of tickets
* ⚠️ Input validation with error messages
* ✅ Instant booking confirmation popup
* 🔄 Automatic update of remaining tickets

---

## 🧠 Concepts Used

* GUI development using Tkinter
* Event-driven programming
* Dictionary data structure for ticket tracking
* Date and time handling using `datetime`
* Input validation and exception handling

---

## 🛠️ Technologies

* Language: Python
* Library: Tkinter
* Platform: Desktop GUI Application

---

## ▶️ How to Run

### Step 1: Run the program

```bash id="py1run"
python BusTicketBookingSystem.py
```

---

## 📋 How It Works

1. The system displays available dates for the next 7 days
2. User selects a preferred date
3. User enters name and number of tickets
4. System checks availability
5. Booking is confirmed if tickets are available
6. Remaining tickets are updated instantly

---

## ⚠️ Validations Implemented

* Empty name is not allowed
* Ticket count must be a positive number
* Cannot book more tickets than available

---

## 💡 Example Functionality

* If 50 tickets are available and user books 5 → remaining becomes 45
* If user tries to book more than available → error message is shown

---

## ⚠️ Limitations

* Ticket data is not stored permanently
* No login or authentication system
* Limited to demo-level functionality

---

## 🔮 Future Enhancements

* Add database integration (MySQL/SQLite)
* Implement login system
* Add seat selection feature
* Online payment integration
* Expand to train/flight booking

---

## 👨‍💻 Developer

Pruthviraj Patil

---

## ⭐ Summary

This project demonstrates how Python GUI applications can be used to simulate real-world systems like ticket booking, combining usability with basic programming concepts.
