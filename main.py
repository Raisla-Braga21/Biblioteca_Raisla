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

# Função para emprestar livro
def emprestar_livro():
    codigo = input("Digite o código do livro: ")
    for livro in livros:
        if livro["codigo"] == codigo and livro["status"] == "disponível":
            livro["status"] = "emprestado"
            salvar_livros()
            print("Empréstimo registrado!")
            return
    print("Livro não encontrado ou já emprestado.")

# Função para devolver livro
def devolver_livro():
    codigo = input("Digite o código do livro: ")
    for livro in livros:
        if livro["codigo"] == codigo and livro["status"] == "emprestado":
            livro["status"] = "disponível"
            salvar_livros()
            print("Devolução registrada!")
            return
    print("Livro não encontrado ou não está emprestado.")

# Função para ordenar livros
def ordenar_livros():
    criterio = input("Ordenar por (titulo/autor/ano): ").lower()
    if criterio in ["titulo", "autor", "ano"]:
        ordenados = sorted(livros, key=lambda x: x[criterio])
        for livro in ordenados:
            print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) | Status: {livro['status']}")
    else:
        print("Critério inválido.")

# Programa principal
def main():
    carregar_livros()
    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Cadastrar livro")
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Listar livros")
        print("5. Buscar livro")
        print("6. Ordenar livros")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            emprestar_livro()
        elif opcao == "3":
            devolver_livro()
        elif opcao == "4":
            listar_livros()
        elif opcao == "5":
            buscar_livro()
        elif opcao == "6":
            ordenar_livros()
        elif opcao == "7":
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")
 
if __name__ == "__main__":
    main()
              