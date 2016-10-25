import md5
import csv
from time import sleep
import pyupm_i2clcd as lcd

ERRO_LIMITE = 3
ERRO_TEMPO = 60

####################### FUNCOES #########################

def criptografa(senha): #recebe a senha e retorna uma string da senha criptografada

	m = md5.new()

	m.update(senha)

	return m.hexdigest()

def autentifica(senha):

	pessoas = []
	senhas = []

	arq_senhas = [] # Garante que arq_senhas exista


	with open('/etc/init.d/senhas.csv', 'r') as raw_arq:
		arq_senhas = csv.reader(raw_arq) #abre o arquivo csv com nomes e senhas
		
		for linha in arq_senhas: #percorre o arquivo de pessoas e coloca os dados numa lista
			pessoas.append(linha[0])
			senhas.append(linha[1])

		senha_criptografada = criptografa(senha)

		for i in range(len(senhas)):
			if senhas[i] == senha_criptografada:
				myLcd.clear()
				myLcd.write("Ola " + pessoas[i] + "!")
				return True

		myLcd.clear()
		sleep(0.1)
		myLcd.write("Senha nao existe")
		return False


def adiciona_usuario():

	arq_senhas = [] # Garante que arq_senhas exista
	with open('/etc/init.d/senhas.csv', 'r') as raw_arq:
		arq_senhas = csv.reader(open('/etc/init.d/senhas.csv', 'r')) #abre o arquivo csv com nomes e senhas

		pessoas = []
		senhas = []

		for linha in arq_senhas: #percorre o arquivo de pessoas e coloca os dados numa lista
			pessoas.append(linha[0])
			senhas.append(linha[1])

		print "Escreva o nome da pessoa a ser adicionada"
		nome = raw_input()
		print "Escreva a senha no teclado numerico"
		senha = le_teclado()

		senha_criptografada = criptografa(senha)

		pessoas.append(nome)
		senhas.append(senha_criptografada)


		with open('senhas.csv', 'w') as raw_arq:
			for i in range(len(pessoas)):
				raw_arq.write(pessoas[i] + ',' + senhas[i] + '\n')

def le_teclado():

	teclado = open('/dev/hidraw0') #O teclado sempre se encontra nessa porta serial                                    
	                                                               
	myLcd.clear()                                                          
	myLcd.write('Escreva a senha')
	myLcd.setCursor(1,0)
	myLcd.write('e aperte Enter:') 

	lendo = True               
	                                                               
	apagado = False  

	linha = ''                                                        
	while lendo:                                                    
	                                               
		linha = linha + str(teclado.read(1))                             
	                                                                        
		tam = len(linha)/40                                               
	                                                                          
		if linha: 

			if not apagado:
				myLcd.clear()
				apagado = True
	        
	        if len(linha) >= 14:                                             
				if linha[len(linha) - 14] == 'X': #caracteristica do enter 
					lendo = False

	                                             
		                                          
		myLcd.setCursor(0,0)
		for j in range(tam):                                   
			myLcd.write('*')  

	return str(linha)   

	


####################### MAIN BEHAVIOUR ################################
sleep(5)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62) #Inicializo o lcd na variavel myLcd

myLcd.setCursor(0,0) #seta a posicao inicial do cursor

myLcd.setColor(53, 39, 249) #cor de fundo em RGB

myLcd.displayOff()
sleep(1)
myLcd.displayOn()

#adiciona_usuario()

erro = 0
is_blocked = False
counter = 0

while True: 

	

	if (not is_blocked):
		senha = le_teclado()
		result = autentifica(senha)
		
		if (result):
			erro = 0
		else:
			erro = erro + 1

		if (erro >= ERRO_LIMITE):
			is_blocked = True
			counter = ERRO_TEMPO
			myLcd.setColor(255, 0, 0)
			myLcd.clear()
			myLcd.write('Travando sistema')


		sleep(3)

	else:
		
		myLcd.clear()
		myLcd.write('Tempo restante:')
		myLcd.setCursor(1,0)
		myLcd.write(str(counter))
		sleep(1)
		counter = counter - 1
		if (counter <= 0):
			is_blocked = False
			myLcd.setColor(53, 39, 249) #cor de fundo em RGB

	
    