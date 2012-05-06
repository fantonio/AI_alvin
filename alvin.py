# coding: iso-8859-1 -*-

from unicodedata import normalize
import pyttsx
import aiml
import os

def tiraAcento(str):
	return normalize('NFKD', str.decode('utf-8')).encode('ASCII', 'ignore')
	
def voz(str):
   engine = pyttsx.init()
   engine.say(str)
   engine.runAndWait()
   return

# defini cores texto.
CorVerme = '\033[31m'
CorVerde = '\033[32m' 
CorAzul  = '\033[34m'
CorOrig  = '\033[0;0m'

# inicialização
ai = aiml.Kernel() 
ai.learn('std-startup.xml') # lê o arquivo principal da AIML e faz referências aos outros
ai.respond('load aiml b') 	# faz com que os outros arquivos da AIML sejam carregados

print " "
nome = raw_input('Qual o seu nome: ')

print "Seja bem vindo! ", nome
print " "
print "A partir de agora você podera conversar com o bot '<' aguarda sua interação."
print " "
 
while (1==1):
	
	frase = raw_input("bot:"+CorVerde+"< "+CorOrig) 			# cor vermelha na escrita.	
	print "bot:"+CorAzul+">"+CorOrig+" %s" % ai.respond(frase) 	# cor verde escrita.
        print ""
        if len(ai.respond(frase)) > 0: 
	       voz(tiraAcento(ai.respond(frase))) # Chama rotina de pronuncia.
