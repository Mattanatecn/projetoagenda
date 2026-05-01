from datetime import date
tarefas=[]
def adicionar_tarefa():
    nome=input('digite uma tarefa:')
    data_texto=input('digite data (dd/mm/aaaa):')
    partes=data_texto.split("/")
    dia=int(partes[0])
    mes=int(partes[1])
    ano=int(partes[2])
    data_entrega=date(ano,mes,dia)
    tarefa={
        'nome': nome,
        'data': data_entrega
    }
    tarefas.append(tarefa)
    print('tarefa adicionada')
def chave_data(t):
    return t['data']#ordenar a lista
def listar_tarefas():
    hoje=date.today()
    ordenadas=sorted(tarefas,key=chave_data)
    print('\nTarefas:')
    for t in ordenadas:
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
            status
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
    else:
        print('digite opções de 1 a 3')
        continue