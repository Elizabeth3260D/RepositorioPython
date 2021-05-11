print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("OBTENCION DE AREA Y PERIMETROS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('Hola soy un cambio')
print("hola elizabeth soy belen buenas noches :)")

print('')
print('Opiones:')
print("1.Cuadrado")
print("2.Triangulo")
print("3.Rectangulo")

while 0<=3:
  

  print('')
  opcion=int(input('Elige una opcion: '))

  print('')


  def miCuadrado():
  
    figura1=int(input('Coloca la medida del lado del  cuadrado: '))
    resultado=figura1*figura1
    print(str("El area del cuadrado es: "),int(resultado))
    resultadoA=figura1*4
    print(str("El perimetro del cuadrado es: "),int(resultadoA))

  print('')
  def miTriangulo():
 
    figura2=int(input('Captura la medida de la base del triangulo: '))
    figura4=int(input('Captura la medida de la altura del triangulo: '))
    resultado3=figura2*figura4/2
    print(str("El area del triangulo es: "),int(resultado3))
    resultadoA=figura2+figura4+figura4
    print(str("El perimetro del triangulo es: "),int(resultadoA))


  print('')
  def miRectangulo():
 
    figura3=int(input('Captura la medida de la base: '))
    figura4=int(input('Captura la medida de la altura:'))
    resultado4=figura3*figura4
    print(str("El area del rectangulo es: "),int(resultado4))
    resultadoA=figura3*2+figura4*2
    print(str("El perimetro del rectangulo es: "),int(resultadoA))
  

  if opcion==1:
    miCuadrado()
  elif opcion==2:
    miTriangulo()
  elif opcion==3:
    miRectangulo()

  print('')
  print('NOTA: Si decea salir escriba SI o si, de lo contrario escriba no o NO')
  print('')
  salir=(input('Desea salir?'))
  if salir=="si" or salir=="SI":
    break
