nome = input('qual o seu nome? ')
idade = input('qual a sua idade? ')

if nome and idade:
    print(f"seu nome é {nome}")
    print(f"seu nome investido é {nome[ : : -1]}" )
    if " " in nome:
        print("seu nome contêm espaços")
        
    else:
        print('seu nome não contêm espaços')
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print('você deixou um dos campos vazio')
    