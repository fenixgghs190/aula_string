#Pegar nome, senha e domínio do usuário

nome = input('Qual o seu nome?: ')

senha = input('Insira sua senha: ')

dominio = input('insira o dominio: ')

print('Olá',nome,'! Seja bem vindo!')
print('Sua senha é: ', senha)
print('Seu domínio é: ', dominio)

#Criação do email com "@" e ".com.br"

email = nome.lower() + '@' + dominio + '.com.br'

print('email criado com sucesso:' ,email)

palavra = 'teste'

#Colocar a string como tudo maiúsculo

print ('Colocando o texto em letra maiúscula: ', palavra.upper())

palavra2 = 'TESTE'

#Colocar a string como tudo minúsculo

print ('Colocando o texto em letra minúscula: ', palavra2.lower())

#Exercício: Fazer uma senha, sendo ela formada pela quantidade de vogais do email criado, ou seja, a quantidade de letra a + e + i + o + u

senha_criada = 'a' + str(email.count('a')) + 'e' + str(email.count('e')) + 'i' + str(email.count('i')) + 'o' + str(email.count('o')) + 'u' + str(email.count('u'))

print('Sua senha criada é: ', senha_criada)
