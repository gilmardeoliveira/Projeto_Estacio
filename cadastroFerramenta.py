import mysql.connector
from tkinter import *

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="capivara155",
    database="projetoestácio"
)


def valoresInseridosNoBancoDeDados():
    nomeDaFerramenta = nome.get()
    descricaoDaFerramenta = descricao.get()
    tamanhoDaFerramenta = tamanho.get()
    voltagemDaFerramenta = voltagem.get()
    unidadeDeMedida = medida.get()
    tipoDeFerramenta = tipo.get()
    materialDaFerramenta = material.get()
    fabricanteDaFerrament = fabricante.get()
    serial = serialNumber.get()

    cursor = conexao.cursor()

    cursor.execute("INSERT INTO ferramentas VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomeDaFerramenta, descricaoDaFerramenta, tamanhoDaFerramenta,
                                                  voltagemDaFerramenta, unidadeDeMedida, tipoDeFerramenta, materialDaFerramenta, fabricanteDaFerrament, serial))

    conexao.commit()


def registroDeFerramentas():
    global tela
    tela = Tk()

    tela.title("Formulário de registro de Ferramentas")

    tela.geometry("1000x1200")

    global nome
    global descricao
    global tamanho
    global voltagem
    global medida
    global tipo
    global material
    global fabricante
    global serialNumber

    nome = StringVar()
    descricao = StringVar()
    tamanho = StringVar()
    voltagem = StringVar()
    medida = StringVar()
    tipo = StringVar()
    material = StringVar()
    fabricante = StringVar()
    serialNumber = StringVar()

    Label(tela, width="300", text="Preencha os campos abaixo",
          bg="orange", fg="white").pack()

    Label(tela, text="Nome:").place(x=20, y=40)
    Entry(tela, textvariable=nome).place(x=90, y=42)

    Label(tela, text="Descrição:").place(x=20, y=80)
    Entry(tela, textvariable=descricao).place(x=90, y=82)

    Label(tela, text="Tamanho").place(x=20, y=120)
    Entry(tela, textvariable=tamanho).place(x=90, y=122)

    Label(tela, text="Voltagem").place(x=20, y=160)
    Entry(tela, textvariable=voltagem).place(x=90, y=162)

    Label(tela, text="Medida").place(x=20, y=200)
    Entry(tela, textvariable=medida).place(x=90, y=202)

    Label(tela, text="Tipo").place(x=20, y=240)
    Entry(tela, textvariable=tipo).place(x=90, y=242)

    Label(tela, text="Material").place(x=20, y=280)
    Entry(tela, textvariable=material).place(x=90, y=282)

    Label(tela, text="Fabricante").place(x=20, y=320)
    Entry(tela, textvariable=fabricante).place(x=90, y=322)

    Label(tela, text="Serial").place(x=20, y=360)
    Entry(tela, textvariable=serialNumber).place(x=90, y=362)

    Button(tela, text="Enter",  width=10, height=1, bg="orange",
           command=valoresInseridosNoBancoDeDados).place(x=105, y=400)
    tela.mainloop()


registroDeFerramentas()
