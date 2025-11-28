# Importa a biblioteca os para manipulação de arquivos
import os

# Caminhos das imagens e arquivos HTML
caminho_imagens = r"./Imagens"
caminho_imagem_info = r"./info.png"  # Caminho da imagem de informações
imagens_a = [
    "graficos_seculo_17.png",
    "graficos_seculo_18.png",
    "graficos_seculo_19.png",
    "graficos_seculo_20.png",
]
imagem_c = "alineaC_cumulativo.png"
html_b = [
    "tabela_apelidos.html",
    "tabela_nomes_proprios.html"
]
html_d = "tabela_alineaD.html"

# Cria a página HTML principal
html_content_principal = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trabalho Prático 1</title>
    <style>
        body {{
            background-image: url('https://navigate360.com/wp-content/uploads/2021/03/NLP-image.png');
            background-size: cover;
            text-align: center;
            color: white;
        }}
        h1 {{
            margin-top: 50px;
            font-size: 3em;
            color: black; /* Altera a cor do título para preto */
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            margin: 20px;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }}
        .button:hover {{
            background-color: rgba(0, 0, 0, 0.9);
        }}
        .button-container {{
            margin-top: 20%; /* Move os botões 15% abaixo do centro */
        }}
        .enunciado-button {{
            position: absolute; /* Posiciona o botão */
            top: 20px; /* Distância do topo */
            left: 20px; /* Distância da esquerda */
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            text-decoration: none;
        }}
        .enunciado-button:hover {{
            background-color: rgba(0, 0, 0, 0.9);
        }}
        .new-tab-button {{
            position: absolute; /* Posiciona o botão no canto superior direito */
            top: 20px; /* Distância do topo */
            right: 20px; /* Distância da direita */
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            text-decoration: none;
        }}
        .new-tab-button:hover {{
            background-color: rgba(0, 0, 0, 0.9);
        }}
    </style>
</head>
<body>
    <a class="enunciado-button" href="file:///C:/Users/Utilizador/Desktop/TP1/plc24tp1.pdf" target="_blank">Enunciado</a>
    <a class="new-tab-button" href="file:///{caminho_imagem_info}" target="_blank">Informações</a> <!-- Botão atualizado para carregar a imagem -->
    <h1>Trabalho Prático 1</h1>
    <div class="button-container">
        <a class="button" href="pagina_alineaA.html" target="_blank">Alínea A</a>
        <a class="button" href="javascript:void(0);" onclick="window.open('pagina_alineaB.html', '_blank');">Alínea B</a>
        <a class="button" href="pagina_alineaC.html" target="_blank">Alínea C</a>
        <a class="button" href="{os.path.join(caminho_imagens, html_d)}" target="_blank">Alínea D</a>
        <a class="button" href="javascript:void(0);" onclick="window.open('pagina_alineaE.html', '_blank');">Alínea E</a> <!-- Novo botão Alínea E -->
    </div>
</body>
</html>
"""

# Caminho para salvar a página HTML principal como index.html
caminho_html_principal = r"C:\Users\Utilizador\Desktop\TP1\index.html"

# Escreve o conteúdo HTML principal no arquivo
with open(caminho_html_principal, 'w', encoding='utf-8') as file:
    file.write(html_content_principal)

# Cria a página HTML para a Alínea A
html_content_alineaA = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alínea A - Gráficos</title>
    <style>
        body {{
            background-color: black;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        h1 {{
            margin-bottom: 40px;
        }}
        .grid-container {{
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* Duas colunas */
            gap: 20px; /* Espaço entre os gráficos */
        }}
        img {{
            width: 100%; /* Largura máxima de 100% para os gráficos */
            height: auto; /* Altura automática para manter a proporção */
        }}
    </style>
</head>
<body>
    <h1>Gráficos da Alínea A</h1>
    <div class="grid-container">
        <img src="{os.path.join(caminho_imagens, 'graficos_seculo_17.png')}" alt="Gráfico Século 17">
        <img src="{os.path.join(caminho_imagens, 'graficos_seculo_18.png')}" alt="Gráfico Século 18">
        <img src="{os.path.join(caminho_imagens, 'graficos_seculo_19.png')}" alt="Gráfico Século 19">
        <img src="{os.path.join(caminho_imagens, 'graficos_seculo_20.png')}" alt="Gráfico Século 20">
    </div>
</body>
</html>
"""

# Caminho para salvar a página HTML da Alínea A
caminho_html_alineaA = r"C:\Users\Utilizador\Desktop\TP1\pagina_alineaA.html"

# Escreve o conteúdo HTML da Alínea A no arquivo
with open(caminho_html_alineaA, 'w', encoding='utf-8') as file:
    file.write(html_content_alineaA)

# Cria a página HTML para a Alínea B
html_content_alineaB = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alínea B - Tabelas</title>
    <style>
        body {{
            background-color: white;
            color: black; /* Texto em preto */
            text-align: center;
            padding: 20px;
        }}
        h1 {{
            margin-bottom: 40px;
        }}
        .container {{
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin-top: 20px;
        }}
        .tabela {{
            width: 45%;
            border: 1px solid #ccc;
            background-color: white;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            margin: 10px;
            padding: 10px;
            border-radius: 5px;
        }}
        iframe {{
            width: 100%;
            height: 600px;
            border: none;
        }}
    </style>
</head>
<body>
    <h1>Tabelas da Alínea B</h1>
    <div class="container">
        <div class="tabela">
            <h2>Tabela de Apelidos</h2>
            <iframe src="{os.path.join(caminho_imagens, html_b[0])}"></iframe>
        </div>
        <div class="tabela">
            <h2>Tabela de Nomes Próprios</h2>
            <iframe src="{os.path.join(caminho_imagens, html_b[1])}"></iframe>
        </div>
    </div>
</body>
</html>
"""

# Caminho para salvar a página HTML da Alínea B
caminho_html_alineaB = r"C:\Users\Utilizador\Desktop\TP1\pagina_alineaB.html"

# Escreve o conteúdo HTML da Alínea B no arquivo
with open(caminho_html_alineaB, 'w', encoding='utf-8') as file:
    file.write(html_content_alineaB)

# Cria a página HTML para a Alínea C
html_content_alineaC = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alínea C - Gráfico Cumulativo</title>
    <style>
        body {{
            background-color: black;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        h1 {{
            margin-bottom: 40px;
        }}
        img {{
            width: 80%; /* Largura máxima de 80% para o gráfico */
            height: auto; /* Altura automática para manter a proporção */
        }}
    </style>
</head>
<body>
    <h1>Gráfico Cumulativo da Alínea C</h1>
    <img src="{os.path.join(caminho_imagens, imagem_c)}" alt="Gráfico Cumulativo">
</body>
</html>
"""

# Caminho para salvar a página HTML da Alínea C
caminho_html_alineaC = r"C:\Users\Utilizador\Desktop\TP1\pagina_alineaC.html"

# Escreve o conteúdo HTML da Alínea C no arquivo
with open(caminho_html_alineaC, 'w', encoding='utf-8') as file:
    file.write(html_content_alineaC)

# Cria a página HTML para a Alínea D
html_content_alineaD = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alínea D - Tabela</title>
    <style>
        body {{
            background-color: white;
            color: black; /* Texto em preto */
            text-align: center;
            padding: 20px;
        }}
        h1 {{
            margin-bottom: 40px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            border: 1px solid #ccc;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h1>Tabela da Alínea D</h1>
    <iframe src="{os.path.join(caminho_imagens, html_d)}" width="100%" height="600" frameborder="0"></iframe>
</body>
</html>
"""

# Caminho para salvar a página HTML da Alínea D
caminho_html_alineaD = r"C:\Users\Utilizador\Desktop\TP1\pagina_alineaD.html"

# Escreve o conteúdo HTML da Alínea D no arquivo
with open(caminho_html_alineaD, 'w', encoding='utf-8') as file:
    file.write(html_content_alineaD)

# Cria a página HTML para a Alínea E
html_content_alineaE = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alínea E</title>
    <style>
        body {{
            background-color: white;
            color: black;
            text-align: center;
            padding: 20px;
        }}
        h1 {{
            margin-bottom: 40px;
        }}
        .container {{
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
        }}
        .info {{
            margin: 10px 0;
        }}
        img {{
            max-width: 100%;  /* Garante que a imagem não exceda a largura da tela */
            height: auto;     /* Mantém a proporção da imagem */
        }}
    </style>
</head>
<body>
    <h1></h1>
    <div class="container">
        <img src="file:///C:/Users/Utilizador/Desktop/TP1/Imagens/alineaE.png" alt="Alínea E">
    </div>
</body>
</html>
"""

# Caminho para salvar a página HTML da Alínea E
caminho_html_alineaE = r"C:\Users\Utilizador\Desktop\TP1\pagina_alineaE.html"

# Escreve o conteúdo HTML da Alínea E no arquivo
with open(caminho_html_alineaE, 'w', encoding='utf-8') as file:
    file.write(html_content_alineaE)


print("Páginas HTML foram geradas com sucesso.")
