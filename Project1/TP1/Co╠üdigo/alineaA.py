import os
import matplotlib.pyplot as plt

# Função para calcular a frequência de processos por ano e organizar por século
def aA(nome_arquivo):
    # Dicionário para armazenar a frequência de anos por século
    frequencia_anos_por_seculo = {}

    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            for linha in linhas:
                campos = linha.strip().split("::")  # Divide a linha em campos
                if len(campos) >= 2:  # Verifica se há pelo menos 2 campos
                    data = campos[1]  # Obtém a data
                    ano = int(data.split("-")[0])  # Extrai o ano
                    seculo = (ano // 100 + 1)  # Calcula o século

                    # Inicializa o dicionário para o século, se ainda não existir
                    if seculo not in frequencia_anos_por_seculo:
                        frequencia_anos_por_seculo[seculo] = {}

                    # Atualiza a frequência do ano
                    if ano in frequencia_anos_por_seculo[seculo]:
                        frequencia_anos_por_seculo[seculo][ano] += 1
                    else:
                        frequencia_anos_por_seculo[seculo][ano] = 1

        return frequencia_anos_por_seculo  # Retorna o dicionário com a frequência

    except FileNotFoundError:
        return f"O arquivo '{nome_arquivo}' não foi encontrado."  # Mensagem de erro se o arquivo não for encontrado
    except Exception as e:
        return f"Ocorreu um erro ao processar o arquivo: {str(e)}"  # Mensagem de erro genérica

# Função que gera um gráfico de linha separado para cada século e os salva em uma pasta
def plot_alineaA_por_seculo(frequencia_anos_por_seculo, caminho_destino):
    for seculo, frequencias_anos in sorted(frequencia_anos_por_seculo.items()):
        anos = sorted(frequencias_anos.keys())  # Ordena os anos
        frequencias = [frequencias_anos[ano] for ano in anos]  # Obtém as frequências correspondentes

        # Configurações do gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(anos, frequencias, marker='o', color='b', linestyle='-')  # Plota os dados
        plt.xlabel('Ano')  # Rótulo do eixo X
        plt.ylabel('Frequência de Processos')  # Rótulo do eixo Y
        plt.title(f'Frequência de Processos no Século {seculo}')  # Título do gráfico
        plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo X
        plt.grid(True)  # Adiciona uma grade ao gráfico
        plt.tight_layout()  # Ajusta o layout

        # Salva o gráfico na pasta especificada
        caminho_grafico = os.path.join(caminho_destino, f'graficos_seculo_{seculo}.png')
        plt.savefig(caminho_grafico)  # Salva o gráfico
        plt.close()  # Fecha a figura atual
        print(f"Gráfico salvo como '{caminho_grafico}'")  # Imprime mensagem de confirmação

# Função que imprime os resultados e salva os gráficos
def print_alineaA(dados, nome_arquivo, caminho_destino):
    # Verifica se os dados são válidos
    if isinstance(dados, dict):  # Verifica se 'dados' é um dicionário
        try:
            with open(nome_arquivo, 'w') as arquivo:  # Abre o arquivo para escrita
                for seculo, frequencias_anos in sorted(dados.items()):
                    arquivo.write(f"Século {seculo}:\n")  # Escreve o século no arquivo
                    for ano, frequencia in sorted(frequencias_anos.items()):
                        linha = f"  Ano {ano}: {frequencia}"  # Formata a linha de resultado
                        print(linha)  # Imprime no terminal
                        arquivo.write(linha + "\n")  # Escreve a linha no arquivo
            print(f"Os resultados foram escritos no arquivo '{nome_arquivo}' e no terminal.")  # Mensagem de confirmação
        except IOError as e:
            print(f"Erro ao criar o arquivo '{nome_arquivo}': {e}")  # Mensagem de erro se falhar a criação do arquivo

        # Chama a função para gerar os gráficos
        plot_alineaA_por_seculo(dados, caminho_destino)
    else:
        # Se 'dados' não for um dicionário, imprime a mensagem de erro
        print(dados)  # Imprime a mensagem de erro retornada pela função aA
