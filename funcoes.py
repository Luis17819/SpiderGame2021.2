
import time



def tempo(s):
    time.sleep(s)

def registralog(nome, email):
    nome = input("Type your name: ")
    email = input("Type your e-mail: ")
    try:
        arquivo = open("historico.txt","r")
    except:
        arquivo = open("historico.txt","w")
        arquivo.close
        arquivo = open("historico.txt","r")
    dados = arquivo.read()
    arquivo.close()    
    dados = dados + "Nome: " + nome + " --> " + "E-mail: " + email + "\n"
    arquivo = open ("historico.txt", "w")
    arquivo.write(dados)
    arquivo.close()
    print("Get ready the game will start...")
    tempo(3)