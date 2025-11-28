import json
import matplotlib.pyplot as plt

# alineaE.py
def aE(ficheiro):
    try:
        with open(ficheiro, 'r') as arquivo:
            linhas = arquivo.readlines()
            
            if len(linhas) > 1:  # Verifica se há pelo menos duas linhas (cabeçalho + registro)
                primeira_linha = linhas[1]  # Obtém a segunda linha (linha[0] é o cabeçalho)
                campo = primeira_linha.strip().split('::')  # Divide a linha em partes usando '::' como delimitador
                
                if len(campo) >= 6:
                    # Cria um dicionário com os campos do registro
                    registro = {
                        "numProc": campo[0],
                        "data": campo[1],
                        "confessado": campo[2],
                        "pai": campo[3],
                        "mae": campo[4],
                        "observacao": campo[5]
                    }
                    
                    # Salva o registro como PNG
                    json_output = json.dumps(registro, indent=4)  # Converte para JSON com indentação

                    # Criação da figura para o texto
                    plt.figure(figsize=(8, 4))
                    plt.text(0.5, 0.5, json_output, fontsize=12, ha='center', va='center', wrap=True)
                    plt.title('Formato JSON do 1º Registo', fontsize=14)  # Adiciona título à imagem
                    plt.axis('off')  # Desliga os eixos
                    
                    # Salva como PNG no diretório especificado com o nome 'alineaE.png'
                    plt.savefig(r'C:\Users\Utilizador\Desktop\TP1\Imagens\alineaE.png', bbox_inches='tight')  # Salva como PNG
                    plt.close()  # Fecha a figura

                    print("Informações salvas como 'C:\\Users\\Utilizador\\Desktop\\TP1\\Imagens\\alineaE.png'.")

                else:
                    print("A primeira linha apresenta número insuficiente de dados.")
            else:
                print("O arquivo está vazio.")
            return None

    except FileNotFoundError:
        return f"O arquivo '{ficheiro}' não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro ao processar o arquivo: {str(e)}"
