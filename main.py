# Lista com os produtos comercializados
produtos = ["computador", "livro", "tablet", "celular",
            "tv", "ar condicionado", "cafeteira", "ar condicionado"]

# Lista com quantidade vendida e custo unitário
vendas = [
    [500, 2500],
    [40000, 50],
    [5000, 1000],
    [12000, 1600],
    [1000, 1800],
    [600, 1350],
    [1100, 350],
    [2300, 1200]
]

# Verifica se "livro" está na lista de produtos
if "livro" in produtos:
    # Obtém o índice do livro
    indice_livro = produtos.index("livro")

    # Cálculo do custo total dos livros antes do reajuste da alíquota
    qtde_livros = vendas[indice_livro][0]
    custo_unitario_livro = vendas[indice_livro][1]
    custo_total_livros = qtde_livros * custo_unitario_livro

    # Reajuste da alíquota (aumento de 10%)
    custo_unitario_livro = custo_unitario_livro * 1.1

    # Cálculo do novo custo total
    custo_total_livros_atualizado = qtde_livros * custo_unitario_livro

    # Impacto financeiro
    diferenca = custo_total_livros_atualizado - custo_total_livros

    diferenca = "R${:_.2}".format(diferenca)
    diferenca = diferenca.replace(".", ",").replace("_", ".")
    print("Com a reforma tributária, o impacto financeiro foi de {}.".format(diferenca))

else:
    print("Não há livros em nosso estoque.")
