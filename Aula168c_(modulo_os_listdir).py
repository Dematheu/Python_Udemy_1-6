# os.listdir para navegar em caminhos

# C:\Users\Lucas\Desktop\EXEMPLO
# caminho = r'C:\\Users\\Lucas\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('\\Users', 'Lucas', 'Desktop', 'EXEMPLO')


for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo):
        continue

    for item in os.listdir(caminho_completo):
        print(os.path.join(caminho_completo, item))
