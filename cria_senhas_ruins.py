#Adiciona e remove as senhas proibidas para serem usadas como senhas de membros do Lab do GER
#Leonardo Alves de Melo

import md5
import csv

######################### DEFINITIONS ###############################

senhas_ruins = 'senhas_ruins.csv'#'/etc/init.d/senhas_ruins.csv'

########################## FUNCTIONS ################################

#MUDAR
def le_teclado():
	return raw_input()

#recebe a senha e retorna uma string da senha criptografada
def criptografa(senha): 

	m = md5.new()
	m.update(senha)
	return m.hexdigest()

def adiciona_senha_ruim():
	with open(senhas_ruins) as arq:
		arqCsv = csv.reader(arq)

		lista_senha = []
		for linha in arqCsv:
			lista_senha.append(linha[0])

		print 'Escreva no teclado numerico a senha que deseja proibir'
		senha = le_teclado()
		senha_criptografada = criptografa(senha)

		#Verifica se essa senha ja nao foi adicionada
		for linha in senha:
			if linha == senha_criptografada:
				print 'Essa senha ja foi adicionada!'
				return

		#Se ja nao foi adicionada, adiciona
		lista_senha.append(senha_criptografada)

	with open(senhas_ruins, 'w') as arq:
		senhas = csv.writer(arq)
		for linha in lista_senha:
			senhas.writerow([linha])
	print 'Senha adicionada com sucesso!'

########################### MAIN ########################

loop = True
while loop:
	print 'Digite [1] para adicionar uma senha proibida'
	print 'Digite [2] para sair'

	comando = raw_input()

	if comando == '1':
		adiciona_senha_ruim()
	elif comando == '2':
		loop = False
	else:
		print 'Este nao eh um comando valido!'

print 'Obrigado e volte sempre!'