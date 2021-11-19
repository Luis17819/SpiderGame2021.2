
import time



def tempo(s):
    time.sleep(s)

def registralog(nome, email):
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    try:
        arquivo = open("historico.txt","r")
    except:
        arquivo = open("historico.txt","w")
        arquivo.close
        arquivo = open("historico.txt","r")
    dados = arquivo.read()
    arquivo.close()    
    dados = dados + "Nome: " + nome + " --> " + "Email: " + email + "\n"
    arquivo = open ("historico.txt", "w")
    arquivo.write(dados)
    arquivo.close()
    print("Prepare-se o jogo vai começar...")
    tempo(3)