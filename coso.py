#coso.py
#2013 - Giovanni "Talorno" Ricciardi - giovanni.talorno@gmail.com
#modulo di comunicazione tra MPD e un pic con fw custom
#per la visualizzazione su LCD



# ---TODO LIST
# -Implementazione Oggetto tipo "song"
# -Implementazione oggetto tipo "playlist" (come array posizionale di "song")
# -Implementazione parsing delle playlist recuperate da mpc
# -Implementazione convertitore da formato parsato ad oggetto song
# -Implementazione convertitore da formato parsato ad oggetto playlist




#importazione modulo seriale,
import serial
#importazione modulo processi
import subprocess


#dichiarazione/inizializzazione di un oggetto seriale per la comunicazione)
#ser = serial.Serial("/dev/ttyS0	", 38400, 8, "N", 1, timeout=1)

#ser1 = serial.Serial("/dev/pts/4", 38400, 8, "N", 1, timeout=1)
#ser2 = serial.Serial("/dev/pts/5", 38400, 8, "N", 1, timeout=1)

#helpers mpc
def volumeUpBy2():
    return subprocess.check_output(['mpc', 'volume', '+2'])


def volumeDownBy2():
    return subprocess.check_output(['mpc', 'volume', '-2'])


def volumeMute():
    return subprocess.check_output(['mpc', 'volume', '0'])


def volumeLevel(vol):
    return subprocess.check_output(['mpc', 'volume ', vol])


def volumeFull():
    return subprocess.check_output(['mpc', 'volume', '100'])


def getStatus():
    return subprocess.check_output(['mpc'])


def getPlaylist():
    return subprocess.check_output(['mpc', 'playlist'])


def getFilesList(directory):
    return subprocess.check_output(['mpc', 'listall', +directory])


def getCurrentSong():
    return subprocess.check_output(['mpc', 'current'])


def playKey():
    return subprocess.check_output(['mpc', 'play'])


def stopKey():
    return subprocess.check_output(['mpc', 'stop'])


def togglePlay():
    return subprocess.check_output(['mpc', 'toggle'])


def pauseKey():
    return subprocess.check_output(['mpc', 'pause'])


def playPos(pos):
    return subprocess.check_output(['mpc', 'play', pos])


def nextSong():
    return subprocess.check_output(['mpc', 'next'])


def prevSong():
    return subprocess.check_output(['mpc', 'prev'])


def refreshLib():
    return subprocess.check_output(['mpc', 'update'])


def refreshLibDir(directory):
    return subprocess.check_output(['mpc', 'update', directory])


def seekPlus():
    try:
        out = subprocess.check_output(['mpc', 'seek', '+'])
    except CalledProcessError:
        if


def seekMinus():
    return subprocess.check_output(['mpc', 'seek', '-'])


#occhio al parsing del tempo!! oggetto tipo tempo in python?
def seekTime(time):
    return subprocess.check_output(['mpc', 'seek', time])


def seekPercent(percent):
    return subprocess.check_output(['mpc', 'seek', percent])


def shuffle():
    return subprocess.check_output(['mpc', 'shuffle'])


def searchSong(name):
    return subprocess.check_output(['mpc', 'search', + name])


def repeatToggle():
    return subprocess.check_output(['mpc', 'repeat'])


def repeatOn():
    return subprocess.check_output(['mpc', 'repeat', 'on'])


def repeatOff():
    return subprocess.check_output(['mpc', 'repeat', 'off'])


def randomToggle():
    return subprocess.check_output(['mpc', 'random'])


def randomOn():
    return subprocess.check_output(['mpc', 'random', 'on'])


def randomOff():
    return subprocess.check_output(['mpc', 'random', 'off'])


def singleToggle():
    return subprocess.check_output(['mpc', 'single'])


def singleOn():
    return subprocess.check_output(['mpc', 'single', 'on'])


def singleOff():
    return subprocess.check_output(['mpc', 'single', 'off'])


#taglist segnali da seriale
#sintassi: ]#        XXX        YYY
#         token     COMANDO    eventuale parametro
# PLAY ->  ]#001000
# Toggle PLay -> ]#002000
# STOP ->  ]#003000
# PAUSE ->  ]#004000
# PLAY Position ->  ]#005000
# NEXT Song ->  ]#006000
# PREV Song ->  ]#007000
# VOL+ ->  ]#008000
# VOL- ->  ]#009000
# VOL value ->  ]#010000
# VOL Full ->   ]#011000
# MUTE ->  ]#012000
# STATUS ->  ]#013000
# Get PLAYLIST ->  ]#014000
# Get FileList ->  ]#015000
# Get CurrSong ->  ]#016000
# RND on ->  ]#017000
# RND Off -> ]#018000
# RND Toggle -> ]#019000
# Loop on -> ]#020000
# Loop Off > ]#021000
# Loop Toggle -> ]#022000


"""


switch = {
    ']#001000': playKey(),
    ']#002000': togglePlay(),
    ']#003000': stopKey(),
    ']#004000': pauseKey(),
    ']#005000': playPos(pos),
    ']#006000': nextSong(),
    ']#007000': prevSong(),
    ']#008000': volumeUpBy2(),
    ']#009000': volumeDownBy2(),
    ']#010000': volumeLevel(vol),
    ']#011000': volumeFull(),
    ']#012000': volumeMute(),
    ']#013000': getStatus(),
    ']#014000': getPlaylist(),
    ']#015000': getFilesList(dir),
    ']#016000': getCurrentSong(),
    ']#017000': randomOn(),
    ']#018000': randomOff(),
    ']#019000': randomToggle(),
    ']#020000': repeatOn(),
    ']#021000': repeatOff(),
    ']#022000': repeatToggle()
    }
"""

#
#
#Pic Helper

def clearScreen():
    ser1.write('#C')


def posX(x):
	ser1.write('#X'+x)


def posY(y):
	ser1.write('#X'+y)


def cursorHome():
	ser1.write('H')

#
#
##CONTROLLO FINE RIGA VIA PIC O QUI?


def lcdWrite(text):
    print(text)


#VARIE
def designGUI(songname, artist, vol,):
    lcdWrite('|---' + songname + '--by--' + artist + '-----|')
    lcdWrite('|_____________Vol: ' + vol + '___|')


#
#
#CHIAMATE DI TEST
#print (getFilesList(ciao))
#designGUI('antani', 'ugo', '22')

pos = 10
vol = 50
directory = "Remo_Anzovino_Tabu"

print (volumeUpBy2())
print (volumeDownBy2())
print (volumeMute())
#print (volumeLevel(vol))
print (volumeFull())
print (getStatus())
print (getPlaylist())
#print (getFilesList(directory))
print (getCurrentSong())
print (playKey())
print (stopKey())
#print (playPos(pos))
print (nextSong())
print (prevSong())
print (refreshLib())
print (refreshLibDir(directory))
print (seekPlus())
print (seekMinus())