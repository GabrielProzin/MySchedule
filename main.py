import tkinter as tk
from tkinter import ttk

def main():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Minha Agenda")

    # Define tamanho da janela
    root.geometry("400x600")

    # Adiciona um rótulo de exemplo
    label = tk.Label(root, text="Bem-vindo à sua Agenda", font=("Arial", 14))
    label.pack(pady=20)

    # Mantém a janela aberta
    root.mainloop()

if __name__ == "__main__":
    main()
