import tkinter as tk

class PartialFractions(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Decompose", command=self.decompose)
        self.label = tk.Label(self, text="")

        self.entry.pack()
        self.button.pack()
        self.label.pack()

    def decompose(self):
        function = self.entry.get()
        a, b, c, d = self.parse_coefficients(function)
        if c == 0:
            self.label.config(text="The function cannot be decomposed.")
        else:
            fraction = "({}x + {}) / ({}x + {})".format(a, b, c, d)
            result = "{} = {} + ({} / {})".format(fraction, a/c, b, d)
            self.label.config(text=result)

    def parse_coefficients(self, function):
        terms = function.split(" ")
        a = float(terms[0]) if "x" in terms[0] else 0
        b = float(terms[2]) if terms[2] != "/" else 0
        c = float(terms[4]) if "x" in terms[4] else 0
        d = float(terms[6]) if terms[6] != "0" else 0
        return a, b, c, d

app = PartialFractions()
app.mainloop()
