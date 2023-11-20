from turtle import Turtle

t = Turtle()
t.speed(1)

while True:
    print('-----------------------------------------------')
    print()
    print('Para qual direção devemos ir?')
    direcao = input('(F: Frente) ou (T: Trás): ').lower()[0]

    if direcao == 'f':
        distancia = int(input('Quantos pixels devemos mover para frente: '))

        # Recebe a direção da rotação e o valor
        girar_para_lado = input('Rotacional para (D: direita), (E: esquerda), (N: Sem rotacionar): ').lower()[0]

        if girar_para_lado == 'd':
            angulo = int(input('Quanto para direita devemos rotacionar: '))
            t.right(angulo)
            t.forward(distancia)

        elif girar_para_lado == 'e':
            angulo = int(input('Quanto para esqueda devemos rotacionar: '))
            t.left(angulo)
            t.forward(distancia)

        else:
            t.forward(distancia)

    elif direcao == 't':
        distancia = int(input('Quantos pixels devemos mover para trás: '))

        # Recebe a direção da rotação e o valor
        girar_para_lado = input('Rotacional para (D: direita), (E: esquerda), (N: Sem rotacionar): ').lower()[0]

        if girar_para_lado == 'd':
            angulo = int(input('Quanto para direita devemos rotacionar: '))
            t.right(angulo)
            t.backward(distancia)

        elif girar_para_lado == 'e':
            angulo = int(input('Quanto para esqueda devemos rotacionar: '))
            t.left(angulo)
            t.backward(distancia)

        else:
            t.backward(distancia)
    
    print()
    resposta = input('Continuar andando? ')
    if resposta not in ('sim', 's'):
        break



    
