import psycopg2
from tkinter import *

class AppBD:
    def __init__(self):
        print("Método Construtor")

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="capivara",
                                               host="127.0.0.1",
                                               port="5432",
                                               database="postgres")
        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)

    def selecionarDados(self):
        try:
            self.abrirConexao()  # tenta conectar ao banco de dados para selecionar dados
            cursor = self.connection.cursor()

            print("Selecionando todos as Ferramentas")
            sql_select_query = """select * from public."Ferramentas" """  # seleciona dados da tabela

            # executa o comando para selecionar dados da tabela
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()  # armazena os dados selecionados da tabela
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")

        return registros  # retorna os valores de selecionados da tabela

    # parâmetros que serão inseridos no banco de dados
    def inserirDados(self, id, descricao, fabricante, voltagem, numerodeserie, tamanho, medida, tipo, material, temporeservamax):
        try:
            self.abrirConexao()  # conexão com o banco de dados

            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO public."Ferramentas" ("ID", "DESCRICAO", "FABRICANTE", "VOLTAGEM", "NUMERODESERIE", "TAMANHO", "MEDIDA", "TIPO", "MATERIAL", "TEMPORESERVAMAX") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """  # comando para inserir os dados no banco de dados
            record_to_insert = (id, descricao, fabricante, voltagem,
                                numerodeserie, tamanho, medida, tipo, material, temporeservamax)  # parâmetros com os dados para serem inseridos
            # o cursor executa a variavel com o dados dos parâmetros no banco de dados
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()  # salva as alterações no banco de dados
            count = cursor.rowcount  # registra quais registros foram inseridos na tabela
            print(count, "Registro inserido com sucesso na tabela Ferramentas")

        except (Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao inserir registro na tabela Ferramentas")
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o Postgre foi fechada.")

    def atualizarDados(self, id, descricao, fabricante, voltagem, numerodeserie, tamanho, medida, tipo, material, temporeservamax):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro antes da Atualização")
            sql_select_query = """select * from public."Ferramentas" where "ID" = %s"""
            cursor.execute(sql_select_query, (id,))
            record = cursor.fetchone()
            print(record)

            sql_update_query = """Update public."Ferramentas" set "DESCRICAO" = %s, "FABRICANTE" = %s, "VOLTAGEM" = %s, "NUMERODESERIE" = %s, "TAMANHO" = %s, "MEDIDA" = %s, "TIPO" = %s, "MATERIAL" = %s, "TEMPORESERVAMAX" = %s where "ID" = %s"""
            cursor.execute(sql_update_query, (descricao, fabricante, voltagem,
                           numerodeserie, tamanho, medida, tipo, material, temporeservamax, id))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso")
            print("Registro depois da Att")
            sql_select_query = """select * from public."Ferramentas" where "ID" = %s"""
            cursor.execute(sql_select_query, (id,))
            record = cursor.fetchone()
            print(record)

        except (Exception, psycopg2.Error) as error:
            print("Erro na atualização", error)

        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("Conexão encerrada.")

    def excluirDados(self, id):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            sql_delete_query = """Delete from public."Ferramentas" where "ID" = %s"""
            cursor.execute(sql_delete_query, (id,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluido com sucesso")
        except (Exception, psycopg2.Error) as error:
            print("Erro na exclusão", error)

        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("Conexão encerrada")
