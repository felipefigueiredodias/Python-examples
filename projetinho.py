var = ''
nomesArquivos = []
array = []
tol = open("fefo.txt", 'a')
while var != 'n':
    lerArquivo = str(input("Digite o nome do arquivo\n"))
    nomesArquivos.append(lerArquivo)
    var = str(input("Deseja continuar?"))
for arquivos in nomesArquivos:
    arq = open(arquivos)
    linhas = arq.readlines()
    for linha in linhas:
        teste = linha.replace("\n", "")
        array.append(teste)
        #tol.write(teste + "\n")

lista_unica = list(set(array))

for lk in lista_unica:
    tol.write(lk+"\n")


