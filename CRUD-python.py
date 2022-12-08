from operator import truediv
import os
################################## verificação se existe arquivo ################################
def existe_arquivo_professor(nome_arquivo):
            
            if os.path.exists(nome_arquivo):
                return True
            else:
                arq=open(nome_arquivo, 'w')
                arq.close()


def existe_arquivo_disciplina(nome_arquivo):
            
            if os.path.exists(nome_arquivo):
                return True
            else:
                arq=open(nome_arquivo, 'w')
                arq.close()


def existe_arquivo_profDisc(nome_arquivo):
            
            if os.path.exists(nome_arquivo):
                return True
            else:
                arq=open(nome_arquivo, 'w')
                arq.close()

arquivo_profDisc= 'arquivo_profDisc.txt'
arquivo_professor= 'arquivo_professor.txt'
arquivo_disciplina= 'arquivo_disciplinas.txt'
existe_arquivo_professor(arquivo_professor)
existe_arquivo_disciplina(arquivo_disciplina)
existe_arquivo_profDisc(arquivo_profDisc)


################################### criação de classes ###########################################

class professor:
    registroFuncional=""
    nome=""
    dataDeNascimento= ""
    sexo=""
    areaDePesquisa=""
    titulação=""
    graduação=""
    email= []
    telefone= []

class disciplina:
    sigla=""
    nome=""
    ementa=""
    bibliografia=""
    numeroDeCreditos=""
    cargaHoraria=""

class professorDisciplina:
    registroFuncional=''
    siglaDisciplina=''
    ano=''
    semestre=''
    dias_da_semana=''
    horarios_inicio=''
    curso=''

##################################################################################################
###################################### INICIO PROFESSOR ##########################################

## lendo e escrevendo arquivo
def le_arquivo_professor(nome_arquivo):
    professores=[]
    arq=open(nome_arquivo, 'r')
    if os.path.getsize('arquivo_professor.txt') == 0:
        return professores
    else: 
       for linha in arq:
         if linha != "\n":
                infos = linha.split(';')
                p=professor()
                p.registroFuncional = infos[0]
                p.nome=infos[1]
                p.dataDeNascimento= infos[2]
                p.sexo=infos[3]
                p.areaDePesquisa=infos[4]
                p.titulação=infos[5]
                p.graduação=infos[6]
                p.email= infos[7]
                p.telefone= infos[8]
                professores.append(p)
    arq.close()
    return professores

def escreve_arquivo_professor(professor, nome_arquivo):
    arq=open(nome_arquivo, 'w')
    i=0
    while i<len(professor):
        p=professor[i]
        arq.write(p.registroFuncional + ";" + p.nome + ";" + p.dataDeNascimento + ";" + p.sexo +";"+ p.areaDePesquisa+";"+p.titulação+";"+ p.graduação+";" + p.email + ";"+ p.telefone+'\n')
        i+=1
    arq.close()

    ## criando funções
def buscar_professor (lista_professores,num_registro):
    existe = False
    saida = - 1
    i=0
    while i<len(lista_professores) and existe == False:
        if lista_professores[i].registroFuncional == num_registro:
            saida = i
            existe=True
        i=i+1
    return saida

def inserir_professor(lista_professor):
    p= professor()
    p.registroFuncional=input("Informe o registro funcional: ")
    saidaBuscarProf= buscar_professor(lista_professor, p.registroFuncional)
    if saidaBuscarProf == -1:
        p.nome=input("Informe o nome: ")
        p.dataDeNascimento=input("Informe a data de nascimento: ")
        p.sexo=input("Informe o sexo: ")
        p.areaDePesquisa=input("Informe a area de pesquisa: ")
        p.titulação=input("infomrme o titulo do professor: ")
        p.graduação=input("Informe o tipo de graduação: ")
        
        email=[]
        email.append(input("Informe o email: ")+" ")
        novo_email = input("deseja informar outro email? (S ou aperte qualquer tecla para continuar)").upper()
        while novo_email=='S': 
            email.append(input("digite o email: ")+" ")
            novo_email = input("deseja informar outro email? (S ou aperte qualquer tecla para continuar)").upper()
        str_email='-'.join(map(str,email))
        p.email=str_email
        
        telefone=[]
        telefone.append(input("Informe o telefone: ")+" ")
        novo_tel = input("deseja informar outro telefone? (S ou aperte qualquer tecla para continuar)").upper()
        while novo_tel=='S': 
            telefone.append(input("digite o telefone: ")+" ")
            novo_tel = input("deseja informar outro telefone? (S ou aperte qualquer tecla para continuar)").upper()
        str_telefone='-'.join(map(str,telefone))  
        p.telefone=str_telefone  
    else:
        print("o professor já existe")

    lista_professor.append(p)

def imprime_professor(p):
  print(p.registroFuncional + " | " + p.nome + " | " + p.dataDeNascimento + " | " + p.sexo +" | "+ p.areaDePesquisa+" | "+p.titulação+" | "+ p.email + " | "+ p.telefone)

def listar_professor(lista_professor):
    if len(lista_professor)==0:
        print("a lista esta vazia")
    else:
        i=0
        while i<len(lista_professor):
            imprime_professor(lista_professor[i])
            i+=1
def listar_elemento_professor(lista_professor):
    if len(lista_professor)==0:
        print("lista vazia")
    else:
        num_registro=input("qual registro deseja listar: ")
        i=buscar_professor(lista_professor,num_registro)
        if i == -1:
            print("Esse registro não existe")
        else:
            imprime_professor(lista_professor[i])

def alterar_item_professor(lista_professor):
        if len(lista_professor)==0:
            print("a lista esta vazia")
        else:
            num_registro= (input("qual o registro deseja alterar?"))
            i=-1
            while i== -1:
            #se i for diferente de -1 signifca que existe professor e o i passa a ser o indice dele
                i=buscar_professor(lista_professor, num_registro)
                if i == -1:
                    print("registro não existe")
                    num_registro= (input("qual o registro deseja alterar?"))

            lista_professor[i].nome = input("Digite o nome do professor: ")
            lista_professor[i].dataDeNascimento = input("Digite a data de nascimento do professor: ")
            lista_professor[i].sexo =input("Digite o sexo do professor")
            lista_professor[i].areaDePesquisa= input("Digite a area de pesquisa: ")
            lista_professor[i].titulação =input("Digite a titulação do professor: ")
            lista_professor[i].graduação=input("Digite a graduação do professor: ")
            lista_professor[i].email=[]
            lista_professor[i].email.append(input("Informe o email: ")+" ")
            

            mail = input("deseja informar outro email? (S ou aperte qualquer tecla para continuar)").upper()
            while mail=='S': 
                lista_professor[i].email.append(input("digite o email: ")+" ")
                mail = input("deseja informar outro email? (S ou aperte qualquer tecla para continuar)").upper()
            
            #convertendo lista para string para poder concatenar
            str_email='-'.join(map(str,lista_professor[i].email))
            lista_professor[i].email=str_email


            #convertendo lista para string para poder concatenar
            lista_professor[i].telefone=[]
            lista_professor[i].telefone.append(input("Informe o telefone: ")+" ")
            tel= input("deseja informar outro telefone? (S ou aperte qualquer tecla para continuar)").upper()
            while tel=='S': 
                lista_professor[i].telefone.append(input("digite o telefone: ")+" ")
                tel= input("deseja informar outro telefone? (S ou aperte qualquer tecla para continuar)").upper()
            str_tel='-'.join(map(str,lista_professor[i].telefone))
            lista_professor[i].telefone=str_tel

def excluir_item_professor(lista_professor):
    if len(lista_professor)==0:
        print("a lista esta vazia")
    else:
            num_registro= (input("qual o registro deseja excluir?"))
            i=-1
            while i== -1:
                i=buscar_professor(lista_professor, num_registro)
                if i == -1:
                    print("registro não existe")
                    num_registro= (input("qual o registro deseja excluir?"))
            del lista_professor[i]



###################################### FIM PROFESSOR #############################################

###################################### INICIO DISCIPLINA #########################################
## lendo e escrevendo arquivo
def le_arquivo_disciplina(nome_arquivo):
    disciplinas=[]
    arq=open(nome_arquivo, 'r')
    if os.path.getsize('arquivo_disciplinas.txt') == 0:
        return disciplinas
    else: 
       for linha in arq:
         if linha != "\n":
                infos = linha.split(';')
                d=disciplina()
                d.sigla = infos[0]
                d.nome = infos[1]
                d.ementa = infos[2]
                d.bibliografia = infos[3]
                d.numeroDeCreditos = infos[4]
                d.cargaHoraria = infos[5]

                disciplinas.append(d)
    arq.close()
    return disciplinas

def escreve_arquivo_disciplina(disciplinas, nome_arquivo):
    arq=open(nome_arquivo, 'w')
    i=0
    while i<len(disciplinas):
        d=disciplinas[i]
        arq.write(d.sigla+ ";" + d.nome + ";" +d.ementa + ";" +d.bibliografia + ";" +d.numeroDeCreditos + ";" +d.cargaHoraria +'\n')
        i+=1
    arq.close()

    ## criando funções
def buscar_disciplina (lista_disciplina,sigla):
    existe = False
    saida = - 1
    i=0
    while i<len(lista_disciplina) and existe == False:
        if lista_disciplina[i].sigla == sigla:
            saida = i
            existe=True
        i=i+1
    return saida

def inserir_disciplina(lista_disciplina):
    d= disciplina()
    d.sigla=input("Informe a sigla: ")
    saidaBuscarDisc= buscar_disciplina(lista_disciplina, d.sigla)
    if saidaBuscarDisc == -1:
        d.nome=input("Informe o nome: ")
        d.ementa=input("Informe a ementa: ")
        d.bibliografia=input("Informe a bibliografia: ")
        d.numeroDeCreditos=input("Informe o numero de creditos: ")
        d.cargaHoraria=input("Informe a carga horaria: ")
        lista_disciplina.append(d)
    else:
        print("o professor já existe")


def imprime_disciplina(d):
    print(d.sigla + " | " + d.nome + " | "+ d.ementa+" | "+d.bibliografia+" | "+d.numeroDeCreditos+" | "+d.cargaHoraria )

def listar_disciplina(lista_disciplina):
    if len(lista_disciplina)==0:
        print("a lista esta vazia")
    else:
        i=0
        while i<len(lista_disciplina):
            imprime_disciplina(lista_disciplina[i])
            i+=1

def listar_elemento_disciplina(lista_disciplina):
    if len(lista_disciplina)==0:
        print("lista vazia")
    else:
        sigla=input("qual sigla deseja listar: ")
        i=buscar_disciplina(lista_disciplina,sigla)
        if i == -1:
            print("Esse registro não existe")
        else:
            imprime_disciplina(lista_disciplina[i])

def alterar_item_disciplina(lista_disciplina):
        if len(lista_disciplina)==0:
            print("a lista esta vazia")
        else:
            sigla= (input("qual o sigla deseja alterar?"))
            i=-1
            while i== -1:
            #se i for diferente de -1 signifca que existe professor e o i passa a ser o indice dele
                i=buscar_disciplina(lista_disciplina, sigla)
                if i == -1:
                    print("registro não existe")
                    sigla= (input("qual o registro deseja alterar?"))

            lista_disciplina[i].nome = input("Digite o nome do professor: ")
            lista_disciplina[i].ementa = input("Digite a ementa: ")
            lista_disciplina[i].bibliografia =input("Digite a bibliografia: ")
            lista_disciplina[i].numeroDeCreditos= input("Digite o número de créditos: ")
            lista_disciplina[i].cargaHoraria =input("Digite a carga horaria: ")
            
def excluir_item_disciplina(lista_disciplina):
    if len(lista_disciplina)==0:
        print("a lista esta vazia")
    else:
            sigla= (input("qual sigla deseja excluir?"))
            i=-1
            while i== -1:
                i=buscar_disciplina(lista_disciplina, sigla)
                if i == -1:
                    print("sigla não existe")
                    sigla= (input("qual sigla deseja excluir?"))
            del lista_disciplina[i]

###################################### FIM DISCIPLINA ############################################


###################################### INICIO PROFDISC ############################################
## lendo e escrevendo arquivo
def le_arquivo_profDisc(nome_arquivo):
    profDisc=[]
    arq=open(nome_arquivo, 'r')
    if os.path.getsize('arquivo_profDisc.txt') == 0:
        return profDisc
    else: 
       for linha in arq:
         if linha != "\n":
                infos = linha.split(';')
                pd=professorDisciplina()
                pd.registroFuncional=infos[0]
                pd.siglaDisciplina=infos[1]
                pd.ano=infos[2]
                pd.semestre=infos[3]
                pd.dias_da_semana=infos[4]
                pd.horarios_inicio=infos[5]
                pd.curso=infos[6]
                
                profDisc.append(pd)
    arq.close()
    return profDisc

def escreve_arquivo_profDisc(profDisc, nome_arquivo):
    arq=open(nome_arquivo, 'w')
    i=0
    while i<len(profDisc):
        pd=profDisc[i]
        arq.write(pd.registroFuncional+ ";"+pd.siglaDisciplina+';'+  pd.ano+';'+  pd.semestre+';'+  pd.dias_da_semana+';'+ pd.horarios_inicio+';'+ pd.curso+ '\n' )
        i+=1
    arq.close()

    ## criando funções
def buscar_profDisc (lista_profDisc,num_registro, sigla):
    existe = False
    saida = - 1
    i=0
    while i<len(lista_profDisc) and existe == False:
        if lista_profDisc[i].registroFuncional == num_registro and lista_profDisc[i].siglaDisciplina == sigla:
            saida = i
            existe=True
        i=i+1
    return saida

def inserir_profDisc(lista_professor, lista_disciplina, lista_profDisc):
    pd=professorDisciplina()
    num_registro=input("digite o registro funcional do professor: ")
    saidaProfessor=buscar_professor(lista_professor, num_registro)
    #saida -1 == nao tem professor igual
    if saidaProfessor != -1: #se professor existe
        sigla=input("digite a sigla da Disciplina: ")
        saidaDisciplina=buscar_disciplina(lista_disciplina, sigla)
        if saidaDisciplina != -1:#se disciplina existe
            saidaProfDisc=buscar_profDisc(lista_profDisc,num_registro, sigla)
            if saidaProfDisc != -1:
                print("professor e materia ja cadastrados")
            else:
                pd.registroFuncional=num_registro
                pd.siglaDisciplina=sigla
                pd.ano=input("Digite o ano: ")
                pd.semestre=input("Digite o semestre: ")
                
                dias_da_semana=[]
                dias_da_semana.append(input("Informe o dia da semana: "))
                novo_dia = input("deseja informar outro dia? (S ou aperte qualquer tecla para continuar)").upper()
                while novo_dia=='S': 
                    dias_da_semana.append(input("digite o dia: "))
                    novo_dia = input("deseja informar outro dia? (S ou aperte qualquer tecla para continuar)").upper()
                str_dias_da_semana='-'.join(map(str,dias_da_semana))
                pd.dias_da_semana=str_dias_da_semana


                
                horarios_inicio=[]
                horarios_inicio.append(input("Informe o horario: ")+" ")
                novo_horario = input("deseja informar horario? (S ou aperte qualquer tecla para continuar)").upper()
                while novo_horario=='S': 
                    horarios_inicio.append(input("digite o horario: ")+" ")
                    novo_horario = input("deseja informar outro horario? (S ou aperte qualquer tecla para continuar)").upper()
                str_horarios_inicio='-'.join(map(str,horarios_inicio))
                pd.horarios_inicio=str_horarios_inicio

                pd.curso=input("Digite o nome do curso: ")
        else:
         print("parametro digitado não existe")
    else:
         print("parametro digitado não existe")
        

    lista_profDisc.append(pd)

def imprime_profDisc(pd):
    print(pd.registroFuncional + " | " + pd.siglaDisciplina + " | "+ pd.ano+" | "+pd.semestre+" | "+pd.dias_da_semana+" | "+pd.horarios_inicio+' | ' + pd.curso)

def listar_profDisc(lista_profDisc):
    if len(lista_profDisc)==0:
        print("a lista esta vazia")
    else:
        i=0
        while i<len(lista_profDisc):
            imprime_profDisc(lista_profDisc[i])
            i+=1
# falta colcoar listar elemento profdisc
def listar_elemento_profDisc(lista_disciplina, lista_professor, lista_profDisc):
    if len(lista_profDisc)==0:
        print("lista vazia")
    else:
        num_registro=input("digite o registro funcional do professor: ")
        saidaProfessor=buscar_professor(lista_professor, num_registro)
        if saidaProfessor != -1: #se professor existe
            sigla=input("digite a sigla da Disciplina: ")
            saidaDisciplina=buscar_disciplina(lista_disciplina, sigla)
            if saidaDisciplina != -1:#se disciplina existe
                saidaProfDisc=buscar_profDisc(lista_profDisc,num_registro, sigla)
                if saidaProfDisc != -1:#se prof e disciplina exitem no mesmo registro retorne o i
                    imprime_profDisc(lista_profDisc[saidaProfDisc])
                else:
                    print("cadastro não encontrado")

def alterar_item_profDisc(lista_profDisc, lista_professor, lista_disciplina):
        if len(lista_profDisc)==0:
            print("a lista esta vazia")
        else:
            num_registro=input("digite o registro funcional do professor: ")
            saidaProfessor=buscar_professor(lista_professor, num_registro)
            if saidaProfessor != -1: #se professor existe
                sigla=input("digite a sigla da Disciplina: ")
                saidaDisciplina=buscar_disciplina(lista_disciplina, sigla)
                if saidaDisciplina != -1:#se disciplina existe
                    saidaProfDisc=buscar_profDisc(lista_profDisc,num_registro, sigla)
                    if saidaProfDisc != -1:#se prof e disciplina exitem no mesmo registro retorne o i
                        

                        lista_profDisc[saidaProfDisc].ano = input("Digite o ano: ")
                        lista_profDisc[saidaProfDisc].semestre = input("Digite o semestre: ")

                        lista_profDisc[saidaProfDisc].dias_da_semana=[]
                        lista_profDisc[saidaProfDisc].dias_da_semana.append(input("Digite digite o dia da semana: "))
                        novo_dia = input("deseja informar outro dia? (S ou aperte qualquer tecla para continuar)").upper()
                        while novo_dia=='S': 
                            lista_profDisc[saidaProfDisc].dias_da_semana.append(input("digite o dia: ")+" ")
                            novo_dia = input("deseja informar outro dia? (S ou aperte qualquer tecla para continuar)").upper()
                        str_dias_da_semana='-'.join(map(str,lista_profDisc[saidaProfDisc].dias_da_semana))
                        lista_profDisc[saidaProfDisc].dias_da_semana=str_dias_da_semana

                        lista_profDisc[saidaProfDisc].horarios_inicio=[]
                        lista_profDisc[saidaProfDisc].horarios_inicio.append(input("Digite o horario: "))
                        novo_horario = input("deseja informar horario? (S ou aperte qualquer tecla para continuar)").upper()
                        while novo_horario=='S': 
                            lista_profDisc[saidaProfDisc].horarios_inicio.append(input("digite o horario: ")+" ")
                            novo_horario = input("deseja informar outro horario? (S ou aperte qualquer tecla para continuar)").upper()
                        str_horarios_inicio='-'.join(map(str, lista_profDisc[saidaProfDisc].horarios_inicio))
                        lista_profDisc[saidaProfDisc].horarios_inicio=str_horarios_inicio

                        lista_profDisc[saidaProfDisc].curso =input("Digite o nome do curso: ")


def excluir_item_profDisc(lista_profDisc, lista_professor, lista_disciplina):
    if len(lista_disciplina)==0:
        print("a lista esta vazia")
    else:
        num_registro=input("digite o registro funcional do professor: ")
        saidaProfessor=buscar_professor(lista_professor, num_registro)
        if saidaProfessor != -1: #se professor existe
            sigla=input("digite a sigla da Disciplina: ")
            saidaDisciplina=buscar_disciplina(lista_disciplina, sigla)
            if saidaDisciplina != -1:#se disciplina existe
                saidaProfDisc=buscar_profDisc(lista_profDisc,num_registro, sigla)
                if saidaProfDisc != -1:#se prof e disciplina exitem no mesmo registro retorne o i
                    del lista_profDisc[saidaProfDisc]
                    print('excluido')

              


########################################### FIM PROFDISC ############################################

############################################ INICIO RELATORIO ############################################
def buscar_professor_titulação (lista_professores,titulo):
    
    saida = []
    i=0
    while i<len(lista_professores):
        if lista_professores[i].titulação == titulo:#2 procura o indice do titulo na lista professor 
            saida.append(i) #3 cria uma lista com os indices referentes a listra professor
        
        i=i+1
    return saida


def relatorio_titulo_professor(lista_professores):
    lista_titulos=[]
    if len(lista_professores)==0:
        print("lista vazia")
    else:
       titulo=(input("digite a titulação deseja: ")) #1 informa o titulo
       lista_titulos=buscar_professor_titulação(lista_professores, titulo)
    if lista_titulos == []:
            print("Esse titulo não existe")
    else:
        i=0
        while i<len(lista_titulos):
            imprime_professor(lista_professores[lista_titulos[i]])#4 imprime a lista professor, mas com os indices da lista pré selecionados
            i+=1
##########################################################
def buscar_credito_disciplina (lista_disciplina, Ncredito):
    saida = []
    i=0
    while i<len(lista_disciplina):
        if int(lista_disciplina[i].numeroDeCreditos) >= int(Ncredito):
            saida.append(i)
        i=i+1
    return saida

def relatorio_credito_disciplina(lista_disciplina):
    lista_creditos=[]
    if len(lista_disciplina)==0:
        print("lista vazia")
    else:
       Ncredito=(input("digite número de créditos mínimos: ")) 
       lista_creditos=buscar_credito_disciplina(lista_disciplina, Ncredito)
    if lista_creditos == []:
            print("não existe disciplina")
    else:
        i=0
        while i<len(lista_creditos):
            imprime_disciplina(lista_disciplina[lista_creditos[i]])
            i+=1
###############################################
def buscar_terçaEquinta (lista_profDisc):
    lista_dias=[]
    i=0
    while i<len(lista_profDisc):
        if lista_profDisc[i].dias_da_semana == 'terça' or lista_profDisc[i].dias_da_semana == 'quinta' or lista_profDisc[i].dias_da_semana == 'terça-quinta':
            lista_dias.append(i)   
        i=i+1
    return lista_dias

#def imprime_relatorio_terçaEquinta(pd,d,p):
    
def imprime_professor_disciplina(p,d):
  print('Registro funcional: '+ p.registroFuncional + " | " + 'Nome do Professor: '+ p.nome+ " | " + 'Sigla da matéria: ' +d.sigla+ " | " +"Nome da matéria: "+d.nome)

def imprime_relatorio_profDisc(pd):
    print("Ano: "+ pd.ano+" | "+"Semestre: "+pd.semestre+" | "+'Dia de aula: '+pd.dias_da_semana+" | "+"horario da aula: "+pd.horarios_inicio+' | ' +"Nome do Curso: "+pd.curso)

def relatorio_aulas_terçaEquinta(lista_profDisc, lista_disciplina, lista_professor):
    lista_dias=[]
    if len(lista_profDisc)==0:
        print("lista vazia")
    else:
       lista_dias=buscar_terçaEquinta(lista_profDisc)#1 crio uma lista com os dias que tem aula terça, quinta e terça e quinta
    if lista_dias == []:# se a lista voltar vazia é pq não tem aula na terça nem na quinta
            print("não existe disciplina")
    else:
        i=0
        while i<len(lista_dias):
            num_registro=(lista_profDisc[lista_dias[i]].registroFuncional)#2pego o numero de registro referente ao professor que tem aula no dia especifico
            prof=buscar_professor(lista_professor,num_registro)#3 com o numero de registro consigo pegar o prorio num de registro como o nome do prof
            sigla=(lista_profDisc[lista_dias[i]].siglaDisciplina)#4 pego a sigla referente a disciplina que tem aula no dia especifico
            relatorio_disciplina=buscar_disciplina(lista_disciplina,sigla)#5 pego a sigla junto com o nome da materia
            imprime_professor_disciplina(lista_professor[prof],lista_disciplina[relatorio_disciplina]) #6 imprimo os registros em uma mesma função
            print(" ")
            imprime_relatorio_profDisc(lista_profDisc[lista_dias[i]])#7 por questão de estética escrevo o resto dos atributos de Prof-Disc em linha separada
            print("______________________________")
            i+=1





############################################ FIM RELATORIO ############################################


############################################ INICIO MENUS ############################################
def menu():
    print("  ")
    print("   *******  MENU  *******")
    print("   **********************")
    print("professores................1")
    print("disciplinas................2")
    print("Professores-Disciplinas....3")
    print("Relatório..................4")
    print("Sair.......................0")
    opcao = input("-> ")
    return opcao

def submenu():
    print("_________________")
    print("Listar todos.........1") 
    print("listar um elemento...2") 
    print("incluir..............3") 
    print("alterar..............4") 
    print("excluir..............5") 
    print("voltar para o menu...9") 
    op= input("-> ")
    return op

def submenu_relatorio():
    
    print("mostrar professores por titulação..........1")
    print("mostrar disciplinas por crédito............2")
    print("informações terça e quinta.................3")
    print("voltar para menu...........................9")
    op= input("-> ")
    return op
############################################ FIM MENUS ############################################


###################################### INICIO MAIN ###############################################

def main():
    professores=le_arquivo_professor(arquivo_professor)
    disciplinas=le_arquivo_disciplina(arquivo_disciplina)
    profDisc=le_arquivo_profDisc(arquivo_profDisc)


    # inicio do menu
    opcao='voltarMenu'
    while opcao != '0':
        if opcao == "voltarMenu": #semnpre que opção for == a voltarMenu volta para o menu principal
            opcao=menu()
            
            #menu dos professores
        if opcao == '1':
            op=''
            while op != '9':# se escolher 9 sai para fora do laço e opcao recebe voltarMenu
                op=submenu()
                if op=="1":
                    listar_professor(professores)
                elif op=="2":
                    listar_elemento_professor(professores)
                elif op=="3":
                    inserir_professor(professores)
                elif op=="4":
                    alterar_item_professor(professores)

                elif op=="5":
                    excluir_item_professor(professores)
            else:
                opcao="voltarMenu"

        #menu das disciplinas
        elif opcao == '2':
            op=''
            while op !='9':# se escolher 9 sai para fora do laço e opcao recebe voltarMenu
                op=submenu()
                if op=="1":
                    listar_disciplina(disciplinas)
                elif op=="2":
                    listar_elemento_disciplina(disciplinas)
                elif op=="3":
                    inserir_disciplina(disciplinas)
                elif op=="4":
                    alterar_item_disciplina(disciplinas)

                elif op=="5":
                    excluir_item_disciplina(disciplinas)
                else:
                    opcao="voltarMenu"



        #professor-disciplina
        elif opcao == '3':
            op=''
            while op !='9':# se escolher 9 sai para fora do laço e opcao recebe voltarMenu
                op=submenu()
                if op=="1":
                    listar_profDisc(profDisc)
                elif op=="2":
                    listar_elemento_profDisc(disciplinas, professores, profDisc)
                elif op=="3":
                    inserir_profDisc(professores,disciplinas,profDisc)
                elif op=="4":
                    alterar_item_profDisc(profDisc, professores, disciplinas)
                elif op=="5":
                    excluir_item_profDisc(profDisc, professores, disciplinas)
                else:
                    opcao="voltarMenu"


        #relatório
        elif opcao == '4':
            op=''
            while op !='9':# se escolher 9 sai para fora do laço e opcao recebe voltarMenu
                op=submenu_relatorio()
                if op=="1":
                    relatorio_titulo_professor(professores)
                elif op=="2":
                    relatorio_credito_disciplina(disciplinas)
                elif op=="3":
                    relatorio_aulas_terçaEquinta(profDisc, disciplinas, professores)
            else:
                opcao="voltarMenu"
                
        elif opcao == '0':
            escreve_arquivo_professor(professores, arquivo_professor)
            escreve_arquivo_disciplina(disciplinas, arquivo_disciplina)
            escreve_arquivo_profDisc(profDisc, arquivo_profDisc)
            print("obrigado por usar nosso programa!")
        else:
                    print("opção invalida")  
main()