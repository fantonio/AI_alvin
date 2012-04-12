# coding: iso-8859-1 -*-

import aiml
import os
import commands

#os.chdir('') # diretório que contém os arquivos da AIML standard
ai = aiml.Kernel() # inicialização

ai.learn('std-startup.xml') # lê o arquivo principal da AIML e faz referências aos outros
ai.respond('load aiml b') # faz com que os outros arquivos da AIML sejam carregados

nome = raw_input('Qual o seu nome:')
print "Seja bem vindo", nome

while (1==1):
	
	frase = raw_input('Fale algo ao bot: ')
	print "Resposta do bot: %s" % ai.respond(frase)
#	print commands.getoutput("/usr/bin/espeak -v pt+f4 -p 99 -s 160 \"" + ai.respond(frase) + "\"")
	print commands.getoutput("/usr/bin/espeak -v pt+f1 \"" + ai.respond(frase) + "\"")
