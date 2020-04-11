import os

def talk(phrase='Проверка связи', name=('Aleksandr' or 'Anna' or 'Elena' or 'Irina'), volume=0, speed=0):
    # name: Anna, Elena, Irina and Aleksandr
    # volume: (-1, 1)
    # speed: (-1, 1)
    print('[LOG]: ')
    os.system('echo "' + phrase + '" | RHVoice-client -s ' + name + ' -v ' + str(volume) + ' -r ' + str(speed) + ' | aplay')