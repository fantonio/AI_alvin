# -*- coding: utf-8 -*-
# coding: iso-8859-1 -*-

from unicodedata import normalize
import pyttsx
import aiml
import os
import sys

def tiraAcento(str):    # Tira o acento para poder ser pronunciado a frase.
	return normalize('NFKD', str.decode('utf-8')).encode('ASCII', 'ignore')
	
def voz(str):
   engine = pyttsx.init()
   engine.say(str)
   engine.runAndWait()
   return

if __name__ == '__main__':
	
  # defini cores texto.
  CorVerme = '\033[31m'
  CorVerde = '\033[32m' 
  CorAzul  = '\033[34m'
  CorOrig  = '\033[0;0m'	
  vozAtiva = 0	
	
  # Verifica se parametro -voz foi passado.	
  if len(sys.argv) > 1:
    if sys.argv[1] == '-voz':
	   vozAtiva = 1
	   		
  # inicialização
  ai = aiml.Kernel() 
  ai.learn('std-startup.xml')   # lê o arquivo principal da AIML e faz referências aos outros
  ai.respond('load aiml b') 	# faz com que os outros arquivos da AIML sejam carregados
  print ""
  print "A partir de agora você podera conversar com o bot '<' aguarda sua interação."
  print ""
 
  while (1==1): # Loop de entrada de dados.
	try:
		frase = raw_input("bot:"+CorVerde+"< "+CorOrig) 		# cor vermelha na escrita.	
		print "bot:"+CorAzul+">"+CorOrig+" %s" % ai.respond(frase) 	# cor verde escrita.
		print ""
		
		# Se voz ativada gera pronuncia da resposta do dialogo.
		if vozAtiva == 1:
			if len(ai.respond(frase)) > 0:
				voz(tiraAcento(ai.respond(frase))) # Chama rotina de pronuncia.
		if frase == "quit":
			sys.exit()
	except:
		frase = False
		sys.exit()

