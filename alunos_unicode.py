#*************CRIA A LISTA DE NOMES DOS ALUNOS, QUE SERÁ IMPORTADA PELO SCRAPPER PARA FAZER A COMPARAÇÃO***************
import pandas as pd

def unicodizar(string):
    a = ['a', 'á', 'à', 'ã', 'A', 'Á', 'À', 'Ã']
    e = ['e', 'é', 'ê', 'è', 'ẽ', 'E', 'É', 'Ê', 'È', 'Ẽ']
    i = ['i', 'í', 'î', 'ì', 'ĩ', 'I', 'Í', 'Î', 'Ì', 'Ĩ']
    u = ['u', 'ú', 'û', 'ù', 'ũ', 'U', 'Ú', 'Û', 'Ù', 'Ũ']
    o = ['o','ó', 'ò', 'ô', 'õ', 'O', 'Ó', 'Ò', 'Ô', 'Õ']
    c = ['c', 'ç', 'C', 'Ç']
    n = ['n', 'ñ', 'N', 'Ñ']
    
    nova_string = ""
    for letra in string:
        if letra in a:
            nova_string += 'A'
        elif letra in e:
            nova_string += 'E'
        elif letra in i:
            nova_string += 'I'
        elif letra in u:
            nova_string += 'U'
        elif letra in o:
            nova_string += 'O'    
        elif letra in c:
            nova_string += 'C'
        elif letra in n:
            nova_string += 'N'
        else:
            nova_string += letra
    return nova_string
      
      
urls_alunos = [
    "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/fc30244a-166d-4830-a66d-a573ebe187eb/download/aluno.csv",
    "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/d2a472aa-3a02-4d45-bc65-5852fa9be664/download/aluno.csv",
    "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/96f114e2-58f9-4f59-9c44-f59814c0b264/download/aluno.csv",
    "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/1535c8e2-f1c4-4dcf-9948-dc734522d040/download/aluno.csv",
]


dfs_alunos = []
nomes = []

# percorre os links e adiociona na lista anterio
for url in urls_alunos:
    df = pd.read_csv(url, encoding="utf-8", sep=",")
    nome = df["nome"].tolist()
    for item in nome:
        no = item.upper()
        n = unicodizar(no)
        nomes.append(n)
    dfs_alunos.append(df)

lista_alunos = nomes