# coding: iso-8859-1 -*-

import aiml
import os

# defini cores texto.
CorVerme = '\033[31m'
CorVerde = '\033[32m' 
CorAzul  = '\033[34m'
CorOrig  = '\033[0;0m'

#os.chdir('') # diretório que contém os arquivos da AIML standard

# inicialização
ai = aiml.Kernel() 
ai.learn('std-startup.xml') # lê o arquivo principal da AIML e faz referências aos outros
ai.respond('load aiml b') 	# faz com que os outros arquivos da AIML sejam carregados

print ""
nome = raw_input('Qual o seu nome: ')

print "Seja bem vindo! ", nome
print ""
print "A partir de agora você podera conversar com o bot '<' aguarda sua interação."
print ""
 
while (1==1):
	
	#frase = raw_input('Fale algo ao bot: ')
	frase = raw_input("bot:"+CorVerde+"< "+CorOrig) # cor vermelha na escrita.
	
	#print "Resposta do bot: %s" % ai.respond(frase)	
	print "bot:"+CorAzul+">"+CorOrig+" %s" % ai.respond(frase) # cor verde escrita.
        print ""
