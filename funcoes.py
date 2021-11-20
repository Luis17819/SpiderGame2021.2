
import time



def tempo(s):
    time.sleep(s)

def registralog(nome, email):
    nome = input("Digite o seu Nome: ")
    email = input("Digite o seu E-mail: ")
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
    print("Prepare-se, o jogo vai começar...")
    tempo(3)