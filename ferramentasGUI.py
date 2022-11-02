# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import *
import ferramentas as ferramentas

class PrincipalBD:
    def __init__(self, win):
        self.objBD = ferramentas.AppBD()

        # Entrada de dados para os botões


        self.lbId = tk.Label(win, text="Id da Ferramenta:")
        self.lbDescricao = tk.Label(win, text="Descricão da Ferramenta:")
        self.lbFabricante = tk.Label(win, text="Fabricante:")
        self.lbVoltagem = tk.Label(win, text="Voltagem:")
        self.lbNumeroDeSerie = tk.Label(win, text="Numero de Série:")
        self.lbTamanho = tk.Label(win, text="Tamanho:")
        self.lbMedida = tk.Label(win, text="Medida:")
        self.lbTipo = tk.Label(win, text="Tipo de Ferramenta:")
        self.lbMaterial = tk.Label(
            win, text="Material:")
        self.lbTempoReservaMax = tk.Label(win, text="Tempo de Reserva:")
        
        self.txtId = tk.Entry(bd=3)
        self.txtDesc = tk.Entry()
        self.txtFab = tk.Entry()
        self.txtVolt = tk.Entry()
        self.txtNumSerie = tk.Entry()
        self.txtTam = tk.Entry()
        self.txtMedida = tk.Entry()
        self.txtTipo = tk.Entry()
        self.txtMaterial = tk.Entry()
        self.txtTempoReserva = tk.Entry()


        self.btnCadastrar = tk.Button(
            win, text="Cadastrar", command=self.fCadastrarFerramenta)
        self.btnAtualizar = tk.Button(
            win, text="Atualizar", command=self.fAtualizarFerramenta)
        self.btnExcluir = tk.Button(
            win, text="Excluir", command=self.fExcluirFerramenta)
        self.btnLimpar = tk.Button(
            win, text="Limpar", command=self.fLimparTela)

        self.dadosColunas = ("Id", "Descricao", "Fabricante", "Voltagem",
                             "NumeroSerie", "Tamanho", "Medida", "Tipo", "Material", "TempoReserva")

        # TreeView

        self.treeProdutos = ttk.Treeview(
            win, columns=self.dadosColunas, selectmode="browse")

        self.verscrlbar = ttk.Scrollbar(
            win, orient="vertical", command=self.treeProdutos.yview)
        self.verscrlbar.pack(side="right", fill="x")

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProdutos.heading("Id", text="Id")
        self.treeProdutos.heading("Descricao", text="Descrição")
        self.treeProdutos.heading("Fabricante", text="Fabricante")
        self.treeProdutos.heading("Voltagem", text="Voltagem")
        self.treeProdutos.heading("NumeroSerie", text="NumeroSerie")
        self.treeProdutos.heading("Tamanho", text="Tamanho")
        self.treeProdutos.heading("Medida", text="Medida")
        self.treeProdutos.heading("Tipo", text="Tipo")
        self.treeProdutos.heading("Material", text="Material")
        self.treeProdutos.heading("TempoReserva", text="TempoReserva")

        self.treeProdutos.column("Id", minwidth=0, width=100)
        self.treeProdutos.column("Descricao", minwidth=0, width=100)
        self.treeProdutos.column("Fabricante", minwidth=0, width=100)
        self.treeProdutos.column("Voltagem", minwidth=0, width=100)
        self.treeProdutos.column("NumeroSerie", minwidth=0, width=100)
        self.treeProdutos.column("Tamanho", minwidth=0, width=100)
        self.treeProdutos.column("Medida", minwidth=0, width=100)
        self.treeProdutos.column("Tipo", minwidth=0, width=100)
        self.treeProdutos.column("Material", minwidth=0, width=100)
        self.treeProdutos.column("TempoReserva", minwidth=0, width=100)

        self.treeProdutos.pack(padx=10, pady=10)

        self.treeProdutos.bind("<<TreeviewSelect>>",
                               self.apresentarRegistrosSelecionados)

        # Posicionamento dos componentes

        self.lbId.place(x=100, y=50)
        self.txtId.place(x=250, y=50)

        self.lbDescricao.place(x=100, y=100)
        self.txtDesc.place(x=250, y=100)

        self.lbFabricante.place(x=100, y=150)
        self.txtFab.place(x=250, y=150)

        self.lbVoltagem.place(x=100, y=200)
        self.txtVolt.place(x=250, y=200)

        self.lbNumeroDeSerie.place(x=100, y=250)
        self.txtNumSerie.place(x=250, y=250)

        self.lbTamanho.place(x=100, y=300)
        self.txtTam.place(x=250, y=300)

        self.lbMedida.place(x=100, y=350)
        self.txtMedida.place(x=250, y=350)

        self.lbTipo.place(x=100, y=400)
        self.txtTipo.place(x=250, y=400)

        self.lbMaterial.place(x=100, y=450)
        self.txtMaterial.place(x=250, y=450)

        self.lbTempoReservaMax.place(x=100, y=500)
        self.txtTempoReserva.place(x=250, y=500)

        self.btnCadastrar.place(x=100, y=540)
        self.btnAtualizar.place(x=200, y=540)
        self.btnExcluir.place(x=300, y=540)
        self.btnLimpar.place(x=400, y=540)

        self.treeProdutos.place(x=100, y=600)
        self.verscrlbar.place(x=1283, y=525, height=200)
        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva = item[
                "values"][0:10]
            self.txtId.insert(0, id1)
            self.txtDesc.insert(0, descricao)
            self.txtFab.insert(0, fabricacao)
            self.txtVolt.insert(0, voltagem)
            self.txtNumSerie.insert(0, numSerie)
            self.txtTam.insert(0, tamanho)
            self.txtMedida.insert(0, medida)
            self.txtTipo.insert(0, tipo)
            self.txtMaterial.insert(0, material)
            self.txtTempoReserva.insert(0, tempoReserva)

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionarDados()
            print("Dados disponíveis no Banco de Dados")
            for item in registros:
                id1 = item[0]
                descricao = item[1]
                fabricacao = item[2]
                voltagem = item[3]
                numSerie = item[4]
                tamanho = item [5]
                medida = item[6]
                tipo = item[7]
                material = item[8]
                tempoReserva = item[9]

                print("Id = ", id1)
                print("Descrição = ", descricao)
                print("Fabricação = ", fabricacao)
                print("Voltagem =", voltagem)
                print("Número de Série = ", numSerie)
                print("Tamanho = ", tamanho)
                print("Medida = ", medida)
                print("Tipo = ", tipo)
                print("Material = ", material)
                print("Tempo de Reserva", tempoReserva)

                self.treeProdutos.insert("", "end", iid=self.iid, values=(
                    id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva))

                self.iid = self.iid + 1
                self.id = self.id + 1

            print("Dados da Base")
        except:
            print("Ainda não existem dados para carregar")

    def fLerCampos(self):
        try:
            print("Dados disponíveis")

            id1 = int(self.txtId.get())
            print("Id", id1)

            descricao = self.txtDesc.get()
            print("Descrição", descricao)

            fabricacao = self.txtFab.get()
            print("Fabricacao", fabricacao)

            voltagem = self.txtVolt.get()
            print("Voltagem", voltagem)

            numSerie = self.txtNumSerie.get()
            print("Numero de Série", numSerie)

            tamanho = self.txtTam.get()
            print("Tamanho", tamanho)

            medida = self.txtMedida.get()
            print("Medida", medida)

            tipo = self.txtTipo.get()
            print("Tipo", tipo)

            material = self.txtMaterial.get()
            print("Material", material)

            tempoReserva = int(self.txtTempoReserva.get())
            print("Tempo de Reserva", tempoReserva)

            print("Leitura de dados realizada com sucesso")

        except:
            print("Não foi possível realizar a leitura dos dados")

        return id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva

    def fCadastrarFerramenta(self):
        try:
            print("Dados disponíveis")
            id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva = self.fLerCampos()

            self.objBD.inserirDados(
                id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva)

            self.treeProdutos.insert("", "end", iid=self.iid, values=(
                id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva))

            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print("Ferramenta Cadastrada.")
        except:
            print("Não foi possível realizar o cadastro.")

    def fAtualizarFerramenta(self):
        try:
            print("Dados disponíveis")
            id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva = self.fLerCampos()
            self.objBD.atualizarDados(
                id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva)

            self.treeProdutos.delete(*self.treeProdutos.get_children())

            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Ferramenta Atualizada")

        except:
            print("Não foi possível realizar a atualização")

    def fExcluirFerramenta(self):
        try:
            print("Dados disponíveis")
            id1, descricao, fabricacao, voltagem, numSerie, tamanho, medida, tipo, material, tempoReserva = self.fLerCampos()
            self.objBD.excluirDados(id1)

            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Ferramenta excluída.")

        except:
            print("Não foi possível realizar a exclusão da ferramenta.")

    def fLimparTela(self):
        try:
            print("Dados disponíveis")
            self.txtId.delete(0, tk.END)
            self.txtDesc.delete(0, tk.END)
            self.txtFab.delete(0, tk.END)
            self.txtVolt.delete(0, tk.END)
            self.txtNumSerie.delete(0, tk.END)
            self.txtTam.delete(0, tk.END)
            self.txtMedida.delete(0, tk.END)
            self.txtTipo.delete(0, tk.END)
            self.txtMaterial.delete(0, tk.END)
            self.txtTempoReserva.delete(0, tk.END)

            print("Campos limpos.")

        except:
            print("Não foi possível limpar os campos")

janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Bem vindo a aplicação")
janela.geometry("1500x1000+10+10")
janela.mainloop()
