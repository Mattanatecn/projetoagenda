from datetime import date#importa funcao data da biblioteca tempo

tarefas=[]#cria lista vazia para armazenar as tarefas

def calcular_status(data_tarefa):#funcao para calcular status da tarefa
    hoje=date.today()#pega a data atual
    dias=(data_tarefa-hoje).days#calcula quantos dias faltam
    if dias<0:#se ja passou da data
        return 'atrasada'
    elif dias==0:#se for hoje
        return 'hoje'
    else:#se ainda faltam dias
        return 'faltam '+str(dias)+' dias'
    
def mostrar_tarefa(t):#funcao para mostrar os dados da tarefa
    status=calcular_status(t['data'])#calcula o status
    print(#mostra os dados da tarefa
        t['data'].strftime('%d/%m/%Y'),#mostra a data formatada
        '-',#separador
        t['nome'],#mostra o nome da tarefa
        "-",#separador
        status,#mostra o status
        t['prioridade'],#mostra a prioridade
        '-',#separador
        t['categoria']#mostra a categoria
        )
    
def adicionar_tarefa():#cria a funcao de adicionar tarefa
    nome=input('digite uma tarefa:')#pra pessoa digitar o nome da tarefa
    data_texto=input('digite data (dd/mm/aaaa):')#pra pessoa digitar a data
    prioridade=int(input('digite a prioridade da tarefa 1-(alta),2-(media)3-(baixa):'))#pra pessoa digitar a prioridade
    categoria=input('categoria:')#pra pessoa digitar a categoria da tarefa
    partes=data_texto.split("/")#separa a data usando /
    dia=int(partes[0])#pega o dia
    mes=int(partes[1])#pega o mes
    ano=int(partes[2])#pega o ano
    data_entrega=date(ano,mes,dia)#cria a data de entrega
    tarefa={#cria um dicionario para armazenar a tarefa
        'nome': nome,#salva o nome da tarefa
        'data': data_entrega,#salva a data da tarefa
        'prioridade': prioridade,#salva a prioridade da tarefa
        'categoria':categoria#salva a categoria da tarefa
    }
    tarefas.append(tarefa)#adiciona a tarefa na lista tarefas
    print('tarefa adicionada')#mostra mensagem de confirmacao

def listar_tarefas():#cria funcao para listar todas as tarefas
    print('\nTarefas:')#mostra titulo da lista
    ordenadas=sorted(tarefas,key=lambda t:(t['data'],t['prioridade']))#ordena pela data e prioridade
    for t in ordenadas:#loop que percorre as tarefas
        mostrar_tarefa(t)#mostra a tarefa

def listarporcategoria():#funcao para listar tarefas por categoria
    print('CATEGORIAS CADASTRADAS:')#mostra titulo das categorias
    categorias=set()#cria conjunto vazio para guardar categorias
    for t in tarefas:#percorre todas as tarefas
        categorias.add(t['categoria'])#adiciona a categoria no conjunto
    for c in categorias:#percorre todas as categorias encontradas
        print('-', c)#mostra cada categoria
    opcao=input('Digite a categoria desejada:')#usuario escolhe categoria
    print('\nTarefas da categoria:', opcao)#mostra titulo da listagem
    for t in tarefas:#percorre novamente as tarefas
        if t['categoria']==opcao:#verifica se a tarefa pertence a categoria
            mostrar_tarefa(t)#mostra a tarefa

def removertarefa():#funcao para remover uma tarefa
    print("qual tarefa você deseja remover:")#pergunta qual tarefa remover
    listar_tarefas()#mostra todas as tarefas cadastradas
    nome=input('digite o nome da tarefa:').strip()#usuario digita o nome da tarefa
    for t in tarefas:#percorre todas as tarefas
        if t['nome']==nome:#verifica se o nome corresponde
            tarefas.remove(t)#remove a tarefa da lista
            print("tarefa removida")#mostra confirmacao de remocao
            return#encerra a funcao

def salvar_tarefas():
    if len(tarefas)==0:
        print("nenhuma tarefa encontrada")
        return
    arquivo=open("tarefas.txt","w",encoding="utf-8")
    for t in tarefas:
        legenda=("Tarefas\n"
        "Legenda prioridade:1-(alta),2-(media)3-(baixa)\n")
        arquivo.write(legenda)
        linha=f"{t["nome"]} | {t["data"]} | {t["prioridade"]} | {t["categoria"]}\n"   
        arquivo.write(linha)
    arquivo.close()
    print("tarefas salvas em tarefas.txt")

def menu():#cria funcao do menu
    print("1-Adicionar")#opcao adicionar tarefa
    print("2-Listar")#opcao listar tarefas
    print("3-Listar por categoria")#opcao listar por categoria
    print("4-Remover Tarefa")#opcao remover tarefa
    print("5-salvar tarefas em aquivo")
    print("6-sair")#opcao sair do programa
    print("Legenda prioridade:1-(alta),2-(media)3-(baixa)")
    while True:#loop ate digitar numero valido
        opcao=input("escolha uma opção:")#usuario escolhe opcao
        try:#tenta transformar em numero
            opcaoint=int(opcao)#converte para inteiro
            break#se funcionar sai do loop
        except:#se der erro
            print('Digite apenas números da lista de opções')#avisa usuario
    return opcaoint#retorna opcao escolhida

print('AGENDA')#titulo do programa
op=0#variavel que guarda opcao escolhida
while op!=6:#loop principal ate escolher sair
    op=menu()#chama funcao menu
    if op==1:#se escolher adicionar
        adicionar_tarefa()#chama funcao adicionar
    elif op==2:#se escolher listar
        listar_tarefas()#chama funcao listar
    elif op==3:#se escolher listar por categoria
        listarporcategoria()#chama funcao listar categoria
    elif op==4:#se escolher remover tarefa
        removertarefa()#chama funcao remover tarefa
    elif op==5:
        salvar_tarefas()
    elif op==6:#se escolher sair
        print('saindo')#mostra mensagem de saida
        break#encerra o programa
    else:#se opcao invalida
        print('digite opções de 1 a 5')#avisa usuario
        continue#volta para o inicio do loop


    """sugestao da IA:
    linha 63 .strip() tira os espaços em branco
    linha 12 foi criada uma funcao para mostrar tarefa evitando repetições
    linha 44 foi usado lambda em vez de uma função para retornar a prioridade
    linha 3 foi criada uma função para calcular o status evitando repetições
    """