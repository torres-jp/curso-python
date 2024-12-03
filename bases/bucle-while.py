## BUCLE WHILE ##

x = 1

while x <= 10:
    print(f'Hola mundo x vale {x}')
    x += 1

    if x == 5:
        break # Esto hace que salga del bucle

    if x == 15:
        continue # Saltea las lineas de aca en adelante
    
else:
    print(f'ya se cumplio la condicion del blucle x es {x}')





while True:
   print('No olvidar de lavarse las manos')
   respuesta = input('Desea salir? (s/n)').strip().lower()

   if respuesta == 's':
     break