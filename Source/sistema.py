#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Desenvolvedor: Leonardo Alves de Melo - leonardo.alves.melo.1995@gmail.com
#GER - Grupo de Estudos em Robotica

from funcoes import *

############# DEFINICOES ###########

ERRO_LIMITE = 3 #Numero de tentativas permitidas antes de travar o sistema
ERRO_TEMPO = 60 #Tempo inicial em que o sistema ficarah travado

####################### MAIN ################################

print 'Sistema da porta iniciado!'

erro = 0
bloqueado = False
contador = 0

while True: 

	if not bloqueado:
		solicita_senha()
		senha = le_teclado()
		pessoa = autentica(senha)
		
		if pessoa:
			erro = 0
			da_boas_vindas(pessoa)
			registra_entrada(pessoa)
			abre_porta()
		else:
			erro += 1
			alerta_pessoa_nao_encontrada()

		if erro >= ERRO_LIMITE:
			bloqueado = True
			contador = ERRO_TEMPO
			alerta_travamento_sistema()

		sleep(3)

	else:
		
		informa_tempo_restante(contador)
		contador -= 1
		if contador <= 0:
			bloqueado = False
			reseta_LCD()

	
    