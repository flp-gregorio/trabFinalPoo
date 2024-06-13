# Projeto Loja de Confecções

## Descrição

Este projeto implementa uma aplicação de gerenciamento de uma loja de confecções utilizando a biblioteca `tkinter` para a interface gráfica. A aplicação permite o cadastro e consulta de produtos, clientes e vendas, além de fornecer relatórios de faturamento e itens mais vendidos.

## Funcionalidades

### Produtos
- **Cadastrar Produto**: Permite o cadastro de novos produtos na loja.
- **Consultar Produto**: Permite a consulta de produtos cadastrados.
- **Faturamento Produto**: Exibe o faturamento gerado por cada produto.
- **Mais Vendidos**: Exibe os 10 produtos mais vendidos.

### Clientes
- **Cadastrar Cliente**: Permite o cadastro de novos clientes.
- **Consultar Cliente**: Permite a consulta de clientes cadastrados.
- **Faturamento Cliente**: Exibe o faturamento gerado por cada cliente.
- **Vendas para Cliente**: Exibe as vendas realizadas para um cliente específico.

### Vendas
- **Registrar Venda**: Permite o registro de novas vendas.
- **Faturamento e Lucro por Período**: Exibe o faturamento e lucro por um período específico.

### Geral
- **Fechar**: Salva os dados e fecha a aplicação.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
├── produto.py
├── cliente.py
├── vendas.py
├── main.py (arquivo principal com o código da interface gráfica)
```

### Arquivos Principais

- **produto.py**: Contém a classe `CtrlProduto` responsável por gerenciar os produtos.
- **cliente.py**: Contém a classe `CtrlCliente` responsável por gerenciar os clientes.
- **vendas.py**: Contém a classe `CtrlVendas` responsável por gerenciar as vendas.
- **main.py**: Contém a interface gráfica e o controle principal da aplicação.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/loja-de-confeccoes.git
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd loja-de-confeccoes
   ```
3. Instale as dependências necessárias:
   ```sh
   pip install -r requirements.txt
   ```

## Execução

Para iniciar a aplicação, execute o arquivo `main.py`:
```sh
python main.py
```

## Autores

- Felipe Alves Gregório - 2022008250
- Nicolas de Sousa Moreira - 2022014472

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
