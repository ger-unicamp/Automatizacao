#Atualiza o banco de dados de usuarios e senhas para acesso ao Lab do GER
# Leonardo Alves de Melo

from funcoes import *

pasta_padrao = '/etc/init.d/' #Diretorio em que se encontra os scripts e dados do sistema


senhas_ruins = pasta_padrao + 'senhas_ruins.csv'
arquivo_senhas = pasta_padrao + 'senhas.csv' #Nome do arquivo que armazena o Hash das senhas junto com o nome do portador da senha


########################## FUNCTIONS ################################

#Retorna se eh uma senha valida ou nao
def avalia_senha(senha, pessoa):

	#Verifica se ja nao existe alguem com essa senha
	for linha in pessoa:
		if senha == linha[1]:
			print 'Ja existe uma pessoa com essa senha! Tente outra!'
			return False

	#Verifica se nao faz parte das senhas que devemos evitar
	with open(senhas_ruins, 'r') as arq:
		arqCsv = csv.reader(arq) 

		for linha in arqCsv:
			if linha[0] == senha:
				print 'Essa senha eh muito trivial! Escolha outra!'
				return False
	#Senha ok
	return True


#Adiciona o usuario na lista em ordem alfabetica e salva no BD
def adiciona_usuario():

	with open(arquivo_senhas, 'r') as arq:
		arqCsv = csv.reader(arq) #abre o arquivo csv com nomes e senhas	
		pessoa = []
		for linha in arqCsv:
			pessoa.append(linha)

		print "Escreva no teclado do computador o nome da pessoa a ser adicionada"
		nome = raw_input()

		#Checa se ja nao ha alguem com este nome
		for linha in pessoa:
			if linha[0] == nome:
				print 'Ja existe alguem com este nome!'
				return

		print "Escreva no teclado numerico a senha"

		loop = True
		#Cria um loop ateh a pessoa colocar uma senha valida
		while loop:
			senha = le_teclado()
			senha_criptografada_1 = criptografa(senha)

			print 'Escreva novamente a senha'

			senha = le_teclado()
			senha_criptografada_2 = criptografa(senha)

			if senha_criptografada_1 == senha_criptografada_2:

				#Se estiver tudo bem com a senha, sai do loop
				if avalia_senha(senha_criptografada_1, pessoa):
					loop = False
			else:
				print 'Senhas nao sao iguais!'

		pessoa.append([nome, senha_criptografada_1])

		#Ordena nossa lista em ordem alfabetica
		pessoa = sorted(pessoa)

	with open(arquivo_senhas, 'w') as arq:
		bd = csv.writer(arq)
		for linha in pessoa:
			bd.writerow(linha)

	print '\nPessoa adicionada com sucesso!\n\n'

#Criar uma interface bonitinha com print para poder remover o usuario
#
def remove_usuario():

	#Abre o arquivo do banco de dados
	with open(arquivo_senhas) as arq:
		arqPessoas = csv.reader(arq)

		pessoa = []
		for linha in arqPessoas:
			pessoa.append(linha)

		print 'Escreva o nome da pessoa que deseja remover'

		nome = raw_input()

		removi = False

		#Procura a pessoa
		for i in range(len(pessoa)):
			if pessoa[i][0] == nome:
				print 'Tem certeza que deseja remover ' + nome + '? [s/n]'
				if raw_input() == 's':
					pessoa.pop(i) #Remove a pessoa
					print 'Pessoa removida com sucesso!'
					removi = True
				else: 
					print 'Pessoa nao removida!'
				break

		if removi:
			with open(arquivo_senhas, 'w') as arq:
				bd = csv.writer(arq)
				for linha in pessoa:
					bd.writerow(linha)
		else:
			print 'Nao encontrei essa pessoa!'

######################### MAIN #######################

#Mantem o loop de interacao com o usuario para remover e adicionar quantas pessaos forem necessarias
loop = True
while loop:
	print '\nDigite [1] para adicionar um membro'
	print 'Digite [2] para remover um membro'
	print 'Digite [3] para ver todos os nomes do Banco de Dados'
	print 'Digite [4] para sair\n'

	comando = raw_input()

	if comando == '1':
		adiciona_usuario()
	elif comando == '2':
		remove_usuario()
	elif comando == '3':
		with open(arquivo_senhas, 'r') as arq:
			arqCsv = csv.reader(arq)
			print '\n----------Lista----------'
			for linha in arqCsv:
				print linha[0] 
			print '-------------------------'

	elif comando == '4':
		loop = False
	else:
		print 'Este nao eh um comando valido'

print 'Obrigado e volte sempre!'
