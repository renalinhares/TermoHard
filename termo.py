import random
from unicodedata import normalize
import time

with open("palavras.txt",encoding='utf8') as file:
    allWords = file.read()
    words = list(map(str,allWords.split()))




i=0
j=0


print('Seja bem vindo ao TermoHARD !! \n Aqui vão algumas instruções: \n 1- Diferente do termo normal, esse aqui tem mais de uma dificuldade, mas não se preocupe, ele é nivelado \n 2- A letra em minusculo rerepsenta que o jogador acetou exatamente onde a letra esta posicionada na palavra \n 3- A letra em maiusculo representa que o jogador não acertou o lugar da letra mas ela é uma das que compõe a palavra \n 4- O asterisco * representa que o jogador mandou mal e a letra não compõe a palavra \n Boa sorte !! \n\n')
time.sleep(5)

dificuldade = int(input("Qual dificuldade você deseja jogar: \n 1-FÁCIL (PALAVRAS COM ATÉ 5 LETRAS) \n 2-MÉDIO (PALAVRAS DE 6 A 10 LETRAS) \n 3-DIFICIL: MAIS DE 10 LETRAS \n"))

while dificuldade >3: 
    print('Digite uma opção válida')


palavra = 'ate'


if dificuldade == 1:
    while len(palavra) > 5 :
        palavra = random.choice(words)
elif dificuldade == 2: 
    while len(palavra) <= 5 or len(palavra) > 10:
        palavra = random.choice(words)
elif dificuldade == 3:
    while len(palavra) <=10:
        palavra = random.choice(words)

palavra_certa = normalize('NFKD', palavra).encode('ASCII','ignore').decode('ASCII')
print(len(palavra)* "   *  ")

    
tentativas = len(palavra)
rodada = 0
letras_usadas = []

while True:
    dados1=[]
    dados2=[]
    palavra_formada = ''
    palavra_verificada = ''
    i=0
    j=0

    print('Começando a ', rodada + 1, ' rodada. Você tem ', tentativas, 'x tentativas')
    print('Essas são as letras usadas até o momento: ', letras_usadas)

    palavra_testada = input("Digite sua respota: ")

    if len(palavra_testada) != len(palavra):
        print("Digite uma palavra com o numero de letras correto")
        continue
    else:
            
        for letra_palavra in palavra_certa:
            dados1.append(letra_palavra)

        for letra_palavra2 in palavra_testada:
            dados2.append(letra_palavra2)

        while i != len(palavra):
            if dados2[i] in dados1:
                if dados2[i] == dados1[j] and i == j:
                    palavra_formada += dados2[i] + '  '
                    palavra_verificada += dados2[i]
                    dados2[i] = ''
                    dados1[j] = ''
                    i +=1
                    j+=1
                    continue
                if i != j and dados2[i] == dados1[j]:
                    palavra_formada += dados2[i].upper() + '   '
                    palavra_verificada += dados2[i].upper()
                    dados1[j] = ''
                    dados2[i]= ''
                    j=0
                    i+=1
                    continue
                j+=1
            else:
                palavra_formada += '*' + '  '
                letras_usadas.append(dados2[i])
                dados2[i] = ''
                i+=1
        print(palavra_formada)
        if palavra_verificada == palavra_certa:
            print("Parabens, você acertou a palavra: ", palavra)
            break
       
        elif tentativas == 1:
            print("Você perdeu o jogo. A palavra era " + palavra)
            break

        else:
            tentativas -=1
            rodada +=1
            continue



    