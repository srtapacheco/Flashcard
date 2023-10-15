import tkinter as tk
import random

flashcards = []

def ler_flashcards_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            cartoes = conteudo.split("\n\n")
            for cartao in cartoes:
                partes = cartao.strip().split("\n")
                if len(partes) == 2:
                    pergunta, resposta = partes
                    flashcards.append((pergunta, resposta))
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")

def mostrar_flashcard():
    if flashcards:
        pergunta, resposta = random.choice(flashcards)
        pergunta_label.config(text=pergunta)
        resposta_label.config(text="")
    else:
        pergunta_label.config(text="Nenhum flashcard disponível")
        resposta_label.config(text="")

def mostrar_resposta():
    resposta = [card[1] for card in flashcards if card[0] == pergunta_label.cget("text")]
    if resposta:
        resposta_label.config(text=f"{', '.join(resposta)}")

def passar_para_proxima_pergunta():
    mostrar_flashcard()

app = tk.Tk()
app.title("Flashcards")

pergunta_label = tk.Label(app, text="", font=("Arial", 14))
pergunta_label.pack(pady=10)

resposta_label = tk.Label(app, text="", font=("Arial", 12))
resposta_label.pack()

mostrar_resposta_button = tk.Button(app, text="Mostrar Resposta", command=mostrar_resposta)
mostrar_resposta_button.pack()

botoes_frame = tk.Frame(app)
botoes_frame.pack(pady=10)

lembrar_button = tk.Button(botoes_frame, text="Lembro", command=passar_para_proxima_pergunta)
lembrar_button.pack(side="left")

nao_lembrar_button = tk.Button(botoes_frame, text="Não lembro", command=passar_para_proxima_pergunta)
nao_lembrar_button.pack(side="left")

ler_flashcards_do_arquivo("perguntas.txt")
mostrar_flashcard()

app.mainloop()
