import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class Cliente:
    def __init__(self, nome, email, cpf):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def cpf(self):
        return self.__cpf
    
    def getCliente(self):
        str = "- Nome: " + self.__nome + "\n"
        str += "- E-mail: " + self.__email+ "\n"
        str += "- Cpf: " + self.__cpf

        return str

class ClienteCadastra(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cliente")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCpf = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameCpf.pack()
        self.frameEmail.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCpf = tk.Label(self.frameCpf,text="CPF: ")
        self.labelEmail = tk.Label(self.frameEmail,text="Email: ")
        self.labelNome.pack(side="left")
        self.labelCpf.pack(side="left")
        self.labelEmail.pack(side="left")    

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")
        self.inputCpf = tk.Entry(self.frameCpf, width=20)
        self.inputCpf.pack(side="left")
        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputEmail.pack(side="left")      
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastraCliente)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ClienteBusca(tk.Toplevel):
        def __init__(self, controle):

            tk.Toplevel.__init__(self)
            self.geometry('250x50')
            self.title("Cliente")
            self.controle = controle

            self.frameCpf = tk.Frame(self)
            self.frameButton = tk.Frame(self)
            self.frameCpf.pack()
            self.frameButton.pack()

            self.labelCpf = tk.Label(self.frameCpf,text="Cpf: ")
            self.labelCpf.pack(side="left")

            self.inputCpf = tk.Entry(self.frameCpf, width=20)
            self.inputCpf.pack(side="left")
        
            self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
            self.buttonSubmit.pack(side="left")
            self.buttonSubmit.bind("<Button>", controle.consultaCliente)

        def mostraJanela(self, titulo, msg):
            messagebox.showinfo(titulo, msg)

class ClienteBuscaData(tk.Toplevel):
        def __init__(self, controle):

            tk.Toplevel.__init__(self)
            self.geometry('250x50')
            self.title("Cliente")
            self.controle = controle

            self.frameCpf = tk.Frame(self)
            self.frameDataInicio = tk.Frame(self)
            self.frameDataFim = tk.Frame(self)
            self.frameButton = tk.Frame(self)
            self.frameCpf.pack()
            self.frameDataInicio.pack()
            self.frameDataFim.pack()
            self.frameButton.pack()

            self.labelCpf = tk.Label(self.frameCpf,text="Cpf: ")
            self.labelCpf.pack(side="left")
            self.labelDataInicio = tk.Label(self.frameDataInicio,text="Data Inicio: ")
            self.labelDataInicio.pack(side="left")
            self.labelDataFim = tk.Label(self.frameDataFim,text="Data Fim: ")
            self.labelDataFim.pack(side="left")

            self.inputCpf = tk.Entry(self.frameCpf, width=20)
            self.inputCpf.pack(side="left")
            self.inputDataInicio = tk.Entry(self.frameDataInicio, width=20)
            self.inputDataInicio.pack(side="left")
            self.inputDataFim = tk.Entry(self.frameDataFim, width=20)
            self.inputDataFim.pack(side="left")
        
            self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
            self.buttonSubmit.pack(side="left")
            self.buttonSubmit.bind("<Button>", controle.consultaVendasClientePeriodo)

        def mostraJanela(self, titulo, msg):
            messagebox.showinfo(titulo, msg)

class ClienteFat(tk.Toplevel):
        def __init__(self, controle):

            tk.Toplevel.__init__(self)
            self.geometry('250x50')
            self.title("Cliente")
            self.controle = controle

            self.frameCpf = tk.Frame(self)
            self.frameButton = tk.Frame(self)
            self.frameCpf.pack()
            self.frameButton.pack()

            self.labelCpf = tk.Label(self.frameCpf,text="Cpf: ")
            self.labelCpf.pack(side="left")

            self.inputCpf = tk.Entry(self.frameCpf, width=20)
            self.inputCpf.pack(side="left")
        
            self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
            self.buttonSubmit.pack(side="left")
            self.buttonSubmit.bind("<Button>", controle.consultaFaturamentoCliente)

        def mostraJanela(self, titulo, msg):
            messagebox.showinfo(titulo, msg)

class LimiteMostraEstudantes():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

class CtrlCliente:
    def __init__(self, controlador):
        if not os.path.isfile("cliente.pickle"):
            self.listaClientes =  []
        else:
            with open("cliente.pickle", "rb") as f:
                self.listaClientes = pickle.load(f)
        self.controlador = controlador

    def salvaClientes(self):
        if len(self.listaClientes) != 0:
            with open("cliente.pickle","wb") as f:
                pickle.dump(self.listaClientes, f)
        
    def insereCliente(self):
        self.limiteCli = ClienteCadastra(self) 
    
    def procuraCliente(self):
        self.limiteBsc = ClienteBusca(self) 

    def procuraClienteFat(self):
        self.limiteFat = ClienteFat(self) 

    def consultaVendasCliente(self):
        self.limiteVndCli = ClienteBuscaData(self)

    def cadastraCliente(self, event):
        nome = self.limiteCli.inputNome.get()
        cpf = self.limiteCli.inputCpf.get()
        email = self.limiteCli.inputEmail.get()
        cliente = Cliente(nome, email, cpf)
        self.listaClientes.append(cliente)
        self.limiteCli.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
        self.clearHandler(event)
    
    def consultaCliente(self, event):
        cpf = self.limiteBsc.inputCpf.get()
        for cliente in self.listaClientes:
            if cliente.cpf == cpf:
                str = cliente.getCliente()
                self.limiteBsc.mostraJanela('Sucesso', str)
                return
    
    def consultaFaturamentoCliente(self, event):
        cpf = self.limiteFat.inputCpf.get()
        notas = self.controlador.ctrlVendas.getListaNotasFiscais()
        
        faturamentoTotal = 0

        for cliente in self.listaClientes:
            if cliente.cpf == cpf:
                for nota in notas:
                    if nota.cliente == cpf:
                        for venda in nota.listaVendas:
                            produto = venda.produto
                            faturamento = float(produto.valorVenda) * int(venda.quantidade)
                            faturamentoTotal += faturamento

        if faturamentoTotal > 0:
            self.limiteFat.mostraJanela('Faturamento', f'Faturamento total: R${faturamentoTotal}')
        else:
            self.limiteFat.mostraJanela('Cliente não encontrado', f'O cliente com o cpf {cpf} não foi encontrado.')        

    def consultaVendasClientePeriodo(self, event):
        cpf = self.limiteVndCli.inputCpf.get()
        data_inicial = self.limiteVndCli.inputDataInicio.get()
        data_final = self.limiteVndCli.inputDataFim.get()

        vendas_cliente = self.controlador.ctrlVendas.consultaVendasClientePeriodo(cpf, data_inicial, data_final)

        if vendas_cliente:
            notas_fiscais = ""
            for nota in vendas_cliente:
                total_value = 0
                for venda in nota.listaVendas:
                    produto = venda.produto
                    quantity = venda.quantidade
                    value = produto.valorVenda
                    total_value += float(value) * int(quantity)
                notas_fiscais += f"Nota Fiscal: {nota.cliente} | Valor Total: R${total_value:.2f}\n"
            self.limiteVndCli.mostraJanela("Notas Fiscais", notas_fiscais)
        else:
            self.limiteVndCli.mostraJanela("Cliente não encontrado", f"O cliente com o cpf {cpf} não possui notas fiscais no período informado.")

    def clearHandler(self, event):
        self.limiteCli.inputNome.delete(0, len(self.limiteCli.inputNome.get()))
        self.limiteCli.inputCpf.delete(0, len(self.limiteCli.inputCpf.get()))
        self.limiteCli.inputEmail.delete(0, len(self.limiteCli.inputEmail.get()))

    def fechaHandler(self, event):
        self.limiteCli.destroy()

