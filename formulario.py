nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
dia = input('Digite seu dia de nascimento: ')
mes = input('Digite seu mes de nascimento: ')
ano = input('Digite seu ano de nascimento: ')
universidade = input('Digite sua universidade: ')

email = nome + sobrenome + '@' + universidade + '.br'
print('Seu email institucional é:', email)
senha = str(email.count('a')) + str(email.count('e')) + str(email.count('i')) + str(email.count('o')) + str(email.count('u'))
print('Sua senha é:', senha)


