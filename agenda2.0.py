from datetime import date
tarefas=[]
def adicionar_tarefa():
    nome=input('digite uma tarefa:')
    data_texto=input('digite data (dd/mm/aaaa):')
    prioridade=int(input('digite a prioridade da tarefa 1-(alta),2-(media)3-(baixa):'))
    partes=data_texto.split("/")
    dia=int(partes[0])
    mes=int(partes[1])
    ano=int(partes[2])
    data_entrega=date(ano,mes,dia)
    tarefa={
        'nome': nome,
        'data': data_entrega,
        'prioridade': prioridade
    }
    tarefas.append(tarefa)
    print('tarefa adicionada')
def chave_data(t):
    return t['data']#retorna a data da tarefa
def chave_prioridade(p):
    return p['prioridade']
def listar_tarefas():
    hoje=date.today()
    ordenadas=sorted(tarefas,key=chave_data)#ordenar a lista
    ordenadas_prioridade=sorted(ordenadas,key=chave_prioridade)
    print('\nTarefas:')
    for t in ordenadas_prioridade:
        dias=(t['data']-hoje).days
        if dias<0:
            status='atrasada'
        elif dias==0:
            status='hoje'
        else:
            status='faltam ' + str(dias)+' dias'

        print(
            t['data'].strftime('%d/%m/%Y'),
            '-',
            t['nome'],
            "-",
            status,
            t['prioridade']
            )
def menu():
    print("1-Adicionar")
    print("2-Listar")
    print("3-sair")
    while True:
        opcao=input("escolha uma opção:")
        try:
            opcaoint=int(opcao)
            break
        except:
            print('Digite apenas números da lista de opções')
    return opcaoint
print('AGENDA')
op=0
while op!=3:
    op=menu()
    if op==1:
        adicionar_tarefa()
    elif op==2:
        listar_tarefas()
    elif op==3:
        print('saindo')
        break
    else:
        print('digite opções de 1 a 3')
        continue