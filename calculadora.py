adicao = '+'
subtração = '-'
multiplicação = "*"
divisao = "/"

numeros_perm = "2134567890"
operador_perm= "+ - * /"


while True:
    
    
    numero1 = input('insira um numero: ')
    
    numero2 = input('insira outro numero: ')
    
    if numero1 and numero2 not in numeros_perm:
        print("Você digitou numeros inválidos")
        continue
    else:
        num1 = float(numero1)
        num2 = float(numero2)
        
    operador = input('Qual operação deseja realizar?(+ - * /) ')
    
   
    
    
    if operador not in operador_perm:
        print('Você não digitou um operador válido!!!')
        continue
    
    if len(operador) > 1:
        print('digite apenas um operador')
        continue
    
    if operador == "+":
        print(num1 + num2)
        
    
    if operador == "-":
        print(num1 - num2)
    
    
    if operador == "*":
        print(num1 * num2)
        
    
    if operador == "/":
        print(num1 / num2)
        
    
    sair = input("Deseja sair? [s]im: ").lower().startswith('s')
    
    if sair is True:
        break
    
    
    
    
    