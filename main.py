import tkinter as tk
import produto as pro
import cliente as cli
import vendas as ven

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('250x250')
        
        self.menubar = tk.Menu(self.root)
        self.produtoMenu = tk.Menu(self.menubar)
        self.clienteMenu = tk.Menu(self.menubar)
        self.vendasMenu = tk.Menu(self.menubar)

        self.produtoMenu.add_command(label='Cadastrar', command=self.controle.cadastraProduto)
        self.produtoMenu.add_command(label='Consultar', command=self.controle.consultaProduto)
        self.produtoMenu.add_command(label='Faturamento', command=self.controle.consultaFaturamentoProduto)
        self.produtoMenu.add_command(label='Mais vendidos', command=self.controle.consultaMaisVendidos)
        self.menubar.add_cascade(label='Produto', menu=self.produtoMenu)

        self.clienteMenu.add_command(label='Cadastrar', command=self.controle.cadastraCliente)
        self.clienteMenu.add_command(label='Consultar', command=self.controle.consultaCliente)
        self.clienteMenu.add_command(label='Faturamento', command=self.controle.consultaFaturamentoCliente)
        self.clienteMenu.add_command(label='Vendas para cliente', command=self.controle.consultaVendasCliente)
        self.menubar.add_cascade(label='Cliente', menu=self.clienteMenu)

        self.vendasMenu.add_command(label='Registrar Venda', command=self.controle.cadastraVenda)
        self.vendasMenu.add_command(label='Faturamento por período', command=self.controle.consultaFaturamentoPeriodo)
        self.vendasMenu.add_command(label='Lucro por período', command=self.controle.consultaLucroPeriodo)
        self.menubar.add_cascade(label='Vendas', menu=self.vendasMenu)

        self.menubar.add_command(label="Fechar", command=self.controle.fecharProg)

        self.root.config(menu=self.menubar)

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = pro.CtrlProduto(self)
        self.ctrlCliente = cli.CtrlCliente(self)
        self.ctrlVendas = ven.CtrlVendas(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Loja de confecções")

        self.root.mainloop()

    def cadastraProduto(self):
        self.ctrlProduto.insereProduto()

    def consultaProduto(self):
        self.ctrlProduto.procuraProduto()

    def consultaFaturamentoProduto(self):
        self.ctrlProduto.procuraFatProduto()

    def consultaMaisVendidos(self):
        self.ctrlProduto.getTop10ProdutosMaisVendidos()

    def cadastraCliente(self):
        self.ctrlCliente.insereCliente()

    def consultaCliente(self):
        self.ctrlCliente.procuraCliente()

    def consultaFaturamentoCliente(self):
        self.ctrlCliente.procuraClienteFat()

    def consultaVendasCliente(self):
        self.ctrlCliente.consultaVendasCliente()

    def cadastraVenda(self):
        self.ctrlVendas.inserirVenda()

    def consultaFaturamentoPeriodo(self):
        self.ctrlVendas.consultaFaturamentoPeriodo()

    def consultaLucroPeriodo(self):
        self.ctrlVendas.consultaLucroPeriodo()

    def fecharProg(self):
        self.ctrlProduto.salvaProdutos()
        self.ctrlCliente.salvaClientes()
        self.ctrlVendas.salvaNotasFiscais()
        self.root.destroy()

if __name__ == "__main__":
        c = ControlePrincipal()