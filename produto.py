import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
from datetime import datetime

class Produto:
    def __init__(self, codigo, descricao, valorCompra, valorVenda, quantidade):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorCompra = valorCompra
        self.__valorVenda = valorVenda
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valorCompra(self):
        return self.__valorCompra
    
    @property
    def valorVenda(self):
        return self.__valorVenda
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def setQuantidade(self, quantidade):
        qtd = int(quantidade)
        self.__quantidade = qtd
    
    def getProduto(self):
        strg = "- Descrição: " + self.__descricao + "\n"
        strg += "- Valor de venda: " + str(self.__valorVenda) + "\n"
        strg += "- Quantidade em estoque: " + str(self.__quantidade)

        return strg
    
class ProdutoCadastra(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Produto")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameDes = tk.Frame(self)
        self.frameCmp = tk.Frame(self)
        self.frameVnd = tk.Frame(self)
        self.frameQtd = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack()
        self.frameDes.pack()
        self.frameCmp.pack()
        self.frameVnd.pack()
        self.frameQtd.pack()
        self.frameButton.pack()
      
        self.labelCod = tk.Label(self.frameCod,text="Cod: ")
        self.labelDes = tk.Label(self.frameDes,text="Descrição: ")
        self.labelCmp = tk.Label(self.frameCmp,text="Valor de compra: ")
        self.labelVnd = tk.Label(self.frameVnd,text="Valor de venda: ")
        self.labelQtd = tk.Label(self.frameQtd,text="Quantidade: ")
        self.labelCod.pack(side="left")
        self.labelDes.pack(side="left")
        self.labelCmp.pack(side="left")
        self.labelVnd.pack(side="left")
        self.labelQtd.pack(side="left")

        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")
        self.inputDes = tk.Entry(self.frameDes, width=20)
        self.inputDes.pack(side="left")
        self.inputCmp = tk.Entry(self.frameCmp, width=20)
        self.inputCmp.pack(side="left")
        self.inputVnd = tk.Entry(self.frameVnd, width=20)
        self.inputVnd.pack(side="left")
        self.inputQtd = tk.Entry(self.frameQtd, width=20)
        self.inputQtd.pack(side="left")
  
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastraProduto)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ProdutoBusca(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x50')
        self.title("Produto")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack()
        self.frameButton.pack()

        self.labelCod = tk.Label(self.frameCod,text="Código: ")
        self.labelCod.pack(side="left")

        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ProdutoFat(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x50')
        self.title("Produto")
        self.controle = controle

        self.frameCod = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack()
        self.frameButton.pack()

        self.labelCod = tk.Label(self.frameCod,text="Código: ")
        self.labelCod.pack(side="left")

        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaFatProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlProduto:
    def __init__(self, controlador):
        if not os.path.isfile("produtos.pickle"):
            self.listaProdutos =  []
        else:
            with open("produtos.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)
        self.controlador = controlador
    
    def salvaProdutos(self):
        if len(self.listaProdutos) != 0:
            with open("produtos.pickle","wb") as f:
                pickle.dump(self.listaProdutos, f)
    
    def insereProduto(self):
        self.limitePro = ProdutoCadastra(self) 
    
    def procuraProduto(self):
        self.limiteProBusca = ProdutoBusca(self) 
    
    def procuraFatProduto(self):
        self.limiteProFat = ProdutoFat(self)
    
    def cadastraProduto(self, event):
        cod = self.limitePro.inputCod.get()
        des = self.limitePro.inputDes.get()
        cmp = self.limitePro.inputCmp.get()
        vnd = self.limitePro.inputVnd.get()
        qtd = self.limitePro.inputQtd.get()
        if cod in self.getListaCodProdutos():
            self.limitePro.mostraJanela('Produto já cadastrado', 'Quantidade atualizada')
            for prod in self.listaProdutos:
                if prod.codigo == cod:
                    valor = int(prod.quantidade) + int(qtd)
                    prod.setQuantidade = valor
                    return
        produto = Produto(cod, des, cmp, vnd, qtd)
        self.listaProdutos.append(produto)
        self.limitePro.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
        self.clearHandler(event)
    
    def consultaProduto(self, event):
        cod = self.limiteProBusca.inputCod.get()
        for produto in self.listaProdutos:
            if produto.codigo == cod:
                str = produto.getProduto()
                self.limiteProBusca.mostraJanela('Produto', str)
                return
    
    def getProduto(self, cod):
        for produto in self.listaProdutos:
            if produto.codigo == cod:
                return produto
        return None
    
    def diminuiEstoque(self, cod, qtd):
        for prod in self.listaProdutos:
            if prod.codigo == cod:
                valor = int(prod.quantidade) - qtd 
                if valor >= 0:
                    prod.setQuantidade = valor
                    return True
                else:
                    return False

    def getListaCodProdutos(self):
        listaCod = []
        for produto in self.listaProdutos:
            listaCod.append(produto.codigo)
        return listaCod
        
    def calcularQuantidadeVendida(self):
        notas = self.controlador.ctrlVendas.getListaNotasFiscais()
        quantidade_vendida = {}

        for notaFiscal in notas:
            for venda in notaFiscal.listaVendas:
                produto = venda.produto
                if produto.codigo in quantidade_vendida:
                    quantidade_vendida[produto.codigo] += venda.quantidade
                else:
                    quantidade_vendida[produto.codigo] = venda.quantidade

        return quantidade_vendida
    
    def getTop10ProdutosMaisVendidos(self):
        quantidade_vendida = self.calcularQuantidadeVendida()

        top_produtos = sorted(quantidade_vendida.items(), key=lambda x: x[1], reverse=True)[:10]

        result_string = ""

        for codigo, quantidade in top_produtos:
            produto = self.controlador.ctrlProduto.getProduto(codigo)
            valor_total = int(quantidade) * float(produto.valorVenda)

            produto_string = f"Código: {produto.codigo}\n"
            produto_string += f"Descrição: {produto.descricao}\n"
            produto_string += f"Preço de Venda R$: {produto.valorVenda}\n"
            produto_string += f"Total Vendido R$: {valor_total}\n\n"

            result_string += produto_string

        self.mostraJanela("Produtos mais vendidos", result_string)

    def consultaFatProduto(self, event):
        codigo_produto = int(self.limiteProFat.inputCod.get())
        faturamento_total = 0

        notas = self.controlador.ctrlVendas.getListaNotasFiscais()
        print('codigo produto: ', codigo_produto, '\n')
        print(notas, '\n')
        for notaFiscal in notas:
            print("caiu for 1\n")
            for venda in notaFiscal.listaVendas:
                print("caiu for 2\n")
                produto = venda.produto  
                codFound = int(produto.codigo)
                if codFound == codigo_produto:
                    faturamento = float(produto.valorVenda) * int(venda.quantidade)
                    faturamento_total += faturamento


        if faturamento_total > 0:
            self.limiteProFat.mostraJanela('Faturamento', f'Faturamento total: R${faturamento_total}')
        else:
            self.limiteProFat.mostraJanela('Produto não encontrado', f'O produto com o código {codigo_produto} não foi encontrado.')

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def clearHandler(self, event):
        self.limitePro.inputCod.delete(0, len(self.limitePro.inputCod.get()))
        self.limitePro.inputDes.delete(0, len(self.limitePro.inputDes.get()))
        self.limitePro.inputCmp.delete(0, len(self.limitePro.inputCmp.get()))
        self.limitePro.inputVnd.delete(0, len(self.limitePro.inputVnd.get()))
        self.limitePro.inputQtd.delete(0, len(self.limitePro.inputQtd.get()))
    
    def fechaHandler(self, event):
        self.limitePro.destroy()