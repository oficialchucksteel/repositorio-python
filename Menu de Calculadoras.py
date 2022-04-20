
nome = str(input('\n Olá, qual é o seu nome: '))

print('\n{:=^32}'.format('MENU'))
opcao = (input('\n 1. Calculadora básica \n 2. Calculador de Potência \n 3. Calculador de Raiz Quadrada \n\n Digite aqui uma das opções:'))

if opcao == '1':
    print('\n{:=^40}'.format('Calculadora básica'))
    n1 = int(input('\n Olá {}, digite o primeiro valor: '.format(nome)))
    n2 = int(input(' Olá {}, digite o segundo valor: '.format(nome)))
    so = n1 + n2
    sb = n1 - n2
    di = n1 / n2
    mu = n1 * n2
    print('\n {} + {} = {} \n {} - {} = {} \n {} / {} = {} \n {} * {} = {}'.format(n1, n2, so, n1, n2, sb, n1, n2, di, n1, n2, mu))

elif opcao == '2':
    print('\n{:=^40}'.format('Calculador de Potência'))
    b = float(input('\n Olá {}, digite a base da potência: '.format(nome)))
    e = float(input(' {}, agora digite o expoente da potência: '.format(nome)))
    p = b ** e
    print('\n {}, {} elevado a {} é igual a {}'.format(nome, b, e, p))

elif opcao == '3':
    print('\n{:=^40}'.format('Calculador de Raiz Quadrada'))
    n = float(input('\n Olá {}, digite o valor: '.format(nome)))
    r = n ** (1/2)
    print('\n {}, a raiz quadrada de {} é o numero {}'.format(nome, n, r))

else:
    print('\n Meu caro {}, eu te dei 3 opções, até contar até o número 3 custa. :-('.format(nome))

pause = input('\n{:=^40}\n\n Aperte Enter para sair'.format('Chuck Steel'))
