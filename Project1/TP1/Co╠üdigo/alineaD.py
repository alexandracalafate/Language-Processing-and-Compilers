import pandas as pd

# Função para responder ao pedido da alínea D.
def aD(nome_arquivo):
    nomes = []  # Lista para armazenar os nomes dos confessados

    try:
        # Abre o arquivo especificado para leitura.
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            for linha in linhas:
                campos = linha.strip().split("::")  # Divide a linha em campos usando "::" como delimitador
                if len(campos) >= 6:  # Verifica se há pelo menos 6 campos
                    nome_completo_confessado = campos[2]  # Pega o nome completo do confessado
                    nomes.append(nome_completo_confessado)  # Adiciona o nome à lista

        # Remove duplicatas e organiza os nomes
        nomes_unicos = list(set(nomes))  # Converte a lista para um conjunto e depois de volta para lista para remover duplicatas

        # Ordena os nomes alfabeticamente
        nomes_unicos.sort()  # Ordena a lista de nomes

        # Imprimir resultados no terminal
        imprimir_resultados(nomes_unicos)  # Chama a função para imprimir os resultados

        # Salvar resultados em arquivo TXT
        salvar_resultados_txt(nomes_unicos)  # Chama a função para salvar os resultados em TXT

        # Gerar tabela em HTML
        gerar_tabela_html(nomes_unicos)  # Chama a função para gerar a tabela em HTML

    except FileNotFoundError:
        return f"O arquivo '{nome_arquivo}' não foi encontrado."  # Mensagem de erro caso o arquivo não seja encontrado
    except Exception as e:
        return f"Ocorreu um erro ao processar o arquivo: {str(e)}"  # Mensagem de erro genérica

# Função para imprimir os resultados no terminal
def imprimir_resultados(nomes):
    print("Resultados Alínea D - Nomes:")  # Título da seção
    for nome in nomes:
        print(nome)  # Imprime cada nome na lista

# Função para salvar os resultados em um arquivo TXT
def salvar_resultados_txt(nomes):
    caminho = r"C:\Users\Utilizador\Desktop\TP1\Ficheiros Texto\alineaD.txt"  # Caminho para o arquivo TXT
    with open(caminho, "w") as arquivo:
        for nome in nomes:
            arquivo.write(f"{nome}\n")  # Escreve cada nome em uma nova linha

# Função para gerar uma tabela HTML com os nomes
def gerar_tabela_html(nomes):
    # Definir o número de colunas
    num_colunas = 4  # Número de colunas que a tabela terá
    
    # Criar linhas para a tabela
    linhas = []  # Lista para armazenar as linhas da tabela
    for i in range(0, len(nomes), num_colunas):
        linha = nomes[i:i + num_colunas]  # Pega um grupo de nomes para a linha
        linhas.append(linha)  # Adiciona a linha à lista de linhas

    # Criar a tabela HTML
    tabela_html = "<table>"  # Início da tabela HTML
    for linha in linhas:
        tabela_html += "<tr>"  # Início de uma nova linha
        for nome in linha:
            tabela_html += f"<td>{nome}</td>"  # Adiciona o nome na célula da tabela
        tabela_html += "</tr>"  # Fim da linha
    tabela_html += "</table>"  # Fim da tabela

    # Criar um HTML completo com estilo
    html = f"""
    <html>
    <head>
        <style>
            table {{
                width: 100%; /* Largura total da tabela */
                border-collapse: collapse; /* Para evitar espaços entre as células */
            }}
            td {{
                border: 1px solid #ddd; /* Borda das células */
                padding: 8px; /* Espaçamento interno */
                text-align: center; /* Alinhamento do texto ao centro */
                width: {100 / num_colunas}%; /* Cada coluna ocupará uma fração da largura total */
            }}
        </style>
    </head>
    <body>
        <h2>Tabela de Nomes</h2>  <!-- Título da tabela -->
        {tabela_html}  <!-- Insere a tabela gerada -->
    </body>
    </html>
    """

    # Salvar o arquivo HTML
    caminho_html = r"C:\Users\Utilizador\Desktop\TP1\Imagens\tabela_alineaD.html"  # Caminho para o arquivo HTML
    with open(caminho_html, "w") as f:
        f.write(html)  # Escreve o HTML no arquivo

    print("Tabela HTML e arquivo TXT salvos com sucesso.")  # Mensagem de confirmação
