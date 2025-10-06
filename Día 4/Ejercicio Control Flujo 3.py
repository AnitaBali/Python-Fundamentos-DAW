habla_ingles = False
sabe_python = True

if sabe_python==True and habla_ingles==True:
        print("Cumples con los requisitos para postularte")
elif sabe_python==True and habla_ingles==False:
        print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python==False and habla_ingles==True:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
