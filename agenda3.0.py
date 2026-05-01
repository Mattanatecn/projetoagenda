from datetime import date#importa funcao data da biblioteca tempo
tarefas=[]#cria lista vazia para armazenar as tarefas
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
def chave_data(t):#funcao usada para ordenar pela data
    return t['data']#retorna a data da tarefa
def chave_prioridade(p):#funcao usada para ordenar pela prioridade
    return p['prioridade']#retorna a prioridade da tarefa
def listar_tarefas():#cria funcao para listar todas as tarefas
    hoje=date.today()#pega a data de hoje
    ordenadas=sorted(tarefas,key=chave_data)#ordena a lista pela data
    ordenadas_prioridade=sorted(ordenadas,key=chave_prioridade)#ordena novamente pela prioridade
    print('\nTarefas:')#mostra titulo da lista
    for t in ordenadas_prioridade:#loop que percorre as tarefas
        dias=(t['data']-hoje).days#calcula quantos dias faltam
        if dias<0:#se a tarefa ja passou da data
            status='atrasada'#define como atrasada
        elif dias==0:#se a tarefa for hoje
            status='hoje'#define como hoje
        else:#se ainda faltam dias
            status='faltam ' + str(dias)+' dias'#mostra quantos dias faltam
        print(#mostra os dados da tarefa
            t['data'].strftime('%d/%m/%Y'),#mostra a data formatada
            '-',#separador
            t['nome'],#mostra o nome da tarefa
            "-",#separador
            status,#mostra o status
            t['prioridade']#mostra a prioridade
            )
def listarporcategoria():#funcao para listar tarefas por categoria
    hoje=date.today()#pega a data atual
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
            dias=(t['data']-hoje).days#calcula dias restantes
            if dias<0:#se a data ja passou
                status='atrasada'#define como atrasada
            elif dias==0:#se a tarefa e hoje
                status='hoje'#define como hoje
            else:#se ainda faltam dias
                status='faltam '+str(dias)+' dias'#mostra quantos dias faltam
            print(#mostra os dados da tarefa
                t['data'].strftime('%d/%m/%Y'),#mostra data formatada
                '-',#separador
                t['nome'],#mostra nome da tarefa
                '-',#separador
                status,#mostra status
                '-',#separador
                t['prioridade']#mostra prioridade
            )
def removertarefa():#funcao para remover uma tarefa
    print("qual tarefa você deseja remover:")#pergunta qual tarefa remover
    listar_tarefas()#mostra todas as tarefas cadastradas
    nome=input('digite o nome da tarefa:')#usuario digita o nome da tarefa
    for t in tarefas:#percorre todas as tarefas
        if t['nome']==nome:#verifica se o nome corresponde
            tarefas.remove(t)#remove a tarefa da lista
            print("tarefa removida")#mostra confirmacao de remocao
            return#encerra a funcao
def menu():#cria funcao do menu
    print("1-Adicionar")#opcao adicionar tarefa
    print("2-Listar")#opcao listar tarefas
    print("3-Listar por categoria")#opcao listar por categoria
    print("4-Remover Tarefa")#opcao remover tarefa
    print("5-sair")#opcao sair do programa
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
while op!=5:#loop principal ate escolher sair
    op=menu()#chama funcao menu
    if op==1:#se escolher adicionar
        adicionar_tarefa()#chama funcao adicionar
    elif op==2:#se escolher listar
        listar_tarefas()#chama funcao listar
    elif op==3:#se escolher listar por categoria
        listarporcategoria()#chama funcao listar categoria
    elif op==4:#se escolher remover tarefa
        removertarefa()#chama funcao remover tarefa
    elif op==5:#se escolher sair
        print('saindo')#mostra mensagem de saida
        break#encerra o programa
    else:#se opcao invalida
        print('digite opções de 1 a 5')#avisa usuario
        continue#volta para o inicio do loop