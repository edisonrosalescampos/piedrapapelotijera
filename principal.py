import random

def jugar():
  opciones    = ["piedra", "papel", "tijera"]
  computadora = opciones[random.randint(0, 2)] 

  print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL Y TIJERA\n")

  usuario = input("Escriba piedra, papel o tijera: ")

  print(f"Tú: {usuario} vs PC: {computadora}")

  # Empate
  if usuario == computadora:
    print("¡Empate!")

  # Piedra
  if usuario == opciones[0]:
    if computadora == opciones[1]:
      print("¡Perdiste!")
    if computadora == opciones[2]:
      print("¡Ganaste!")

  # Papel
  if usuario == opciones[1]:
    if computadora == opciones[0]:
      print("¡Ganaste!") 
    if computadora == opciones[2]:
      print("¡Perdiste!")  

  # Tijera
  if usuario == opciones[2]:
    if computadora == opciones[0]:
      print("¡Perdiste!")
    if computadora == opciones[1]:
      print("¡Ganaste!")

jugar()