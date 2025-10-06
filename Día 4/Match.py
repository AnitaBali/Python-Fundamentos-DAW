cliente={'nombre':'Ana',
         'edad':35,
         'puesto':'programadora'}

pelicula={'titulo':'Big Fish',
          'ficha':{'protagonista':'Jude Law',
                   'director':'Tim Burton'}}

elementos=[cliente,pelicula,"libro"]

for e in elementos:
    match e:
        case{'nombre':nombre,
             'edad':edad,
             'puesto':puesto}:
            print("Es un cliente")
            print(nombre,edad,puesto)
        case{'titulo':titulo,
             'ficha':{'protagonista':protagonista,
                      'director':director}}:
            print("Es una película")
            print(titulo,protagonista,director)
        case _:
            print("No se que es esto")