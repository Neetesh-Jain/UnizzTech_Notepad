import tkinter as tk
from tkinter import filedialog, messagebox

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r") as file:
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open file: {e}")

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_widget.get("1.0", tk.END))
            messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot save file: {e}")

# Function to exit the application
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

# Add a Text widget for writing text
text_widget = tk.Text(root, wrap="word", font=("Arial", 12))
text_widget.pack(expand=1, fill=tk.BOTH)

# Add a Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Attach the Menu bar to the main window
root.config(menu=menu_bar)

# Run the Tkinter event loop
root.mainloop()
