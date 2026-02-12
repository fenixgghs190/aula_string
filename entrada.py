nome = input('Qual o seu nome?: ')

senha = input('Insira sua senha: ')

dominio = input('insira o dominio: ')

print('Olá',nome,'! Seja bem vindo!')
print('Sua senha é: ', senha)
print('Seu domínio é: ', dominio)

email = nome + '@' + dominio + '.com.br'

print('email criado com sucesso:' ,email)
