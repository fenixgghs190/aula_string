#Pegar informações do usuário através do input

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
dia = input('Digite seu dia de nascimento: ')
mes = input('Digite seu mes de nascimento: ')
ano = input('Digite seu ano de nascimento: ')
universidade = input('Digite sua universidade: ')

#Construir o endereço de e-mail, contendo nome, sobrenome e universidade e apresentar ao usuário

email = nome.lower() + sobrenome.lower() + '@' + universidade.lower() + '.br'
print('Seu email institucional é:', email)

#Construir a senha, contendo as letras "A, E, I, O, U", e na frente das letras contendo a quantidade de vogais existentes no e-mail e apresentar a senha ao usuário

senha = "a" + str(email.count('a')) + "e" + str(email.count('e')) + "i" + str(email.count('i')) + "o" + str(email.count('o')) + "u" + str(email.count('u'))
print('Sua senha é:', senha)

#Transcrever a data de nascimento do usuário

nascimento = dia + "/" + mes + "/" + ano
print('Sua data de nascimento é: ', nascimento)


