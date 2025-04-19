import tkinter as tk
from tkinter import ttk, messagebox

class Calculatrice:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Variable pour stocker l'expression
        self.expression = ""
        
        # Créer une variable pour afficher le résultat
        self.text_input = tk.StringVar()
        self.text_input.set("0")
        
        # Créer la zone d'affichage
        self.display_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.display_frame.pack(expand=True, fill="both")
        
        self.display = tk.Entry(self.display_frame, font=("Arial", 24, "bold"),
                            textvariable=self.text_input, bd=5, insertwidth=4,
                            bg="#e8e8e8", justify="right")
        self.display.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Créer la zone des boutons
        self.buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Configurer la grille des boutons
        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)
        self.buttons_frame.columnconfigure(2, weight=1)
        self.buttons_frame.columnconfigure(3, weight=1)
        
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
        
        # Créer les boutons
        self.create_buttons()
    
    def create_buttons(self):
        # Première rangée
        self.create_button("C", 0, 0, bg="#ff9500", command=self.clear)
        self.create_button("⌫", 0, 1, bg="#ff9500", command=self.backspace)
        self.create_button("%", 0, 2, bg="#ff9500", command=lambda: self.append_to_expression("%"))
        self.create_button("/", 0, 3, bg="#ff9500", command=lambda: self.append_to_expression("/"))
        
        # Deuxième rangée
        self.create_button("7", 1, 0, command=lambda: self.append_to_expression("7"))
        self.create_button("8", 1, 1, command=lambda: self.append_to_expression("8"))
        self.create_button("9", 1, 2, command=lambda: self.append_to_expression("9"))
        self.create_button("*", 1, 3, bg="#ff9500", command=lambda: self.append_to_expression("*"))
        
        # Troisième rangée
        self.create_button("4", 2, 0, command=lambda: self.append_to_expression("4"))
        self.create_button("5", 2, 1, command=lambda: self.append_to_expression("5"))
        self.create_button("6", 2, 2, command=lambda: self.append_to_expression("6"))
        self.create_button("-", 2, 3, bg="#ff9500", command=lambda: self.append_to_expression("-"))
        
        # Quatrième rangée
        self.create_button("1", 3, 0, command=lambda: self.append_to_expression("1"))
        self.create_button("2", 3, 1, command=lambda: self.append_to_expression("2"))
        self.create_button("3", 3, 2, command=lambda: self.append_to_expression("3"))
        self.create_button("+", 3, 3, bg="#ff9500", command=lambda: self.append_to_expression("+"))
        
        # Cinquième rangée
        self.create_button("0", 4, 0, columnspan=2, command=lambda: self.append_to_expression("0"))
        self.create_button(".", 4, 2, command=lambda: self.append_to_expression("."))
        self.create_button("=", 4, 3, bg="#ff9500", command=self.calculate)
    
    def create_button(self, text, row, column, columnspan=1, bg="#ffffff", command=None):
        button = tk.Button(self.buttons_frame, text=text, font=("Arial", 16), 
                          bg=bg, fg="#000000", bd=1, relief="raised", command=command)
        button.grid(row=row, column=column, columnspan=columnspan, padx=2, pady=2, sticky="nsew")
        return button
    
    def append_to_expression(self, value):
        if self.expression == "0" and value.isdigit():
            self.expression = value
        else:
            self.expression += value
        self.text_input.set(self.expression)
    
    def clear(self):
        self.expression = ""
        self.text_input.set("0")
    
    def backspace(self):
        self.expression = self.expression[:-1]
        if not self.expression:
            self.expression = "0"
        self.text_input.set(self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.text_input.set(self.expression)
        except Exception as e:
            messagebox.showerror("Erreur", "Expression invalide")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculatrice(root)
    root.mainloop()