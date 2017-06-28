#coding: utf-8
## Bot na versão 1.0 apenas terminal


import aiml
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

kernel = aiml.Kernel()
print bcolors.HEADER + "\n#########################################################################"
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
print "#########################################################################" + bcolors.ENDC
print "\n"

print bcolors.HEADER + "#########################################################################"
print bcolors.BOLD + "Dr Wostraus" + bcolors.ENDC + bcolors.HEADER + ", um Chatterbot para auxliar alunos a entender conceitos de \nInteligência Artificial \n"
print "Digite ajuda para obter todos os comandos que o bot tem \n"
print "Digite sair para terminar a execução do bot"
print "#########################################################################" + bcolors.ENDC + "\n"

while True:
    message = raw_input("Digite sua Mensagem: ")
    if message == "sair":
        exit()
    elif message == "ajuda":
        print bcolors.WARNING + "Posso responder sobre os seguintes assuntos: \n"
        print "* Definições de Inteligência Artificial"
        print "* As 4 abordagens da Inteligência Artificial"
        print "* A abordagem Agindo de Forma Humana"
        print "* A abordagem Agindo Racionalmente"
        print "* Quem foi Alan Turing"
        print "* O que é o Teste de Turing"
        print "* O que é um Agente Inteligênte"
        print "* Quais são as Aplicações de IA"
        print "* O que são Algoritmos Genéticos"
        print "* Redes Neurais"
        print "* Processos de aprendizagem"
        print "* Lógica Fuzzy"
        print "* Sistemas Multiagentes"
        print "* História da Inteligência Artificial"
        print "* Mineração de Dados"
        print "* Algoritmos de Busca"
        print "E existem alguns easter eggs escondidos ;D"

        print bcolors.ENDC
    else:
        bot_response = kernel.respond(message)
        if (bot_response == ""):
            print bcolors.FAIL + "Não entendi muito bem, digite ajuda se estiver com problemas" + bcolors.ENDC + "\n"
        else:
            print bcolors.OKBLUE + "Dr. Wostraus: " + bot_response
            print bcolors.ENDC + "\n"
