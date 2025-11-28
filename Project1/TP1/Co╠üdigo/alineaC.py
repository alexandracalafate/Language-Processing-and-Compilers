import re
import matplotlib.pyplot as plt
import os

def aC(arquivo_copia):
    try:
        # Abre o arquivo especificado para leitura
        with open(arquivo_copia, 'r') as copia:
            linhas = copia.readlines()  # Lê todas as linhas do arquivo
            frequencia = 0  # Inicializa o contador de frequência
            frequencia_cumulativa = []  # Lista para armazenar a frequência acumulativa

            # Itera sobre cada linha do arquivo
            for linha in linhas:
                campos = linha.strip().split("::")  # Divide a linha em campos usando "::" como delimitador
                if len(campos) >= 6:  # Verifica se há pelo menos 6 campos
                    observacoes = campos[5]  # Pega o campo de observações

                    # Verifica se a palavra 'Tio' está nas observações
                    if re.search(r'Tio', observacoes):
                        frequencia += 1  # Incrementa a frequência se 'Tio' for encontrado
                    frequencia_cumulativa.append(frequencia)  # Adiciona a frequência acumulada à lista

        return frequencia_cumulativa  # Retorna a lista de frequências cumulativas

    except FileNotFoundError:
        return f"O arquivo '{arquivo_copia}' não foi encontrado."  # Mensagem de erro caso o arquivo não seja encontrado
    except Exception as e:
        return f"Ocorreu um erro ao processar o arquivo: {str(e)}"  # Mensagem de erro genérica

# Função que cria o gráfico cumulativo e salva o resultado
def plot_cumulative_frequency(frequencia_cumulativa, path_texto):
    try:
        # Diretório para salvar o gráfico
        dir_imagens = r"C:\Users\Utilizador\Desktop\TP1\Imagens"
        path_imagem = os.path.join(dir_imagens, 'alineaC_cumulativo.png')  # Caminho completo da imagem a ser salva

        # Salvando o arquivo de texto com a frequência final
        with open(path_texto, 'w') as arquivo:
            arquivo.write(f"Frequência final de processos recomendados por Tio: {frequencia_cumulativa[-1]}\n")
            print(f"Frequência final de processos recomendados por Tio: {frequencia_cumulativa[-1]}")  # Imprime a frequência final no terminal

        # Criando o gráfico cumulativo
        plt.figure(figsize=(10, 6))  # Define o tamanho da figura
        plt.plot(frequencia_cumulativa, color='skyblue', marker='o', linestyle='-')  # Plota a frequência cumulativa
        plt.xlabel('Número de Linhas', fontsize=12)  # Rótulo do eixo X
        plt.ylabel('Frequência Cumulativa', fontsize=12)  # Rótulo do eixo Y
        plt.title('Frequência Cumulativa de Processos Recomendados por Tio', fontsize=14)  # Título do gráfico
        
        # Adicionando a frase no meio do gráfico
        freq_final = frequencia_cumulativa[-1]  # Frequência final
        plt.text(len(frequencia_cumulativa) / 2, freq_final / 2, 
                 f"Frequência final de processos recomendados por Tio: {freq_final}", 
                 fontsize=12, color='darkblue', ha='center', va='center')  # Adiciona texto ao gráfico

        plt.grid(True)  # Adiciona uma grade ao gráfico
        plt.tight_layout()  # Ajusta a disposição do gráfico
        plt.savefig(path_imagem)  # Salva o gráfico como imagem
        plt.close()  # Fecha a figura do gráfico
        print(f"Gráfico cumulativo salvo como '{path_imagem}'.")  # Mensagem de confirmação

    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")  # Mensagem de erro caso ocorra um erro de I/O
