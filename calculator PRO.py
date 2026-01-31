import tkinter as tk
from tkinter import ttk
import math

# =========================
# CALCULATOR PRO APP
# =========================
class CalculatorPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator PRO")
        self.root.geometry("360x520")
        self.root.resizable(False, False)

        self.expression = ""
        self.history = []

        self.build_ui()
        self.bind_keys()

    # =========================
    # UI
    # =========================
    def build_ui(self):
        self.root.configure(bg="#1e1e1e")

        # Display
        self.display_var = tk.StringVar()
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Segoe UI", 20),
            justify="right",
            bg="#2b2b2b",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        display.pack(fill="x", padx=10, pady=10, ipady=10)

        # History
        self.history_box = tk.Listbox(
            self.root,
            height=5,
            bg="#1e1e1e",
            fg="#aaaaaa",
            font=("Segoe UI", 9),
            selectbackground="#444444",
            relief="flat"
        )
        self.history_box.pack(fill="x", padx=10, pady=5)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(expand=True, fill="both", padx=5, pady=5)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sin", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("cos", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("sqrt", 3, 4),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3), ("^", 4, 4),
            ("←", 5, 0), ("=", 5, 1, 1, 4)
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            rowspan = btn[3] if len(btn) > 3 else 1
            colspan = btn[4] if len(btn) > 4 else 1

            tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 11),
                bg="#2b2b2b",
                fg="white",
                activebackground="#444444",
                activeforeground="white",
                relief="flat",
                command=lambda t=text: self.on_button_click(t)
            ).grid(
                row=row,
                column=col,
                rowspan=rowspan,
                columnspan=colspan,
                sticky="nsew",
                padx=4,
                pady=4
            )

        for i in range(6):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(5):
            btn_frame.columnconfigure(i, weight=1)

    # =========================
    # KEYBOARD SUPPORT
    # =========================
    def bind_keys(self):
        self.root.bind("<Return>", lambda e: self.on_button_click("="))
        self.root.bind("<BackSpace>", lambda e: self.on_button_click("←"))
        self.root.bind("<Escape>", lambda e: self.on_button_click("C"))

        for key in "0123456789+-*/.^":
            self.root.bind(key, lambda e, k=key: self.on_button_click(k))

    # =========================
    # BUTTON LOGIC
    # =========================
    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
        elif value == "←":
            self.expression = self.expression[:-1]
        elif value == "=":
            self.calculate()
            return
        elif value == "sin":
            self.expression += "sin("
        elif value == "cos":
            self.expression += "cos("
        elif value == "sqrt":
            self.expression += "sqrt("
        elif value == "^":
            self.expression += "**"
        else:
            self.expression += value

        self.display_var.set(self.expression)

    # =========================
    # CALCULATION
    # =========================
    def calculate(self):
        try:
            result = eval(
                self.expression,
                {"__builtins__": None},
                {
                    "sin": lambda x: math.sin(math.radians(x)),
                    "cos": lambda x: math.cos(math.radians(x)),
                    "sqrt": math.sqrt
                }
            )

            history_entry = f"{self.expression} = {result}"
            self.history.append(history_entry)
            self.history_box.insert(0, history_entry)

            self.expression = str(result)
            self.display_var.set(self.expression)

        except:
            self.display_var.set("Error")
            self.expression = ""

# =========================
# RUN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorPro(root)
    root.mainloop()
