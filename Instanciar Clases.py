class Materia:
    def __init__(self,sigla,docente,alumno,nota1,nota2,nota3 ):
        self.sigla =  sigla
        self.docente = docente
        self.alumno = alumno
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3


    def nota_final(self):
       notaf = (self.nota1+self.nota2+self.nota3)//3
       if notaf > 50:
           print('Aprobo')
       else:
           print('Reprobo')


    def __str__(self):
        return "Sigla:{}, Docente:{}, Alumno:{} , Nota1: {}, Nota2: {}, Nota3: {}".format(self.sigla, self.docente, self.alumno, self.nota1, self.nota2, self.nota3)



print("MATERIA")
materia = Materia('INF-142','Ramiro Flores','Juan Perez',60,59,67)
print(materia)
materia.nota_final()
print('-'*25)


class Mascota:
    def __init__(self,nombre,edad,raza, dueño, vacuna):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.dueño = dueño
        self.vacuna = vacuna


    def vacunas(self):
        if self.vacuna == True:
            print('Si esta vacunado')
        else:
            print('Requiere vacuna')


    def __str__(self):
        return "Nombre:{}, Edad:{}, Raza:{}, Dueño:{}, Vacuna:{}".format(self.nombre,self.edad,self.raza,self.dueño,self.vacuna)



print("MASCOTA")
mascota = Mascota('Firulais','3 meses','Pug','Juan Perez',True)
print(mascota)
mascota.vacunas()
