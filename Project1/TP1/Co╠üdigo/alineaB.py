import pandas as pd

# Função para responder ao pedido da alínea B.
def aB(nome_arquivo):
    # Dicionários para armazenar a frequência de Nomes Próprios e Apelidos por século.
    nomes_proprios_seculo = {}
    apelidos_seculo = {}
    
    try:
        # Abre o arquivo especificado para leitura.
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                campos = linha.strip().split("::")
                if len(campos) >= 6:
                    data = campos[1]
                    if data != 'Data':
                        ano = int(data.split("-")[0])
                        seculo = (ano - 1) // 100 + 1

                        nome_completo_confessado = campos[2]
                        partes_nomes_confessado = nome_completo_confessado.split()
                        if len(partes_nomes_confessado) >= 2:
                            nome_proprio_confessado = partes_nomes_confessado[0]
                            if "," in partes_nomes_confessado:
                                apelido_partido = partes_nomes_confessado.split(",")
                                apelido_confessado = apelido_partido[0]
                            else:
                                apelido_confessado = partes_nomes_confessado[-1]

                            # Verifica se o século já existe nos dicionários.
                            if seculo not in nomes_proprios_seculo:
                                nomes_proprios_seculo[seculo] = {}
                            if seculo not in apelidos_seculo:
                                apelidos_seculo[seculo] = {}

                            # Atualiza a contagem de ocorrências.
                            nomes_proprios_seculo[seculo].setdefault(nome_proprio_confessado, 0)
                            apelidos_seculo[seculo].setdefault(apelido_confessado, 0)
                            nomes_proprios_seculo[seculo][nome_proprio_confessado] += 1
                            apelidos_seculo[seculo][apelido_confessado] += 1

                        # Repete para o pai.
                        nome_completo_pai = campos[3]
                        partes_nomes_pai = nome_completo_pai.split()
                        if len(partes_nomes_pai) >= 2:
                            nome_proprio_pai = partes_nomes_pai[0]
                            if "," in partes_nomes_pai:
                                apelido_pai_partido = partes_nomes_pai.split(",")
                                apelido_pai = apelido_pai_partido[0]
                            else:
                                apelido_pai = partes_nomes_pai[-1]
                            nomes_proprios_seculo[seculo].setdefault(nome_proprio_pai, 0)
                            apelidos_seculo[seculo].setdefault(apelido_pai, 0)
                            nomes_proprios_seculo[seculo][nome_proprio_pai] += 1
                            apelidos_seculo[seculo][apelido_pai] += 1

                        # Repete para a mãe.
                        nome_completo_mae = campos[4]
                        partes_nomes_mae = nome_completo_mae.split()
                        if len(partes_nomes_mae) >= 2:
                            nome_proprio_mae = partes_nomes_mae[0]
                            if "," in partes_nomes_mae:
                                apelido_mae_partido = partes_nomes_mae.split(",")
                                apelido_mae = apelido_mae_partido[0]
                            else:
                                apelido_mae = partes_nomes_mae[-1]
                            nomes_proprios_seculo[seculo].setdefault(nome_proprio_mae, 0)
                            apelidos_seculo[seculo].setdefault(apelido_mae, 0)
                            nomes_proprios_seculo[seculo][nome_proprio_mae] += 1
                            apelidos_seculo[seculo][apelido_mae] += 1

        # Imprimir resultados no terminal
        imprimir_resultados(nomes_proprios_seculo, apelidos_seculo)

        # Salvar resultados em arquivo TXT
        salvar_resultados_txt(nomes_proprios_seculo, apelidos_seculo)

        # Gerar tabelas em HTML
        gerar_tabelas_html(nomes_proprios_seculo, apelidos_seculo)

    except FileNotFoundError:
        return f"O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro ao processar o arquivo: {str(e)}"

def imprimir_resultados(nomes_proprios_seculo, apelidos_seculo):
    df_nomes = pd.DataFrame.from_dict({seculo: nomes for seculo, nomes in nomes_proprios_seculo.items()}, orient='index').fillna(0)
    df_apelidos = pd.DataFrame.from_dict({seculo: apelidos for seculo, apelidos in apelidos_seculo.items()}, orient='index').fillna(0)

    # Imprimindo no terminal
    print("Resultados Alínea B - Nomes Próprios:")
    print(df_nomes)
    print("\nResultados Alínea B - Apelidos:")
    print(df_apelidos)

def salvar_resultados_txt(nomes_proprios_seculo, apelidos_seculo):
    caminho = r"C:\Users\Utilizador\Desktop\TP1\Ficheiros Texto\resultados.txt"
    with open(caminho, "w") as arquivo:
        for seculo, nomes_seculo in nomes_proprios_seculo.items():
            arquivo.write(f"\nSéculo {seculo} - Nomes Próprios:\n")
            for nome, ocorrencias in nomes_seculo.items():
                arquivo.write(f"\t{nome} - {ocorrencias} ocorrência(s)\n")

            arquivo.write(f"\nSéculo {seculo} - Apelidos:\n")
            apelidos_seculo_seculo = apelidos_seculo.get(seculo, {})
            for apelido, ocorrencias in apelidos_seculo_seculo.items():
                arquivo.write(f"\t{apelido} - {ocorrencias} ocorrência(s)\n")

def gerar_tabelas_html(nomes_proprios_seculo, apelidos_seculo):
    # Criar listas para armazenar os dados
    dados_nomes = []
    dados_apelidos = []
    
    # Iterar pelos séculos e coletar dados
    for seculo in sorted(nomes_proprios_seculo.keys()):
        for nome, ocorrencias in nomes_proprios_seculo[seculo].items():
            dados_nomes.append([seculo, nome, ocorrencias])
        
        for apelido, ocorrencias in apelidos_seculo[seculo].items():
            dados_apelidos.append([seculo, apelido, ocorrencias])
    
    # Criar DataFrames
    df_nomes = pd.DataFrame(dados_nomes, columns=['Século', 'Nome Próprio', 'Ocorrências'])
    df_apelidos = pd.DataFrame(dados_apelidos, columns=['Século', 'Apelido', 'Ocorrências'])
    
    # Salvar as tabelas como HTML com estilo para barra de rolagem
    tabela_nomes_html = df_nomes.to_html(index=False, border=0, justify='center', classes='tabela-nomes')
    tabela_apelidos_html = df_apelidos.to_html(index=False, border=0, justify='center', classes='tabela-apelidos')

    # Criar um HTML completo com estilo
    html_nomes = f"""
    <html>
    <head>
        <style>
            .tabela-container {{
                max-height: 500px; /* Ajuste a altura máxima conforme necessário */
                overflow-y: auto; /* Adiciona barra de rolagem vertical */
                border: 1px solid #ccc; /* Borda da tabela */
                margin: 20px; /* Margem em volta da tabela */
                width: 100%; /* Largura total */
            }}
            table {{
                width: 100%; /* Largura total da tabela */
                border-collapse: collapse; /* Para evitar espaços entre as células */
            }}
            th, td {{
                border: 1px solid #ddd; /* Borda das células */
                padding: 8px; /* Espaçamento interno */
                text-align: left; /* Alinhamento do texto */
            }}
            th {{
                background-color: #f2f2f2; /* Cor de fundo dos cabeçalhos */
            }}
        </style>
    </head>
    <body>
        <h2>Tabela de Nomes Próprios</h2>
        <div class="tabela-container">
            {tabela_nomes_html}
        </div>
    </body>
    </html>
    """
    
    html_apelidos = f"""
    <html>
    <head>
        <style>
            .tabela-container {{
                max-height: 500px; /* Ajuste a altura máxima conforme necessário */
                overflow-y: auto; /* Adiciona barra de rolagem vertical */
                border: 1px solid #ccc; /* Borda da tabela */
                margin: 20px; /* Margem em volta da tabela */
                width: 100%; /* Largura total */
            }}
            table {{
                width: 100%; /* Largura total da tabela */
                border-collapse: collapse; /* Para evitar espaços entre as células */
            }}
            th, td {{
                border: 1px solid #ddd; /* Borda das células */
                padding: 8px; /* Espaçamento interno */
                text-align: left; /* Alinhamento do texto */
            }}
            th {{
                background-color: #f2f2f2; /* Cor de fundo dos cabeçalhos */
            }}
        </style>
    </head>
    <body>
        <h2>Tabela de Apelidos</h2>
        <div class="tabela-container">
            {tabela_apelidos_html}
        </div>
    </body>
    </html>
    """

    # Salvar os arquivos HTML
    with open(r"C:\Users\Utilizador\Desktop\TP1\Imagens\tabela_nomes_proprios.html", "w") as f_nomes:
        f_nomes.write(html_nomes)
        
    with open(r"C:\Users\Utilizador\Desktop\TP1\Imagens\tabela_apelidos.html", "w") as f_apelidos:
        f_apelidos.write(html_apelidos)

    print("Tabelas HTML salvas com sucesso.")
