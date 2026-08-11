import csv
 
# Arquivo onde os livros serão salvos
ARQUIVO = "livros.csv"

# Lista que guarda os livros em memória
livros = []
 
# Função para carregar os livros do arquivo
def carregar_livros():
    try:
        with open(ARQUIVO, newline="", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        pass  # Se o arquivo não existir, começa vazio
 
# Função para salvar os livros no arquivo
def salvar_livros():
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["titulo", "autor", "ano", "codigo", "status"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)
 
# Função para cadastrar um livro
def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    codigo = input("Código/ISBN: ")
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "codigo": codigo,
        "status": "disponível"
    }
    livros.append(livro)
    salvar_livros()
    print("Livro cadastrado com sucesso!")

# Função para listar todos os livros
def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) | Código: {livro['codigo']} | Status: {livro['status']}")

# Função para buscar livro por título ou autor
def buscar_livro():
    termo = input("Digite o título ou autor: ").lower()
    encontrados = [livro for livro in livros if termo in livro["titulo"].lower() or termo in livro["autor"].lower()]
    if encontrados:
        for livro in encontrados:
            print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) | Status: {livro['status']}")
    else:
        print("Nenhum livro encontrado.")