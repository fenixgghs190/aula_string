#Pegar informações do usuário através do input

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
dia = input('Digite seu dia de nascimento: ')
mes = input('Digite seu mes de nascimento: ')
ano = input('Digite seu ano de nascimento: ')
universidade = input('Digite sua universidade: ')

#Construir o endereço de e-mail, contendo nome, sobrenome e universidade

email = nome.lower() + '.' + sobrenome.lower() + '@' + universidade.lower() + '.br'

#Construir a senha, contendo as letras "A, E, I, O, U", e na frente das letras contendo a quantidade de vogais existentes no e-mail

senha = "a" + str(email.count('a')) + "e" + str(email.count('e')) + "i" + str(email.count('i')) + "o" + str(email.count('o')) + "u" + str(email.count('u'))

#Os colchetes {} substituem o espaço pela variavel apresentada pelo comando ".format(string)", substitue pela string escolihida
#Pode-se também colocar 2 colchetes na string, e adicionar duas variáveis de forma consecutiva, por exemplo "'Seu email é {} e sua senha é {}'.format(email, senha)"
print('Seu email é: {}'.format(email))
print('Sua senha é: {}'.format(senha))
print('Sua data de nascimento é: {}/{}/{}'.format(dia, mes, ano))
print('Seu nome completo é: {} {}'.format(nome, sobrenome))
