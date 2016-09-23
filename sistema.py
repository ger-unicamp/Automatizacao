import mraa
import md5
import csv

senhas = csv.reader(open('senhas.csv', 'rw'))

def criptografa(senha):
	
	m = md5.new()

	m.update(senha)

	return m.digest()

def autentica(senha):
	
	senha_criptografada = criptografa(senha)

entrada = raw_input()

print criptografa(entrada)

	


