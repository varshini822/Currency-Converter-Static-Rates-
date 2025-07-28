import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💱 Currency Converter (Static Rates)")
        self.root.geometry("500x550")
        self.root.configure(bg="#f0f8ff")
        self.root.resizable(False, False)

        self.exchange_rates = {
            'USD': 1.0,
            'INR': 83.0,
            'EUR': 0.91,
            'GBP': 0.78,
            'JPY': 140.0
        }

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Currency Converter", font=("Helvetica", 22, "bold"), bg="#f0f8ff", fg="#003366").pack(pady=15)

        # Amount
        tk.Label(self.root, text="Enter Amount:", font=("Arial", 12), bg="#f0f8ff").pack()
        self.amount_entry = tk.Entry(self.root, font=("Arial", 14), justify="center", width=20)
        self.amount_entry.pack(pady=10)

        # Dropdown Frame
        dropdown_frame = tk.Frame(self.root, bg="#f0f8ff")
        dropdown_frame.pack(pady=10)

        self.from_currency = ttk.Combobox(dropdown_frame, values=list(self.exchange_rates.keys()), state="readonly", width=10, font=("Arial", 12))
        self.from_currency.set("USD")
        self.from_currency.grid(row=0, column=0, padx=10)

        # Swap button
        tk.Button(dropdown_frame, text="⇄", font=("Arial", 12, "bold"), bg="#d0d0ff", command=self.swap_currencies).grid(row=0, column=1)

        self.to_currency = ttk.Combobox(dropdown_frame, values=list(self.exchange_rates.keys()), state="readonly", width=10, font=("Arial", 12))
        self.to_currency.set("INR")
        self.to_currency.grid(row=0, column=2, padx=10)

        # Convert Button
        tk.Button(self.root, text="Convert", font=("Arial", 12, "bold"), bg="#c8e6c9", fg="black", command=self.convert_currency).pack(pady=15)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#f0f8ff", fg="#222")
        self.result_label.pack(pady=10)

        # Reset Button
        tk.Button(self.root, text="Reset", font=("Arial", 11, "bold"), bg="#ffcccc", command=self.reset).pack()

        # History label and log
        tk.Label(self.root, text="🧾 Conversion History:", font=("Arial", 12, "bold"), bg="#f0f8ff", fg="#003366").pack(pady=10)
        self.history_box = scrolledtext.ScrolledText(self.root, height=8, width=52, font=("Arial", 10))
        self.history_box.pack(pady=5)
        self.history_box.config(state="disabled")

        # Status Bar
        self.status_label = tk.Label(self.root, text="💬 Ready to convert!", font=("Arial", 10, "italic"),
                                     bg="#dfeffc", fg="#444", bd=1, relief="sunken", anchor="w")
        self.status_label.pack(side="bottom", fill="x")

    def convert_currency(self):
        try:
            amount_text = self.amount_entry.get().strip()
            if not amount_text:
                raise ValueError("Empty input")

            amount = float(amount_text)
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            if from_curr == "" or to_curr == "":
                raise ValueError("Currency not selected")

            if from_curr == to_curr:
                converted = amount
            else:
                usd_amount = amount / self.exchange_rates[from_curr]
                converted = usd_amount * self.exchange_rates[to_curr]

            result = f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}"
            self.result_label.config(text=result)
            self.status_label.config(text=f"✅ Converted from {from_curr} to {to_curr}")
            self.log_history(result)

        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Error: {e}")
            self.status_label.config(text="⚠️ Conversion failed: Invalid input")

    def reset(self):
        self.amount_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.from_currency.set("USD")
        self.to_currency.set("INR")
        self.status_label.config(text="🔁 Reset successful.")
        self.history_box.config(state="normal")
        self.history_box.delete(1.0, tk.END)
        self.history_box.config(state="disabled")

    def swap_currencies(self):
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        self.from_currency.set(to_curr)
        self.to_currency.set(from_curr)
        self.status_label.config(text="🔄 Currencies swapped.")

    def log_history(self, text):
        self.history_box.config(state="normal")
        self.history_box.insert(tk.END, text + "\n")
        self.history_box.config(state="disabled")

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
