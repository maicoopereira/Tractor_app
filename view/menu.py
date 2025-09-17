import tkinter as tk

def on_button_click():
    """Function to be executed when the button is clicked."""
    entered_text = entry.get()
    print(f"User entered: {entered_text}")
    label.config(text=f"You said: {entered_text}")

# Create the root window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")

# Create and pack a label
label = tk.Label(root, text="Enter something:")
label.pack(pady=10)

# Create and pack an entry widget
entry = tk.Entry(root)
entry.pack(pady=5)

# Create and pack a button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()