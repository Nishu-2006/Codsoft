from tkinter import Tk, Button, Entry, StringVar, messagebox, Frame

# --- Core Calculator Functions ---
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculate(operation, num1, num2):
    if operation == 'add':
        return add(num1, num2)
    elif operation == 'subtract':
        return subtract(num1, num2)
    elif operation == 'multiply':
        return multiply(num1, num2)
    elif operation == 'divide':
        return divide(num1, num2)
    else:
        return "Invalid operation"

# --- GUI Class ---
class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.resizable(False, False)
        master.configure(bg="#ffe4e1")

        self.expression = ""
        self.input_text = StringVar()

        # Display
        self.input_frame = Frame(master, bg="#ffe4e1")
        self.input_frame.pack(pady=10)
        self.input_field = Entry(
            self.input_frame, textvariable=self.input_text,
            font=('Arial', 18, 'bold'), bd=5, relief='ridge',
            justify='right', width=20, bg="#fffacd", fg="#8b0000"
        )
        self.input_field.grid(row=0, column=0)
        self.input_field.bind("<Key>", self.on_key_press)

        # Buttons
        self.btns_frame = Frame(master, bg="#ffe4e1")
        self.btns_frame.pack()
        button_colors = {'/': "#87ceeb", '*': "#87ceeb", '-': "#87ceeb", '+': "#87ceeb", '=': "#32cd32", 'C': "#ff6347"}
        default_bg = "#fafad2"

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            btn = Button(
                self.btns_frame, text=text, width=5, height=2,
                font=('Arial', 14, 'bold'), bd=2, relief='ridge',
                bg=button_colors.get(text, default_bg),
                fg="#fff" if text in button_colors else "#333",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

        for i in range(4):
            self.btns_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            self.calculate_expression()
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def on_key_press(self, event):
        key = event.char
        if key in '0123456789.+-*/':
            self.expression += key
            self.input_text.set(self.expression)
            return "break"
        elif key == '\r':  # Enter key
            self.calculate_expression()
            return "break"
        elif key == '\x08':  # Backspace
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
            return "break"

    def calculate_expression(self):
        try:
            # Simple support for 2-operand backend function usage
            tokens = self.expression.replace(' ', '')
            for op in ['+', '-', '*', '/']:
                if op in tokens:
                    parts = tokens.split(op)
                    if len(parts) == 2:
                        num1 = float(parts[0])
                        num2 = float(parts[1])
                        operation = {'+': 'add', '-': 'subtract', '*': 'multiply', '/': 'divide'}[op]
                        result = calculate(operation, num1, num2)
                        self.input_text.set(result)
                        self.expression = str(result)
                        return

            # fallback to eval for longer expressions
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression\n{e}")
            self.input_text.set("")
            self.expression = ""

# --- Start Application ---
if __name__ == "__main__":
    root = Tk()
    calculator = CalculatorGUI(root)
    root.mainloop()