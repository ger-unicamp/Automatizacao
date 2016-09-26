import mraa
import md5
import csv
from time import sleep
import pyupm_i2clcd as lcd


####################### FUNCOES #########################
def criptografa(senha): #recebe a senha e retorna uma string da senha criptografada

	m = md5.new()

	m.update(senha)

	return m.hexdigest()

def autentifica(senha):

	pessoas = []
	senhas = []

	arq_senhas = [] # Garante que arq_senhas exista
	with open('senhas.csv', 'r') as raw_arq:
		arq_senhas = csv.reader(raw_arq) #abre o arquivo csv com nomes e senhas

	for linha in arq_senhas: #percorre o arquivo de pessoas e coloca os dados numa lista
		pessoas.append(linha[0])
		senhas.append(linha[1])

	senha_criptografada = criptografa(senha)

	for i in range(len(senhas)):
		if senhas[i] == senha_criptografada:
			print "A pessoa eh: " + pessoas[i]
			return

	print "Senha nao registrada"

def adiciona_usuario():

	arq_senhas = [] # Garante que arq_senhas exista
	with open('senhas.csv', 'r') as raw_arq:
		arq_senhas = csv.reader(open('senhas.csv', 'r')) #abre o arquivo csv com nomes e senhas

	pessoas = []
	senhas = []

	for linha in arq_senhas: #percorre o arquivo de pessoas e coloca os dados numa lista
		pessoas.append(linha[0])
		senhas.append(linha[1])

	print "Escreva o nome da pessoa a ser adicionada"
	nome = raw_input()
	print "Escreva a senha"
	senha = raw_input()

	senha_criptografada = criptografa(senha)

	pessoas.append(nome)
	senhas.append(senha_criptografada)


	with open('senhas.csv', 'r') as raw_arq:
		for i in range(len(pessoas)):
			raw_arq.write(pessoas[i] + ',' + senhas[i] + '\n')

####################### MAIN BEHAVIOUR ################################


myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62) #Inicializo o lcd na variavel myLcd

myLcd.setCursor(0,0) #seta a posicao inicial do cursor

myLcd.setColor(53, 39, 249) #cor de fundo em RGB

myLcd.write('Digite sua senha')

adiciona_usuario()

while (true):
	print "Escreva a senha ja cadastrada"
	senha = raw_input()
	autentifica(senha)
