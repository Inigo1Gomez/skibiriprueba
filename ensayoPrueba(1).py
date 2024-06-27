nominaTrabajadores = []
cargos = ("CEO","Desarrollador","Analista de datos")
DESCUENTO_SALUD = 0.07
DESCUENTO_AFP = 0.12

def registrarTrabajador():
    nombre = input("INGRESE NOMBRE ")
    print("CARGOS DISPONIBLES")
    print("******************")
    for i in range(len(cargos)):
        print(i, cargos[i])
    posicionCargo = int(input("SELECCIONE POSICIÓN DEL CARGO: "))
    cargo = cargos[posicionCargo]
    sueldoBruto=int(input("INGRESE SUELD BRUTO $"))
    descuentoSalud = int(sueldoBruto * 0.07)
    descuentoAfp = int(sueldoBruto * 0.12)
    liquidoPagar = int(sueldoBruto - descuentoSalud - descuentoAfp)
    trabajador = [nombre,cargo,sueldoBruto,descuentoSalud, descuentoAfp, liquidoPagar]
    nominaTrabajadores.append(trabajador)


def listarTrabajadores():
    print("TRABAJADOR\tCARGO\tSUELDO BRUTO\tDESC.SALUD\tDESC.AFP\tLÍQUIDO A PAGAR")
    print("---------------------------------------------------------------")

    for i in range(len(nominaTrabajadores)):
        print(nominaTrabajadores[i][0],end="\t\t")
        print(nominaTrabajadores[i][1],end="\t")
        print(nominaTrabajadores[i][2],end="\t\t")
        print(nominaTrabajadores[i][3],end="\t\t")
        print(nominaTrabajadores[i][4],end="\t\t\t")
        print(nominaTrabajadores[i][5],end="\t\t\t")
        print()
        print("---------------------------------------------------------------")

def imprimiPlanillaSueldos():
    op = int(input("(1)MOSTRAR TODOS LOS CARGOS (2)MOSTRAR UN CARGO ESPECÍFICO"))
    if op ==1:
        print("TRABAJADOR\tCARGO\tSUELDO BRUTO\tDESC.SALUD\tDESC.AFP\tLÍQUIDO A PAGAR")
        print("---------------------------------------------------------------")

        for i in range(len(nominaTrabajadores)):
            print(nominaTrabajadores[i][0],end="\t\t")
            print(nominaTrabajadores[i][1],end="\t")
            print(nominaTrabajadores[i][2],end="\t\t")
            print(nominaTrabajadores[i][3],end="\t\t")
            print(nominaTrabajadores[i][4],end="\t\t\t")
            print(nominaTrabajadores[i][5],end="\t\t\t")
            print()
            print("---------------------------------------------------------------")
    
    elif op==2:
        cargoBuscar = input("INGRESE CARGO A BUSCAR ")
        if cargoBuscar in cargos:
            print("CARGO EXISTENTE")
            posicionCargo = cargos.index(cargoBuscar)
            cargoSeleccionado = cargos[posicionCargo]
            print(F"TRABAJADORES CON EL CARGO {cargoBuscar}")

            for trabajador in nominaTrabajadores:
                if trabajador [1] == cargoSeleccionado:
                    print(trabajador[0],end="\t\t")
                    print(trabajador[1],end="\t\t")
                    print(trabajador[2],end="\t\t")
                    print(trabajador[3],end="\t\t")
                    print(trabajador[4],end="\t\t")
                    print(trabajador[5],end="\t\t")
                    print()
                    print("-----------------------------------------------------------------------")
        else:
            print("CARGO NO EXISTE")

def exportarATXT():
    with open('nomina_trabajadores.txt', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["TRABAJADOR", "CARGO", "SUELDO BRUTO", "DESC.SALUD", "DESC.AFP", "LÍQUIDO A PAGAR"])
        for trabajador in nominaTrabajadores:
            writer.writerow(trabajador)
    print("Nómina exportada a 'nomina_trabajadores.txt'")

while True:
    print("(1)REGISTRAR TRABAJADOR")
    print("(2)LISTAR TODOS LOS TRABAJADORES")
    print("(3)IMPRIMIR PLANILLA DE SUELDOS")
    print("(4)SALIR")
    print("(5)Exportar a .txt")
    opcion = int(input("INGRESE OPCIÓN: "))

    if opcion==1:
        registrarTrabajador()
    elif opcion==2:
        listarTrabajadores()
    elif opcion==3:
        imprimiPlanillaSueldos()
    elif opcion==4:
        break
    elif opcion==5:
        exportarATXT