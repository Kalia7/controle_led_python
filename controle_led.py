import serial

arduino = serial.Serial('COM6', 9600, timeout=1)
print('Arduino Conectado')

while True:
    cmd = input('Digite "L" para ligar, "D" para desligar ou "S" para sair: ').strip().upper()

    if cmd == 'L':
        arduino.write('L'.encode())  # envia o byte 'L'
        print('LED ligado!')
    elif cmd == 'D':
        arduino.write('D'.encode())  # envia o byte 'D'
        print('LED desligado!')
    elif cmd == 'S':
        print('Saindo...')
        break
    else:
        print('Comando inválido.')

 
arduino.close()