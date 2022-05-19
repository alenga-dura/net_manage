# coding=utf8
# Made by Alenga




# IMPORTS
import cmd_command
import os
import time

# ESPACIADO
def spc():
    print('')

# CLEAR TERMINAL
def cls():
    os.system('cls')

# MENU SIMPLE
def menuSimple():
    # MENÚ
    cls()
    print('---MENU MODO SIMPLE---')
    print('Herramienta de administración de red')
    print('1.- Liberar y renovar la dirección IP')
    print('2.- Borrar caché DNS')
    print('3.- Borrar perfiles de redes')
    print('4.- Modo avanzado (No afecta al funcionamiento)')
    print('5.- Salir')
    spc()

# MENU ADVANCED
def menuAdvanced():
    # MENÚ
    cls()
    print('---MENU MODO AVANZADO---')
    print('Herramienta de administración de red')
    print('1.- ipconfig /release /renew')
    print('2.- ipconfig /flushdns')
    print('3.- Script borrar perfiles de redes')
    print('4.- Modo simple (No afecta al funcionamiento)')
    print('5.- Salir')
    spc()

# MENU POSITION VARIABLE
menuPos = 0  # 0=Simple 1=Advanced


while True:

    # IS IN MENU?
    if menuPos == 0:
        menuSimple()
    if menuPos == 1:
        menuAdvanced()

    # INPUT
    optionMenu = ''
    optionMenu = str(input('Introduce el número de la opción que quieras realizar\n'))

    # OPTIONS

    if optionMenu == '1':
        cls()
        print('---Opción 1---')
        cmd_command.wincmd('ipconfig /release')
        cmd_command.wincmd('ipconfig /renew')
        print('Se ha liberado y renovado la dirección IP')
        input('Pulsa Enter para continuar...')

    elif optionMenu == '2':
        cls()
        print('---Opción 2---')
        cmd_command.wincmd('ipconfig /flushdns')
        print('Se ha borrado el caché DNS')
        input('Pulsa Enter para continuar...')

    elif optionMenu == '3':
        cls()
        print('---Opción 3---')
        print('OJO. ¡Debes dar permiso de administrador a la terminar para el correcto funcionamiento de esta opción!')
        input('Pulsa Enter para continuar...')
        # CREATE
        file = open("clearNet.bat", "w")
        file.write('@echo off' + os.linesep)
        file.write('set "params=%*"' + os.linesep)
        file.write(
            r'cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )' + os.linesep)
        file.write(
            r'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles" /f' + os.linesep)
        file.write('netcfg -d' + os.linesep)
        file.write('exit' + os.linesep)
        file.close()

        # EXECUTE
        # cmd_command.wincmd('start /min clearNet.bat ^& exit')
        cmd_command.wincmd('clearNet.bat')

        # CONTADOR
        seconds = int(3)
        while seconds > int(0):
            print(str(seconds) + '...')
            time.sleep(1)
            seconds = seconds - int(1)

        print('Se han borrado los perfiles de redes')

        # DELETE
        spc()
        print('Borrando archivos temporales...')
        os.remove(r'clearNet.bat')
        cls()
        print('Se han borrado los archivos temporales')
        input('Pulsa Enter para continuar...')

        while True:
            cls()
            print('Para completar la eliminación de los perfiles de red debes reiniciar el equipo.')
            rebootInput = input('Desea reiniciar ahora? (s/n) \n')
            if rebootInput == 'S' or rebootInput == 's':
                print('Se va a reiniciar el equipo...')
                cmd_command.wincmd(r'shutdown /r /f')
                time.sleep(1000)
                break
            elif rebootInput == 'N' or rebootInput == 'n':
                break
            else:
                pass

    elif optionMenu == '4':
        if menuPos == 0:
            menuPos = 1
        elif menuPos == 1:
            menuPos = 0

        print(menuPos)

    elif optionMenu == '5':
        cls()
        print('Cerrando programa...')
        input('Pulsa Enter para continuar...')
        quit(0)

    else:
        print('Opción inválida')