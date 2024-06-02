import tkinter as tk
import random
import string

def generate_password(length):
    """Generate a single password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords():
    """Generate passwords based on user input and display them."""
    try:
        num_passwords = int(num_passwords_entry.get())
        password_length = int(password_length_entry.get())
        passwords = [generate_password(password_length) for _ in range(num_passwords)]
        passwords_text.delete('1.0', tk.END)  # Clear previous passwords
        passwords_text.insert(tk.END, '\n'.join(passwords))
    except ValueError:
        passwords_text.delete('1.0', tk.END)  # Clear previous passwords
        passwords_text.insert(tk.END, "Invalid input. Please enter numbers only.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input fields and labels
tk.Label(root, text="Number of Passwords:").grid(row=0, column=0, sticky="e")
num_passwords_entry = tk.Entry(root)
num_passwords_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Password Length:").grid(row=1, column=0, sticky="e")
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a button to generate passwords
generate_button = tk.Button(root, text="Generate", command=generate_passwords)
generate_button.grid(row=2, column=0, columnspan=2, pady=5)

# Create a text widget to display passwords
passwords_text = tk.Text(root, height=10, width=30)
passwords_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
root.mainloop()
