import tkinter as tk

class AkiPalavrasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AkiPalavras")
        self.lista1 = ["Abacaxi", "Melancia", "Girassol", "Computador", "Avião", "Chocolate",
                       "Caneta", "Montanha", "Livro", "Piano", "Trompeta", "Celular", "Bateria", "Tambor"]

        self.label = tk.Label(root, text="Bem-vindo ao AkiPalavras!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Mostrar Palavras", command=self.mostrar_palavras, font=("Arial", 14))
        self.start_button.pack(pady=10)

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_palavras(self):
        self.limpar_tela()

        self.label = tk.Label(self.root, text="Pense em uma destas palavras:", font=("Arial", 14))
        self.label.pack(pady=10)

        palavras = "\n".join(self.lista1)
        self.lista_label = tk.Label(self.root, text=palavras, font=("Arial", 12))
        self.lista_label.pack(pady=10)

        self.botao_comecar_perguntas = tk.Button(self.root, text="Começar Perguntas", command=self.pergunta1, font=("Arial", 14))
        self.botao_comecar_perguntas.pack(pady=10)

    def pergunta(self, texto, func_sim, func_nao):
        self.limpar_tela()
        self.label = tk.Label(self.root, text=texto, font=("Arial", 14))
        self.label.pack(pady=20)

        self.button_sim = tk.Button(self.root, text="Sim", command=func_sim, width=10, font=("Arial", 12))
        self.button_sim.pack(pady=5)

        self.button_nao = tk.Button(self.root, text="Não", command=func_nao, width=10, font=("Arial", 12))
        self.button_nao.pack(pady=5)

    def resultado(self):
        self.limpar_tela()
        if len(self.lista1) == 1:
            resposta = f"A sua palavra é {self.lista1[0]}!"
        else:
            resposta = f"A sua palavra é {', '.join(self.lista1)}?"
        self.label = tk.Label(self.root, text=resposta, font=("Arial", 16))
        self.label.pack(pady=20)

    def pergunta1(self):
        self.pergunta("A palavra tem relação com a natureza?", self.pergunta_natureza_sim, self.pergunta_natureza_nao)

    def pergunta_natureza_sim(self):
        for palavra in ["Caneta", "Livro", "Avião", "Piano", "Computador", "Trompeta", "Celular", "Tambor", "Bateria"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.pergunta2()

    def pergunta_natureza_nao(self):
        for palavra in ["Abacaxi", "Melancia", "Chocolate", "Girassol", "Montanha"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.pergunta6()

    def pergunta2(self):
        self.pergunta("Se trata de uma fruta?", self.pergunta2_sim, self.pergunta2_nao)

    def pergunta2_sim(self):
        for palavra in ["Chocolate", "Girassol", "Montanha"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.pergunta3()

    def pergunta2_nao(self):
        for palavra in ["Abacaxi", "Melancia"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.pergunta4()

    def pergunta3(self):
        self.pergunta("A fruta tem interior vermelho?", self.pergunta3_sim, self.pergunta3_nao)

    def pergunta3_sim(self):
        if "Abacaxi" in self.lista1:
            self.lista1.remove("Abacaxi")
        self.resultado()

    def pergunta3_nao(self):
        if "Melancia" in self.lista1:
            self.lista1.remove("Melancia")
        self.resultado()

    def pergunta4(self):
        self.pergunta("É um alimento?", self.pergunta4_sim, self.pergunta4_nao)

    def pergunta4_sim(self):
        for palavra in ["Girassol", "Montanha"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.resultado()

    def pergunta4_nao(self):
        if "Chocolate" in self.lista1:
            self.lista1.remove("Chocolate")
        self.pergunta5()

    def pergunta5(self):
        self.pergunta("Sua escolha pode ser escalada?", self.pergunta5_sim, self.pergunta5_nao)

    def pergunta5_sim(self):
        if "Girassol" in self.lista1:
            self.lista1.remove("Girassol")
        self.resultado()

    def pergunta5_nao(self):
        if "Montanha" in self.lista1:
            self.lista1.remove("Montanha")
        self.resultado()

    def pergunta6(self):
        self.pergunta("Possui algo relacionado a tecnologia?", self.pergunta6_sim, self.pergunta6_nao)

    def pergunta6_sim(self):
        for palavra in ["Caneta", "Livro", "Piano", "Trompeta"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.pergunta9()

    def pergunta6_nao(self):
        for palavra in ["Computador", "Avião", "Celular"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.pergunta7()

    def pergunta7(self):
        self.pergunta("A palavra gera melodia?", self.pergunta7_sim, self.pergunta7_nao)

    def pergunta7_sim(self):
        for palavra in ["Caneta", "Livro"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.pergunta10()

    def pergunta7_nao(self):
        for palavra in ["Piano", "Trompeta", "Bateria", "Tambor"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.pergunta8()

    def pergunta8(self):
        self.pergunta("Pode ser usado para escrever?", self.pergunta8_sim, self.pergunta8_nao)

    def pergunta8_sim(self):
        if "Livro" in self.lista1:
            self.lista1.remove("Livro")
        self.resultado()

    def pergunta8_nao(self):
        if "Caneta" in self.lista1:
            self.lista1.remove("Caneta")
        self.resultado()

    def pergunta9(self):
        self.pergunta("É usado como transporte?", self.pergunta9_sim, self.pergunta9_nao)

    def pergunta9_sim(self):
        for palavra in ["Computador", "Celular"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.resultado()

    def pergunta9_nao(self):
        if "Avião" in self.lista1:
            self.lista1.remove("Avião")
        self.pergunta11()

    def pergunta10(self):
        self.pergunta("É um instrumento de sopro?", self.pergunta10_sim, self.pergunta10_nao)

    def pergunta10_sim(self):
        for palavra in ["Piano", "Bateria", "Tambor"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.resultado()

    def pergunta10_nao(self):
        if "Trompeta" in self.lista1:
            self.lista1.remove("Trompeta")
        self.pergunta_baqueta()

    def pergunta_baqueta(self):
        self.pergunta("É tocado por baquetas?", self.pergunta_baqueta_sim, self.pergunta_baqueta_nao)

    def pergunta_baqueta_sim(self):
        if "Piano" in self.lista1:
            self.lista1.remove("Piano")
        self.pergunta_pratos()

    def pergunta_baqueta_nao(self):
        for palavra in ["Tambor", "Bateria"]:
            if palavra in self.lista1:
                self.lista1.remove(palavra)
        self.resultado()

    def pergunta_pratos(self):
        self.pergunta("Possui pratos?", self.pergunta_pratos_sim, self.pergunta_pratos_nao)

    def pergunta_pratos_sim(self):
        if "Tambor" in self.lista1:
            self.lista1.remove("Tambor")
        self.resultado()

    def pergunta_pratos_nao(self):
        if "Bateria" in self.lista1:
            self.lista1.remove("Bateria")
        self.resultado()

    def pergunta11(self):
        self.pergunta("Sua escolha cabe no bolso?", self.pergunta11_sim, self.pergunta11_nao)

    def pergunta11_sim(self):
        if "Computador" in self.lista1:
            self.lista1.remove("Computador")
        self.resultado()

    def pergunta11_nao(self):
        if "Celular" in self.lista1:
            self.lista1.remove("Celular")
        self.resultado()

if __name__ == "__main__":
    root = tk.Tk()
    app = AkiPalavrasApp(root)
    root.mainloop()