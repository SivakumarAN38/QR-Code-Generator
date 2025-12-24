import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get().strip()

    if data == "" or data == PLACEHOLDER:
        messagebox.showerror("Error", "Please enter a URL or text")
        return

    qr = qrcode.make(data)
    qr.save("qrcode.png")

    img = Image.open("qrcode.png").resize((220, 220))
    img_tk = ImageTk.PhotoImage(img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    status_label.config(text="QR Code Generated Successfully ✔")

def clear_placeholder(event):
    if entry.get() == PLACEHOLDER:
        entry.delete(0, tk.END)
        entry.config(fg="black")

def add_placeholder(event):
    if entry.get() == "":
        entry.insert(0, PLACEHOLDER)
        entry.config(fg="gray")

# ---------------- UI SETUP ---------------- #

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
root.configure(bg="#f2f2f2")

card = tk.Frame(root, bg="white", bd=2, relief="groove")
card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)

tk.Label(
    card,
    text="QR Code Generator",
    font=("Segoe UI", 16, "bold"),
    bg="white"
).pack(pady=15)

# Placeholder text
PLACEHOLDER = "Enter URL or text"

entry = tk.Entry(
    card,
    font=("Segoe UI", 11),
    width=35,
    justify="center",
    fg="gray"
)
entry.pack(pady=10)
entry.insert(0, PLACEHOLDER)

entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", add_placeholder)

tk.Button(
    card,
    text="Generate QR",
    font=("Segoe UI", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    cursor="hand2",
    command=generate_qr
).pack(pady=12)

qr_label = tk.Label(card, bg="white")
qr_label.pack(pady=10)

status_label = tk.Label(
    card,
    text="",
    font=("Segoe UI", 9),
    fg="green",
    bg="white"
)
status_label.pack(pady=5)

root.mainloop()
