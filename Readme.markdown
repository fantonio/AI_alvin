Bot de nome alvin
===========================================================

Versão 1.0

Criado por [Fábio Antonio] 
fantonios@gmail.com

Descrição
----------

Este bot chamado alvin é feito em python e utiliza da linguagem AIML (Artificial Intelligence Markup Language), uma linguagem de criação de personagens inteligentes, eu utilizei aqui para a criação de um bot de interação com o usuário. Utilizando do Pyamil que é a unificação da linguagem python com a aiml, sendo assim permite um rápido desenvolvimento sem a necessidade de técnicos especialistas em programação e lógica.

Biblioteca usadas
------------------

import pyttsx
import normalize

Esto usando a biblioteca pyttsx e ela usa drive de audio diferente em cada sistema;

  Item 1: No Windows pyttsx usa o driver SAPI5.
  Item 2: No Linux pyttsx usa o driver eSpeak.
		Para instalar a biblioteca pyttsx no Linux baixe o arquivo do site oficial: http://pypi.python.org/pypi/pyttsx
		A biblioteca normalize é uma classe existente da classe principal: unicodedata que é instalada por padrão ao instalarmos o python no linux.
  Item 3: No Mac IOs pyttsx esta usando o driver padrão.

### Após instalar as bibliotecas, baixar e descompactar o programa, execute:

python alvin.py

Após carregar as bibliotecas de linguagens, ele pedira o seu nome digite, após o teclar enter
o sistema mostrara o prompt de interação de dialogo.

bot:< "indica que esta esperando que você digite alguma coisa, para interagir com o alvin."
bot:> "indica a resposta que alvin retorno a sua interação com ele."

Agora a resposta de alvin esta sendo sintetizada.
