import os
import core

citas = core.leerArchivo('citas')

def agregarCitas():
    ciclo = True
    while ciclo:
        ciclo2 = True
        while ciclo2:
            cicloV = True
            while cicloV:
                core.clear()
                print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
                print('-'*10, '{:^44}'.format('AGREGAR CITAS MEDICAS📖'), '-'*10)
                print('-'*67)
                nombrePaciente = input('\n🧑 Ingrese el nombre del Paciente: ').title()
                if nombrePaciente in citas:
                    print('\nError... 😬 El usuario ya se encientra registrado..')
                    input('Press Enter to continue..')
                else:
                    cicloV = False    
            valido = nombrePaciente.isalpha()
            if valido == True :
                ciclo2 = False
            else:
                print('Ingrese un nombre valido...')
                input('Press Enter to continue...')    
        ciclo3 = True
        while ciclo3:
            core.clear()
            print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
            print('-'*10, '{:^44}'.format('AGREGAR CITAS MEDICAS📖'), '-'*10)
            print('-'*67)
            añoCita = core.cicloTry(input('\n🗓️ Ingrese el Año de la Cita: '))
            if type(añoCita)== int:
                if (añoCita >= 2023):
                    ciclo3 = False
                else:
                    print(f'Error... El Año {añoCita} ya Paso... ')
                    input('Press Enter to continue...')

        ciclo4 = True
        while ciclo4:
            core.clear()
            print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
            print('-'*10, '{:^44}'.format('AGREGAR CITAS MEDICAS📖'), '-'*10)
            print('-'*67)
            print('\n📆 Los Meses deben ponerse como caracter Numerico 😉 ')
            mesCita = core.cicloTry(input('\n📆 Ingrese el mes de la cita: '))
            if type(mesCita) == int:
                if(mesCita > 0) and (mesCita <=12):
                    ciclo4 = False
                else:
                    print(f'Error... El Mes {mesCita} No existe... ')
                    input('Press Enter to continue...')                       

        ciclo5 = True
        while ciclo5:
            core.clear()
            print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
            print('-'*10, '{:^44}'.format('AGREGAR CITAS MEDICAS📖'), '-'*10)
            print('-'*67)
            diaCita = core.cicloTry(input('\n📅 Ingrese el Dia de la Cita: '))
            if type(diaCita)== int:
                if (mesCita == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                    if (diaCita > 0) and (mesCita <= 31):
                        ciclo5 = False
                    else:
                        print(f'Error... El Dia {diaCita} No existe en el mes: {mesCita}')
                elif (mesCita == 4 or 6 or 9 or 11): 
                    if (diaCita > 0) and (mesCita <=30):
                        ciclo5 = False
                    else:
                        print(f'Error... El Dia {diaCita} No existe en el mes: {mesCita}')       
                elif (mesCita == 2):
                    if (diaCita > 0) and (diaCita <= 28):
                        ciclo5 = False
                    else:
                        print(f'Error... El Dia {diaCita} No existe en el mes: {mesCita}')
                else:
                    print(f'Error... El Dia {diaCita} No existe en el mes: {mesCita}')
                    input('Press Enter to continue...')            

        ciclo6 = True
        while ciclo6:
            core.clear()
            print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
            print('-'*10, '{:^44}'.format('AGREGAR CITAS MEDICAS📖'), '-'*10)
            print('-'*67)
            print('\n🕐 Nuestros Horarios son de 8am a 7pm (Hora Militar)')
            horaCita = core.cicloTry(input('\n🕐 Ingrese la Hora de la Cita: '))
            if type(horaCita)== int:
                if (horaCita >= 8) and (horaCita <= 19):
                    ciclo6 = False
                else:
                    print(f'Error... La Hora {horaCita} no es valida... ')
                    input('Press Enter to continue...')

        ciclo7 = True
        while ciclo7:
            core.clear()
            print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
            print('-'*10, '{:^44}'.format('AGREGAR CITAS MEDICAS📖'), '-'*10)
            print('-'*67)
            minutoCita = core.cicloTry(input('\n⏳ Ingrese el minuto de la Cita: '))
            if type(minutoCita)== int:
                if (minutoCita >= 0) and (minutoCita <= 59):
                    ciclo7 = False
                else:
                    print(f'Error... El minuto {minutoCita} no es valido... ')
                    input('Press Enter to continue...')

        ciclo8 = True
        while ciclo8:
            core.clear()
            print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
            print('-'*10, '{:^44}'.format('AGREGAR CITAS MEDICAS📖'), '-'*10)
            print('-'*67)
            motivo = input('\n💬 Ingrese el motivo de la Consulta: ').capitalize()
            if type(motivo)==str:
                ciclo8 = False
            else:
                print('Ingrese un motivo valido... Solo se permiten caracteres alfabeticos')
                input('Press Enter to continue...')


        fechaCompleta = {'dia': diaCita, 'mes': mesCita, 'año': añoCita}
        horaCompleta = {'hora': horaCita,'minuto': minutoCita}

        citas.update({nombrePaciente:{}})
        citas[nombrePaciente].update({
            'fecha': fechaCompleta,
            'hora': horaCompleta,
            'motivo': motivo
        })
        core.escribirArchivo('citas', core.convertirArchivo(citas))

        print(f'La Cita del Usuario {nombrePaciente} fue Agendada Exitosamente :) ')
        ciclo = False
        break


def buscarCitas():
    ciclo = True
    while ciclo:
        core.clear()
        print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
        print('-'*10, '{:^44}'.format('BUSCAR CITAS MEDICAS🔎'), '-'*10)
        print('-'*67)
        nombrePaciente = (input('\n🧑 Ingrese el nombre del Paciente para Buscar la Cita: ')).title()
        if nombrePaciente in citas:
            core.clear()
            print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
            print('-'*10, '{:^44}'.format('BUSCAR CITAS MEDICAS🔎'), '-'*10)
            print('-'*66)
            print(f'\nEl usuario {nombrePaciente} esta Registrado ✅')
            for items, nombre in enumerate(citas):
                if nombre == nombrePaciente:
                    for dato, valor in citas[nombre].items():
                        if dato == 'fecha':
                            print(f"\n🗓️ Fecha : {valor['dia']}/{valor['mes']}/{valor['año']} ")
                        elif dato == 'hora':
                            print(f"🕦 Hora : {valor['hora']}:{valor['minuto']} ")
                        elif dato == 'motivo':
                            print(f" 💬 Motivo : {valor}")
            input('\nPress enter to continue...')    

        else:
            print(f'El usuario {nombrePaciente} no esta Registrado ❌')
            input('Press Enter to continue...')
        ciclo = False
        break

def editarCitas():
    ciclo = True
    while ciclo:
        ciclo1 = True
        while ciclo1:
            core.clear()
            print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
            print('-'*10, '{:^44}'.format('MODIFICAR CITAS MEDICAS🪪'), '-'*10)
            print('-'*66)
            nombrePaciente = (input('\n🧑 Ingrese el nombre del Paciente: ')).title()
            if nombrePaciente not in citas:
                print(f'\nEl usuario {nombrePaciente} no esta Registrado ❌')
                input('Press Enter to continue...')
            if nombrePaciente in citas:
                print(f'\nEl usuario {nombrePaciente} esta Registrado ✅')
                for items, nombre in enumerate(citas):
                        if nombre == nombrePaciente:
                            for dato, valor in citas[nombre].items():
                                if dato == 'fecha':
                                    print(f"\n1. 🗓️ Modificar Fecha")
                                elif dato == 'hora':
                                    print(f"2. 🕙 Modificar Hora")
                                elif dato == 'motivo':
                                    print(f"3. 📃 Modificar Motivo")
                            print(f'4. 🧑 Modificar Nombre')
                            print(f'5. Salir 🏃‍♂️ ')              
                            index = core.cicloTry(input('\nIngrese una Opcion: '))
                            if type(index)== int:
                                if (index > 0) and (index <= 5):
                                    ciclo1 = False
                            if index == 1:
                                ciclo3 = True
                                while ciclo3:
                                    core.clear()
                                    print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
                                    print('-'*10, '{:^44}'.format('EDITAR FECHA 🗓️'), '-'*10)
                                    print('-'*66)
                                    nuevoAño = core.cicloTry(input('\n🗓️ Ingrese el Año de la Cita: '))
                                    if type(nuevoAño)== int:
                                        if (nuevoAño >= 2023):
                                            ciclo3 = False
                                        else:
                                            print(f'Error... El Año {nuevoAño} ya Paso... ')
                                            input('Press Enter to continue...')

                                ciclo4 = True
                                while ciclo4:
                                    core.clear()
                                    print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
                                    print('-'*10, '{:^44}'.format('EDITAR FECHA 🗓️'), '-'*10)
                                    print('-'*66)
                                    print('\n📆 Los Meses deben ponerse como caracter Numerico ;) ')
                                    mesNuevo = core.cicloTry(input('\n📆 Ingrese Un Mes: '))
                                    if type(mesNuevo) == int:
                                        if(mesNuevo >= 0 and mesNuevo <=12):
                                            ciclo4 = False
                                        else:
                                            print(f'Error... El Mes {mesNuevo} No existe... ')
                                            input('Press Enter to continue...')                       

                                ciclo5 = True
                                while ciclo5:
                                    core.clear()
                                    print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
                                    print('-'*10, '{:^44}'.format('EDITAR FECHA 🗓️'), '-'*10)
                                    print('-'*66)
                                    diaNuevo = core.cicloTry(input('\n📅 Ingrese el Dia de la Cita: '))
                                    if type(diaNuevo)== int:
                                        if (mesNuevo == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                            if (diaNuevo > 0) and (mesNuevo <= 31):
                                                ciclo5 = False
                                            else:
                                                print(f'Error... El Dia {diaNuevo} No existe en el mes: {mesNuevo}')
                                        elif (mesNuevo == 4 or 6 or 9 or 11): 
                                            if (diaNuevo > 0) and (mesNuevo <=30):
                                                ciclo5 = False
                                            else:
                                                print(f'Error... El Dia {diaNuevo} No existe en el mes: {mesNuevo}')       
                                        elif (mesNuevo == 2):
                                            if (diaNuevo > 0) and (diaNuevo <= 28):
                                                ciclo5 = False
                                            else:
                                                print(f'Error... El Dia {diaNuevo} No existe en el mes: {mesNuevo}')
                                        else:
                                            print(f'Error... El Dia {diaNuevo} No existe en el mes: {mesNuevo}')
                                            input('Press Enter to continue...')            
                                        
                                citas[nombre]['fecha'].update({'dia': diaNuevo, 'mes': mesNuevo, 'año': nuevoAño})
                                core.escribirArchivo('citas', core.convertirArchivo(citas))
                                core.clear()
                                print(f"la Fecha Fue Modificada Satisfactoriamente...🌟")
                                input("\nPresione Enter para volver...")
                                ciclo = False
                                break

                            if index == 2:
                                ciclo6 = True
                                while ciclo6:
                                    core.clear()
                                    print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
                                    print('-'*10, '{:^44}'.format('MODIFICAR HORA 🕚'), '-'*10)
                                    print('-'*66)
                                    print('\n🕚 Nuestros Horarios son de 8am a 7pm (Hora Militar)')
                                    nuevaHora = core.cicloTry(input('\n🕚 Ingrese la Hora de la Cita: '))
                                    if type(nuevaHora)== int:
                                        if (nuevaHora >= 8) and (nuevaHora <= 19):
                                            ciclo6 = False
                                        else:
                                            print(f'Error... La Hora {nuevaHora} no es valida... ')
                                            input('Press Enter to continue...')

                                ciclo7 = True
                                while ciclo7:
                                    core.clear()
                                    print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
                                    print('-'*10, '{:^44}'.format('MODIFICAR HORA🕚'), '-'*10)
                                    print('-'*66)
                                    nuevoMinuto = core.cicloTry(input('\n⏳ Ingrese el minuto de la Cita: '))
                                    if type(nuevoMinuto)== int:
                                        if (nuevoMinuto >= 0) and (nuevoMinuto <= 59):
                                            ciclo7 = False
                                        else:
                                            print(f'Error... El minuto {nuevoMinuto} no es valido... ')
                                            input('Press Enter to continue...')

                                citas[nombre]['hora'].update({'hora': nuevaHora, 'minutos': nuevoMinuto })
                                core.escribirArchivo('citas', core.convertirArchivo(citas))
                                core.clear()
                                print(f"la Hora Fue Modificada Satisfactoriamente...🌟")
                                input("\nPresione Enter para volver...")
                                ciclo = False
                                break

                            if index == 3:
                                ciclo8 = True
                                while ciclo8:
                                    core.clear()
                                    print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
                                    print('-'*10, '{:^44}'.format('MODIFICAR MOTIVO🪪'), '-'*10)
                                    print('-'*66)
                                    nuevoMotivo = input('\n🪪 Ingrese el motivo de la Consulta: ').capitalize()
                                    if type(nuevoMotivo)==str:
                                        ciclo8 = False
                                    else:
                                        print('Ingrese un motivo valido... Solo se permiten caracteres alfabeticos')
                                        input('Press Enter to continue...')

                                citas[nombre].update({'motivo': nuevoMotivo })
                                core.escribirArchivo('citas', core.convertirArchivo(citas))
                                core.clear()
                                print(f"El motivo Fue Modificado Satisfactoriamente...🌟")
                                input("\nPresione Enter para volver...")
                                ciclo = False
                                break

                            if index == 4:
                                ciclo2 = True
                                while ciclo2:
                                    core.clear()
                                    print('-'*10, '{:^44}'.format('CENTRO MEDICO 🏣 CAMPUS MD'), '-'*10)
                                    print('-'*10, '{:^44}'.format('MODIFICAR NOMBRE 🧑'), '-'*10)
                                    print('-'*66)
                                    NuevoNombre = input('\n🧑 Ingrese el nombre del Paciente: ').title()
                                    valido = NuevoNombre.isalpha()
                                    if valido == True :
                                        ciclo2 = False
                                    else:
                                        print('Ingrese un nombre valido...')
                                        input('Press Enter to continue...')

                                citas.update({NuevoNombre: citas.pop(nombre)})
                                core.escribirArchivo('citas', core.convertirArchivo(citas))
                                core.clear()
                                print(f"El Nombre Fue Modificado Satisfactoriamente...🌟")
                                input("\nPresione Enter para volver...")
                                break
                                     
                            if index == 5:
                                ciclo = False
                                    


def eliminarCitas():
    ciclo = True
    while ciclo:
        ciclo2 = True
        while ciclo2:
            core.clear()
            print(
                "-" * 10,
                "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                "-" * 10,
            )
            print(
                "-" * 10,
                "{:^44}".format("CANCELAR CITAS 🚫"),
                "-" * 10,
            )
            print("-" * 67)
            nombre = input(
                "\n🧑 Ingrese el nombre de la persona a cancelar su cita: "
            ).title()
            print("\n🤔 Seguro quiere cancelar la cita? \n\n1.Si ✅ \n2.No ❌")
            eliminar = core.cicloTry(input("\nIngrese la Opcion: "))
            if type(eliminar) == int:
                if (eliminar >= 1) and (eliminar <= 2):
                    ciclo2 = False
                else:
                    print("\nOpcion No Valida...")
                    input("\nPress Enter to continue...")
        if eliminar == 1:
            citas.pop(nombre)
            citas.update()
            core.escribirArchivo("citas", core.convertirArchivo(citas))
            core.clear()
            print(f"La Cita de {nombre} ha sido cancelada...✅")
            input("\nPresione Enter para volver...")
            ciclo = False
            break
        elif eliminar == 2:
            core.clear()
            print(
                "-" * 10,
                "{:^44}".format("CENTRO MEDICO 🏣 CAMPUS MD "),
                "-" * 10,
            )
            print(
                "-" * 10,
                "{:^44}".format("CANCELAR CITAS 🚫"),
                "-" * 10,
            )
            print("-" * 67)
            print("\nNo se elimino la cita... 🤗")
            input("\nPresione Enter para volver...")
            ciclo = False
            break