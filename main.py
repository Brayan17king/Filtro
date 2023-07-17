import core
import citas

if __name__ == '__main__':
    ciclo = True
    while ciclo:
        ciclo2 = True
        while(ciclo2):
            core.menuPrincipal()
            opcMenu = core.cicloTry(input('\nIngrese una Opcion: '))
            if type(opcMenu) == int:
                if (opcMenu > 0) and (opcMenu<=5):
                    (ciclo2) = False    
        if (opcMenu == 1):
            citas.agregarCitas()
        elif (opcMenu == 2):
            citas.buscarCitas()
        elif (opcMenu == 3):
            citas.editarCitas()
        elif (opcMenu == 4):
            citas.eliminarCitas()
        elif (opcMenu == 5):
            core.clear()
            print('\n 👋 Bye que tengas un excelente dia 🌞')
            ciclo = False
            break
        else:
            print('Opcion no valida❌')
            input('Press Enter to continue...')    
