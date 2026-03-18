import tkinter as tk
from tkinter import messagebox
import random

# Create main window
root = tk.Tk()
root.title("SmartLot")
root.geometry("400x500")
root.configure(bg="#f4f4f4")

# Header
header = tk.Label(root, text="🚗 SmartLot\nStop circling. Start parking.",
                  bg="#c8102e", fg="white", font=("Arial", 14), pady=10)
header.pack(fill="x")

# Info box
info_label = tk.Label(root, text="Select a parking lot",
                      bg="white", width=30, height=4, font=("Arial", 12))
info_label.pack(pady=20)

# Function to show parking info
def select_lot(name, spots):
    if spots > 0:
        info_label.config(
            text=f"{name}\n✅ {spots} spots available",
            fg="green"
        )
    else:
        info_label.config(
            text=f"{name}\n❌ Lot Full",
            fg="red"
        )

# Simulate navigation
def navigate():
    messagebox.showinfo("Navigation", "Navigation started! 🚗")

# Simulate real-time updates
def refresh():
    global lots
    for lot in lots:
        lots[lot] = random.randint(0, 15)
    messagebox.showinfo("Update", "Parking data updated!")

# Parking data
lots = {
    "Rams Lot": 12,
    "North Lot": 0,
    "Student Center": 7,
    "Library Lot": 0
}

# Buttons for lots
for name, spots in lots.items():
    color = "green" if spots > 0 else "red"

    btn = tk.Button(root,
                    text=name,
                    bg=color,
                    fg="white",
                    width=20,
                    height=2,
                    command=lambda n=name: select_lot(n, lots[n]))
    btn.pack(pady=5)

# Navigation button
nav_btn = tk.Button(root, text="Navigate", command=navigate,
                    bg="#c8102e", fg="white")
nav_btn.pack(pady=10)

# Refresh button
refresh_btn = tk.Button(root, text="Refresh Availability", command=refresh,
                        bg="#c8102e", fg="white")
refresh_btn.pack(pady=10)

# Run app
root.mainloop()