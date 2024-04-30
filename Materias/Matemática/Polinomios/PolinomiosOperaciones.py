import tkinter as tk
import numpy as np

class PolynomialApp:
    def __init__(self, master):
        self.master = master
        master.title("Operaciones con Polinomios")

        # Labels and entries for polynomial degrees
        self.degree_label1 = tk.Label(master, text="Grado del primer polinomio:")
        self.degree_label1.grid(row=0, column=0)
        self.degree_entry1 = tk.Entry(master)
        self.degree_entry1.grid(row=0, column=1)
        self.degree_entry1.bind("<Return>", lambda e: self.create_entries(self.degree_entry1, self.entries_frame1, self.update_poly_label1, True))

        # Frame for the first polynomial
        self.entries_frame1 = tk.Frame(master)
        self.entries_frame1.grid(row=2, column=0, columnspan=2)
        self.poly_label1 = tk.Label(master, text="Polinomio 1: ")
        self.poly_label1.grid(row=3, column=0, columnspan=2)

        # Separator
        self.separator = tk.Label(master, text="-------------------------------")
        self.separator.grid(row=4, column=0, columnspan=2)

        self.degree_label2 = tk.Label(master, text="Grado del segundo polinomio:")
        self.degree_label2.grid(row=5, column=0)
        self.degree_entry2 = tk.Entry(master)
        self.degree_entry2.grid(row=5, column=1)
        self.degree_entry2.bind("<Return>", lambda e: self.create_entries(self.degree_entry2, self.entries_frame2, self.update_poly_label2, True))

        # Frame for the second polynomial
        self.entries_frame2 = tk.Frame(master)
        self.entries_frame2.grid(row=6, column=0, columnspan=2)
        self.poly_label2 = tk.Label(master, text="Polinomio 2: ")
        self.poly_label2.grid(row=7, column=0, columnspan=2)

        # Operation buttons
        self.add_button = tk.Button(master, text="Sumar", command=self.add_polynomials)
        self.add_button.grid(row=8, column=0)
        self.subtract_button = tk.Button(master, text="Restar", command=self.subtract_polynomials)
        self.subtract_button.grid(row=8, column=1)
        self.multiply_button = tk.Button(master, text="Multiplicar", command=self.multiply_polynomials)
        self.multiply_button.grid(row=8, column=2)

        # Result label
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=9, column=0, columnspan=3)

    def create_entries(self, degree_entry, frame, update_func, clear_result=False):
        try:
            degree = int(degree_entry.get())
        except ValueError:
            degree_entry.config(bg='red')
            return
        else:
            degree_entry.config(bg='white')

        # Clear old entries
        for widget in frame.winfo_children():
            widget.destroy()

        # Optionally clear result
        if clear_result:
            self.result_label.config(text="")

        entries = []
        for i in range(degree + 1):
            entry = tk.Entry(frame, width=3)
            entry.pack(side=tk.LEFT)  # Pack side by side
            entry.bind("<KeyRelease>", lambda e, ufunc=update_func, ents=entries: ufunc(ents))
            entries.append(entry)

    def collect_coeffs(self, entries):
        return [float(entry.get()) for entry in entries[::-1] if entry.get() != '']

    def format_polynomial(self, coeffs):
        terms = []
        for power, coeff in enumerate(coeffs):
            if coeff != 0:
                term = f"{coeff}x^{power}" if power > 0 else f"{coeff}"
                terms.append(term)
        return " + ".join(reversed(terms)).replace('x^1', 'x').replace('+ -', '- ')

    def update_poly_label(self, entries, label):
        coeffs = self.collect_coeffs(entries)
        poly_string = self.format_polynomial(coeffs)
        label.config(text=f"{label.cget('text').split(':')[0]}: {poly_string}")

    def update_poly_label1(self, entries):
        self.update_poly_label(entries, self.poly_label1)

    def update_poly_label2(self, entries):
        self.update_poly_label(entries, self.poly_label2)

    def perform_operation(self, operation):
        coeffs1 = self.collect_coeffs(self.entries_frame1.winfo_children())
        coeffs2 = self.collect_coeffs(self.entries_frame2.winfo_children())
        poly1 = np.poly1d(coeffs1)
        poly2 = np.poly1d(coeffs2)
        result_poly = operation(poly1, poly2)
        result_coeffs = result_poly.coeffs[::-1]
        result_string = self.format_polynomial(result_coeffs)
        self.result_label.config(text=f"Resultado: {result_string}")

    def add_polynomials(self):
        self.perform_operation(lambda p1, p2: p1 + p2)

    def subtract_polynomials(self):
        self.perform_operation(lambda p1, p2: p1 - p2)

    def multiply_polynomials(self):
        self.perform_operation(lambda p1, p2: p1 * p2)

root = tk.Tk()
app = PolynomialApp(root)
root.mainloop()

