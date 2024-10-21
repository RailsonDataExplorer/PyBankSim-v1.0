import tkinter as tk
from tkinter import messagebox, simpledialog

class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bancário")
        self.root.geometry("300x300")
        self.root.config(bg="#f0f0f0")

        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

        # Criação dos Widgets
        self.label_saldo = tk.Label(root, text=f"Saldo: R$ {self.saldo:.2f}", font=("Arial", 16), bg="#f0f0f0")
        self.label_saldo.pack(pady=20)

        self.button_depositar = tk.Button(root, text="Depositar", command=self.depositar, bg="#4CAF50", fg="white")
        self.button_depositar.pack(pady=5, padx=10, fill='x')

        self.button_sacar = tk.Button(root, text="Sacar", command=self.sacar, bg="#f44336", fg="white")
        self.button_sacar.pack(pady=5, padx=10, fill='x')

        self.button_extrato = tk.Button(root, text="Extrato", command=self.exibir_extrato, bg="#2196F3", fg="white")
        self.button_extrato.pack(pady=5, padx=10, fill='x')

        self.button_sair = tk.Button(root, text="Sair", command=root.quit, bg="#9E9E9E", fg="white")
        self.button_sair.pack(pady=5, padx=10, fill='x')

    def depositar(self):
        valor = self.entrada_valor("Informe o valor do depósito:")
        if valor is not None and valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            self.atualizar_saldo()
            messagebox.showinfo("Sucesso", f"Depósito realizado com sucesso!\nSaldo Atual: R$ {self.saldo:.2f}")
        else:
            messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")

    def sacar(self):
        valor = self.entrada_valor("Informe o valor do saque:")
        if valor is not None:
            if valor > self.saldo:
                messagebox.showerror("Erro", "Operação falhou! Você não tem saldo suficiente.")
            elif valor > self.limite:
                messagebox.showerror("Erro", "Operação falhou! O valor do saque excede o limite.")
            elif self.numero_saques >= self.LIMITE_SAQUES:
                messagebox.showerror("Erro", f"Operação falhou! Número máximo de saques excedido. Você pode realizar {self.LIMITE_SAQUES - self.numero_saques} saques.")
            elif valor > 0:
                self.saldo -= valor
                self.extrato += f"Saque: R$ {valor:.2f}\n"
                self.numero_saques += 1
                self.atualizar_saldo()
                messagebox.showinfo("Sucesso", f"Saque realizado com sucesso!\nSaldo Atual: R$ {self.saldo:.2f}")
            else:
                messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        if not self.extrato:
            extrato_display = "Não foram realizadas movimentações."
        else:
            extrato_display = self.extrato
        extrato_display += f"\nSaldo Atual: R$ {self.saldo:.2f}"
        messagebox.showinfo("Extrato", extrato_display)

    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo: R$ {self.saldo:.2f}")

    def entrada_valor(self, mensagem):
        valor = simpledialog.askfloat("Entrada", mensagem, minvalue=0)
        return valor

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
