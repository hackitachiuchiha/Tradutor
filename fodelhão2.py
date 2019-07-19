# -*- coding: utf-8 -*-
from googletrans import Translator
translator = Translator()


cont = 1
# O unicode não é necessário para mostrar só o texto
nome = '1. Overview of the Projects'
enviar = open(nome+'.vtt','r') 
receber = open(nome+' pt.vtt','w')

for linha in enviar.readlines():
	if(cont == 3) :      
	    traduzido = translator.translate(linha, dest='pt').text
	    receber.write(traduzido+'\n')
	    cont = 0
	else :
	    receber.write(linha)
	    cont = cont + 1

enviar.close()
receber.close()
