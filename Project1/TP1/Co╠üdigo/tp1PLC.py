import os
import re
from alineaA import aA, print_alineaA  # Funções da Alínea A
from alineaB import aB  # Função da Alínea B
from alineaC import aC, plot_cumulative_frequency  # Função da Alínea C
from alineaD import aD  # Função da Alínea D
from alineaE import aE  # Função da Alínea E

# Função para criar uma cópia do arquivo original sem registros repetidos
def criar_copia_sem_repetidos(arquivo_original, arquivo_copia):
    with open(arquivo_original, 'r') as original:
        linhas = original.readlines()

    sem_repetidos = set(linhas)
    linhas_sem_repetidos = list(sem_repetidos)

    with open(arquivo_copia, 'w') as copia:
        for linha in linhas_sem_repetidos:
            if not re.match(r'^NumProc::Data::Confessado::Pai::Mae::Observacoes::$', linha.strip()):
                copia.write(linha)

if __name__ == "__main__":
    # Caminhos para os arquivos e diretórios
    caminho_imagens = r"C:\Users\Utilizador\Desktop\TP1\Imagens"
    caminho_ficheiros = r"C:\Users\Utilizador\Desktop\TP1\Ficheiros Texto"
    arquivo_original = r"C:\Users\Utilizador\Desktop\TP1\processos.txt"
    arquivo_copia = r"C:\Users\Utilizador\Desktop\TP1\copia.txt"

    # Verifica se os diretórios existem; se não, cria-os
    os.makedirs(caminho_imagens, exist_ok=True)
    os.makedirs(caminho_ficheiros, exist_ok=True)

    # Cria uma cópia do arquivo original sem registros repetidos
    criar_copia_sem_repetidos(arquivo_original, arquivo_copia)

    # Executa as análises de cada alínea
    
    # Alínea A: Frequência de processos por ano e geração de gráficos por século
    dados_aA = aA(arquivo_copia)
    print_alineaA(dados_aA, os.path.join(caminho_ficheiros, "resultados_alineaA.txt"), caminho_imagens)
    
    # Alínea B: Geração de tabela HTML com nomes e apelidos
    aB(arquivo_copia)  # Chama a função da Alínea B, que já cuida da geração das tabelas HTML

    # Alínea C: Gráfico cumulativo da frequência de processos recomendados
    frequencia_cumulativa = aC(arquivo_copia)  # Obtém a frequência cumulativa
    path_texto = os.path.join(caminho_ficheiros, "resultado_alineaC.txt")  # Define o caminho do arquivo de texto
    if isinstance(frequencia_cumulativa, list):  # Verifica se o retorno é uma lista
        plot_cumulative_frequency(frequencia_cumulativa, path_texto)  # Chama a função de plotagem
    else:
        print(frequencia_cumulativa)  # Se não for uma lista, imprime a mensagem de erro
    
    # Alínea D: Processa os dados e gera arquivos TXT e HTML
    aD(arquivo_copia)
    
    # Alínea E: Visualiza e gera o gráfico para o primeiro registro do arquivo
    aE(arquivo_copia)

    print("Processamento completo. Arquivos e imagens foram gerados com sucesso.")
import os
import re
from alineaA import aA, print_alineaA  # Importa as funções da Alínea A
from alineaB import aB  # Importa a função da Alínea B
from alineaC import aC, plot_cumulative_frequency  # Importa as funções da Alínea C
from alineaD import aD  # Importa a função da Alínea D
from alineaE import aE  # Importa a função da Alínea E

# Função para criar uma cópia do arquivo original sem registos repetidos
def criar_copia_sem_repetidos(arquivo_original, arquivo_copia):
    # Abre o arquivo original para leitura
    with open(arquivo_original, 'r') as original:
        linhas = original.readlines()  # Lê todas as linhas do arquivo

    # Utiliza um conjunto para remover linhas duplicadas
    sem_repetidos = set(linhas)  
    linhas_sem_repetidos = list(sem_repetidos)  # Converte o conjunto de volta para uma lista

    # Abre o arquivo de cópia para escrita
    with open(arquivo_copia, 'w') as copia:
        for linha in linhas_sem_repetidos:
            # Filtra a linha que contém o cabeçalho
            if not re.match(r'^NumProc::Data::Confessado::Pai::Mae::Observacoes::$', linha.strip()):
                copia.write(linha)  # Escreve a linha no arquivo de cópia

if __name__ == "__main__":
    # Caminhos para os arquivos e diretórios
    caminho_imagens = r"C:\Users\Utilizador\Desktop\TP1\Imagens"  # Diretório para imagens
    caminho_ficheiros = r"C:\Users\Utilizador\Desktop\TP1\Ficheiros Texto"  # Diretório para arquivos texto
    arquivo_original = r"C:\Users\Utilizador\Desktop\TP1\processos.txt"  # Caminho do arquivo original
    arquivo_copia = r"C:\Users\Utilizador\Desktop\TP1\copia.txt"  # Caminho do arquivo de cópia

    # Verifica se os diretórios existem; se não, cria-os
    os.makedirs(caminho_imagens, exist_ok=True)
    os.makedirs(caminho_ficheiros, exist_ok=True)

    # Cria uma cópia do arquivo original sem registos repetidos
    criar_copia_sem_repetidos(arquivo_original, arquivo_copia)

    # Executa as análises de cada alínea
    
    # Alínea A: Frequência de processos por ano e geração de gráficos por século
    dados_aA = aA(arquivo_copia)  # Chama a função aA com o arquivo de cópia
    print_alineaA(dados_aA, os.path.join(caminho_ficheiros, "resultados_alineaA.txt"), caminho_imagens)
    
    # Alínea B: Geração de tabela HTML com nomes e apelidos
    aB(arquivo_copia)  # Chama a função da Alínea B, que gera as tabelas HTML

    # Alínea C: Gráfico cumulativo da frequência de processos recomendados
    frequencia_cumulativa = aC(arquivo_copia)  # Obtém a frequência cumulativa
    path_texto = os.path.join(caminho_ficheiros, "resultado_alineaC.txt")  # Define o caminho do arquivo de texto
    if isinstance(frequencia_cumulativa, list):  # Verifica se o retorno é uma lista
        plot_cumulative_frequency(frequencia_cumulativa, path_texto)  # Chama a função de plotagem
    else:
        print(frequencia_cumulativa)  # Se não for uma lista, imprime a mensagem de erro
    
    # Alínea D: Processa os dados e gera arquivos TXT e HTML
    aD(arquivo_copia)
    
    # Alínea E: Visualiza e gera o gráfico para o primeiro registo do arquivo
    aE(arquivo_copia)

    # Mensagem de conclusão do processamento
    print("Processamento completo. Arquivos e imagens foram gerados com sucesso.")
