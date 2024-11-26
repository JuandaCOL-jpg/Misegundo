import pygame 

pygame.init()
screen = pygame.display.set_mode((450,450))
#COMANDO PARA PONER UN TITULO A LA PESTAÑA
pygame.display.set_caption("Triqui Juan")

fondo = pygame.image.load("C:\\Users\\IK\\Downloads\\imagenes\\Tablero.png")
circulo = pygame.image.load("C:\\Users\\IK\\Downloads\\imagenes\\Circulo.png")
equis = pygame.image.load("C:\\Users\\IK\\Downloads\\imagenes\\Equis.png")

#COMANDO PARA DARLE TAMAÑO A LAS IMAGENES
fondo = pygame.transform.scale(fondo, (450,450))
circulo = pygame.transform.scale(circulo, (125,125))
equis = pygame.transform.scale(equis, (125,125))

#Vamos a crear una matriz en la que vamos a graficar las imagenes o los elemntos
coor = [[(40,50),(165,50),(290,50)],
        [(40,175),(165,175),(290,175)],
        [(40,300),(165,300),(290,300)]]

#Matriz para almacenar las jugadas que se hagan
tablero =  [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

turno = "X"

#vARIABLE DE CONTROL
game_over = False

#Facilitar los x por segundo a los que trabajara el video juego
clock = pygame.time.Clock()

#Graficar
def graficar_board():
    screen.blit(fondo, (0,0))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == "X":
                dibujar_x(fila,columna)
            elif tablero[fila][columna] == "O":
                dibujar_o(fila,columna)
    
#Vamos a graficar las X
def dibujar_x(fila,columna):
    screen.blit(equis, coor[fila][columna])
#Vamos a graficar los circulos O
def dibujar_o(fila,columna):
    screen.blit(circulo, coor[fila][columna])

#funcion para verificar el ganador
def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    else:
        return False

while not game_over:
    #Aseguramos de que el juego siempre corra a 30 fotogramas por segundo en cualquier dispositivo
    clock.tick(30)
    #Capturamos los eventos ya sea un clic en la pantalla o cerrar el juego
    for event in pygame.event.get():
        #Comando para decir que si el usuario cierra el juego entonces game over pasa a ser true y finaliza el juego
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN: #Si el evento es igual a un click dell mouse entoncees:
            mouseX, mouseY = event.pos
            if (mouseX >= 40 and mouseX < 415) and(mouseY >= 50 and mouseY < 425):
                fila = (mouseY - 50) // 125
                columna = (mouseX - 40) // 125
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = turno
                    #Verificamos despues de que haya pasado un turno y antes de que pase al siguiente(Verificamos ganador)
                    fin_juego = verificar_ganador()
                    if fin_juego:
                        print(f"El jugador {turno} ha ganado!!")
                        print("Hola soy JUANNNN")
                        game_over = True
                turno = "O" if turno == "X" else "X"
    #Vamos a graficar los elemntos
    graficar_board()
    #COMANDO PARA ACTUALIZAR LA CONSOLA
    pygame.display.update()
pygame.quit()