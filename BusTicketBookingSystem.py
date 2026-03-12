import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Bus Ticket Booking System
class BusTicketBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Ticket Booking System")
        
        # Initialize available tickets for each day (just for demo purposes)
        self.available_tickets = {self.get_date_string(i): 50 for i in range(7)}  # 50 tickets for each day

        # Create a title label
        self.title_label = tk.Label(root, text="Bus Ticket Booking System", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Create a label to show available dates
        self.date_label = tk.Label(root, text="Select a date to book your ticket:", font=("Arial", 12))
        self.date_label.pack()

        # Create buttons for each date in the next 7 days
        #self.date_buttons = []
        for i in range(7):
            date_button = tk.Button(root, text=self.get_date_string(i), command=lambda i=i: self.show_ticket_details(i))
            date_button.pack(pady=5)
            #self.date_buttons.append(date_button)

        # Frame to hold the ticket booking interface (Initially hidden)
        self.booking_frame = tk.Frame(root)
        
        # User Name Entry
        self.name_label = tk.Label(self.booking_frame, text="Enter your name:", font=("Arial", 12))
        self.name_entry = tk.Entry(self.booking_frame, font=("Arial", 12))
        
        # Number of Tickets Entry
        self.ticket_label = tk.Label(self.booking_frame, text="Number of Tickets:", font=("Arial", 12))
        self.ticket_entry = tk.Entry(self.booking_frame, font=("Arial", 12))

        # Book Button
        self.book_button = tk.Button(self.booking_frame, text="Book Ticket", font=("Arial", 12), command=self.book_ticket)

    # Function to get the date string (next 7 days)
    def get_date_string(self, offset):
        date = datetime.now() + timedelta(days=offset)
        return date.strftime("%Y-%m-%d")

    # Show ticket details for the selected date
    def show_ticket_details(self, day_index):
        selected_date = self.get_date_string(day_index)
        
        # Show available tickets and date
        if self.available_tickets[selected_date] > 0:
            self.booking_frame.pack_forget()  # Hide the booking frame before showing it again
            self.booking_frame.pack(pady=20)  # Show the booking frame

            self.name_label.pack()
            self.name_entry.pack(pady=5)
            
            self.ticket_label.pack()
            self.ticket_entry.pack(pady=5)
            
            self.book_button.pack(pady=10)
            
            self.selected_date = selected_date
            self.remaining_tickets_label = tk.Label(self.booking_frame, text=f"Available Tickets for {selected_date}: {self.available_tickets[selected_date]}", font=("Arial", 12))
            self.remaining_tickets_label.pack(pady=5)
        else:
            messagebox.showinfo("No Tickets Available", f"No tickets available for {selected_date}. Please choose another date.")

    # Book the ticket
    def book_ticket(self):
        try:
            name = self.name_entry.get()
            num_tickets = int(self.ticket_entry.get())
            
            if name == "" or num_tickets <= 0:
                messagebox.showerror("Invalid Input", "Please enter a valid name and ticket number.")
                return

            if num_tickets > self.available_tickets[self.selected_date]:
                messagebox.showerror("Not Enough Tickets", f"Only {self.available_tickets[self.selected_date]} tickets are available for {self.selected_date}.")
                return

            # Proceed with booking
            self.available_tickets[self.selected_date] -= num_tickets
            messagebox.showinfo("Booking Confirmed", f"Thank you, {name}! Your booking for {num_tickets} tickets on {self.selected_date} has been confirmed.")
            
            # Update remaining tickets label
            self.remaining_tickets_label.config(text=f"Available Tickets for {self.selected_date}: {self.available_tickets[self.selected_date]}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of tickets.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BusTicketBookingSystem(root)
    root.mainloop()
