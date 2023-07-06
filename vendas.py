import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class Venda:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    @property
    def produto(self):
        return self.__produto
    
    @property
    def quantidade(self):
        return self.__quantidade

class NotaFiscal:
    def __init__(self, cliente, listaVendas, data):
        self.__cliente = cliente
        self.__listaVendas = listaVendas
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def listaVendas(self):
        return self.__listaVendas
    
    @property
    def data(self):
        return self.__data

class NotaFiscalCadastra(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x200')
        self.title("Nota Fiscal")
        self.controle = controle

        self.descricao_var = tk.StringVar()
        self.quantidade_var = tk.StringVar()
        

        self.frameCliente = tk.Frame(self)
        self.frameData = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameQuantidade = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameDesc = tk.Frame(self)
        self.frameQuantidadeRestante = tk.Frame(self)
        self.frameCliente.pack()
        self.frameData.pack()
        self.frameProduto.pack()
        self.frameQuantidade.pack()
        self.frameButton.pack()
        self.frameDesc.pack()
        self.frameQuantidadeRestante.pack()

        self.labelCliente = tk.Label(self.frameCliente,text="CPF do cliente: ")
        self.labelData = tk.Label(self.frameData,text="Data da venda: ")
        self.labelCliente.pack(side="left")
        self.labelData.pack(side="left")
        self.labelProduto = tk.Label(self.frameProduto,text="Código do produto: ")
        self.labelQuantidade = tk.Label(self.frameQuantidade,text="Quantidade: ")
        self.labelProduto.pack(side="left")
        self.labelQuantidade.pack(side="left")
        self.labelDesc = tk.Label(self.frameDesc, text="Descrição: ")
        self.labelDescValue = tk.Label(self.frameDesc, textvariable=self.descricao_var)
        self.labelDesc.pack(side="left")
        self.labelDescValue.pack(side="left")
        self.labelQuantidadeRestante = tk.Label(self.frameQuantidadeRestante, text="Quantidade restante: ")
        self.labelQuantidadeRestanteValue = tk.Label(self.frameQuantidadeRestante, textvariable=self.quantidade_var)
        self.labelQuantidadeRestante.pack(side="left")
        self.labelQuantidadeRestanteValue.pack(side="left")

        self.inputCliente = tk.Entry(self.frameCliente, width=20)
        self.inputCliente.pack(side="left")
        self.inputData = tk.Entry(self.frameData, width=20)
        self.inputData.pack(side="left")
        self.inputProduto = tk.Entry(self.frameProduto, width=20)
        self.inputProduto.pack(side="left")
        self.inputQuantidade = tk.Entry(self.frameQuantidade, width=20)
        self.inputQuantidade.pack(side="left")

        self.buttonProcurar = tk.Button(self.frameButton, text="Procurar produto")
        self.buttonProcurar.pack(side="left")
        self.buttonProcurar.bind("<Button>", controle.getDesc)

        self.buttonCadastrar = tk.Button(self.frameButton, text="Cadastrar nota fiscal")
        self.buttonCadastrar.pack(side="left")
        self.buttonCadastrar.bind("<Button>", controle.cadastraNotaFiscal)

        self.buttonAdicionar = tk.Button(self.frameButton, text="Adicionar produto")
        self.buttonAdicionar.pack(side="left")
        self.buttonAdicionar.bind("<Button>", controle.adicionaProduto)

        self.buttonFechar = tk.Button(self.frameButton ,text="Fechar")
        self.buttonFechar.pack(side="left")
        self.buttonFechar.bind("<Button>", controle.fechaHandler)


        

    def atualiza(self, descricao, quantidade):
        self.descricao_var.set(descricao)
        self.quantidade_var.set(str(quantidade))

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
 
class ClienteFat(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x50')
        self.title("Produto")
        self.controle = controle

        self.frameCpf = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCpf.pack()
        self.frameButton.pack()

        self.labelCpf = tk.Label(self.frameCod,text="Cpf: ")
        self.labelCpf.pack(side="left")

        self.inputCpf = tk.Entry(self.frameCod, width=20)
        self.inputCpf.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaFatProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlVendas:
    def __init__(self, controle):
        if not os.path.isfile("notafiscais.pickle"):
            self.notasFiscais = []
        else:
            with open("notafiscais.pickle", "rb") as f:
                self.notasFiscais = pickle.load(f)
        self.controlador = controle
        self.listaVendas = []

    def salvaNotasFiscais(self):
        if len(self.notasFiscais) != 0:
            with open("notafiscais.pickle","wb") as f:
                pickle.dump(self.notasFiscais, f)
        
    def inserirVenda(self):
        self.viewNota = NotaFiscalCadastra(self)

    def procuraFatCliente(self):
        self.limiteCliFat = ClienteFat(self)
    
    def getNotasFiscais(self):
        notas = []
        for notaFiscal in self.notasFiscais:
            nota = {
                'cliente': notaFiscal.cliente,
                'listaVendas': [],
                'data': notaFiscal.data
            }
            for venda in notaFiscal.listaVendas:
                venda_info = {
                    'produto': {
                        'codigo': venda.produto.codigo,
                        'descricao': venda.produto.descricao,
                        'preco_venda': venda.produto.valorVenda
                    },
                    'quantidade': venda.quantidade
                }
                nota['listaVendas'].append(venda_info)
            notas.append(nota)
        return notas
    
    def getListaNotasFiscais(self):
        notasAux = []
        for nota in self.notasFiscais:
            notasAux.append(nota)
        return notasAux

    
    def cadastraNotaFiscal(self, event):
        print(self.listaVendas)
        listaAux = []
        for lista in self.listaVendas:
            listaAux.append(lista)
        nota = NotaFiscal(self.viewNota.inputCliente.get(), listaAux, self.viewNota.inputData.get())
        self.notasFiscais.append(nota)
        for produto in listaAux:
            self.controlador.ctrlProduto.diminuiEstoque(produto.produto.codigo, int(produto.quantidade))
        self.viewNota.mostraJanela('Sucesso', 'Nota fiscal cadastrada com sucesso')
    
    def consultaFatProduto(self, event):
        codigo_produto = int(self.limiteProFat.inputCod.get())
        faturamento_total = 0

        for notaFiscal in self.notasFiscais:
            for venda in notaFiscal.listaVendas:
                if venda.produto.codigo == codigo_produto:
                    faturamento = venda.produto.valorVenda * venda.quantidade
                    faturamento_total += faturamento

        self.limiteProFat.mostraJanela('Faturamento', f'Faturamento total: R${faturamento_total}')
    
    def consultaFatCliente(self, event):
        nome_cliente = self.limiteProFat.inputNome.get()
        faturamento_total = 0

        for notaFiscal in self.notasFiscais:
            if notaFiscal.cliente.nome == nome_cliente:
                for venda in notaFiscal.listaVendas:
                    faturamento = venda.produto.valorVenda * venda.quantidade
                    faturamento_total += faturamento

        self.limiteProFat.mostraJanela('Faturamento', f'Faturamento total: R${faturamento_total}')

    
    def adicionaProduto(self, event):
        id = self.viewNota.inputProduto.get()
        produto = self.controlador.ctrlProduto.getProduto(id)
        quantidade = int(self.viewNota.inputQuantidade.get())
        venda = Venda(produto, quantidade)
        self.listaVendas.append(venda)
        self.viewNota.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
        print(self.listaVendas)
        self.clearProdutos(self)
    
    def getDesc(self, event):
        id = self.viewNota.inputProduto.get()
        if(id in self.controlador.ctrlProduto.getListaCodProdutos()):
            produto = self.controlador.ctrlProduto.getProduto(id)
            self.viewNota.atualiza(produto.descricao, produto.quantidade)
        else:
            self.viewNota.mostraJanela('Erro', 'Digite um código válido')
    
    def consultaVendasClientePeriodo(self, cpf, data_inicial, data_final):
        notas_fiscais = self.getListaNotasFiscais()

        vendas_cliente = []
        for nota_fiscal in notas_fiscais:
            if nota_fiscal.cliente == cpf:
                data_nota = nota_fiscal.data
                if data_inicial <= data_nota <= data_final:
                    vendas_cliente.append(nota_fiscal)

        return vendas_cliente
    
    def clearProdutos(self):
        self.viewNota.inputProduto.delete(0, len(self.viewNota.inputProduto.get()))
        self.viewNota.inputQuantidade.delete(0, len(self.viewNota.inputQuantidade.get()))
    
    def consultarNotasFiscaisCliente(self, cliente):
        notasCliente = []
        for notaFiscal in self.__notasFiscais:
            if notaFiscal.cliente == cliente:
                notasCliente.append(notaFiscal)
        return notasCliente

    def fechaHandler(self, event):
        self.listaVendas.clear()
        self.viewNota.destroy()
