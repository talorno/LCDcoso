#coso.py
#2013 - Giovanni "Talorno" Ricciardi - giovanni.talorno@gmail.com
#modulo di comunicazione tra MPD e un pic con fw custom per la visualizzazione su LCD



# ---TODO LIST
# -Implementazione Oggetto tipo "song"
# -Implementazione oggetto tipo "playlist" (come array posizionale di "song")
# -Implementazione parsing delle playlist recuperate da mpc
# -Implementazione convertitore da formato parsato ad oggetto song
# -Implementazione convertitore da formato parsato ad oggetto playlist









#taglist segnali da seriale
# PLAY ->  ]#pl#[
# Toggle PLay -> ]#togPL#[
# STOP ->  ]#sto#[
# PAUSE ->  ]#pau#[
# PLAY Position ->  ]#plPOSIZIONE#[
# NEXT Song ->  ]#nextSO#[
# PREV Song ->  ]#prevSO#[
# VOL+ ->  ]#volup#[
# VOL- ->  ]#voldo#[
# VOL value ->  ]#volVALORE#[
# VOL Full ->   ]#volFULL#[
# MUTE ->  ]#mute#[
# STATUS ->  ]#sta#[
# Get PLAYLIST ->  ]#getPL#[
# Get FileList ->  ]#getFL#[
# Get CurrSong ->  ]#getSO#[
# RND on ->  ]#rndON#[
# RND Off -> ]#rndOFF#[
# RND Toggle -> ]#rnd#[
# Loop on -> ]#loopON#[
# Loop Off > ]#loopOFF#[
# Loop Toggle -> ]#loop#[



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
	return subprocess.check_output(['mpc volume + 2'])

def volumeDownBy2():
	return subprocess.check_output(['mpc volume - 2'])
	
def volumeMute():
	return subprocess.check_output(['mpc volume 0'])
	
def volumeFull():
	return subprocess.check_output(['mpc volume 0'])
def getStatus():
	return subprocess.check_output(['mpc'])

def getPlaylist():
	return subprocess.check_output(['mpc playlist'])

def getFilesList(dir):	
	return subprocess.check_output(['mpc listall']+dir)

def getCurrentSong():
	return subprocess.check_output(['mpc current'])
	
def playKey():
	return subprocess.check_output(['mpc play'])

def stopKey():
	return subprocess.check_output(['mpc stop'])

def togglePlay():
	return subprocess.check_output(['mpc toggle'])

def pauseKey():
	return subprocess.check_output(['mpc pause'])
		
def playPos(pos):	
	return subprocess.check_output(['mpc play']+pos)

def nextSong():
	return subprocess.check_output(['mpc next'])

def prevSong():
	return subprocess.check_output(['mpc prev'])

def refreshLib():
	return subprocess.check_output(['mpc update'])

def refreshLibDir(directory):
	return subprocess.check_output(['mpc update']+directory)

def seekPlus():
	return subprocess.check_output(['mpc seek +'])

def seekMinus():
	return subprocess.check_output(['mpc seek -'])

def seekPlus():
	return subprocess.check_output(['mpc seek +'])

	#occhio al parsing del tempo!! oggetto tipo tempo in python?
def seekTime(time):
	return subprocess.check_output(['mpc seek']+time)
	
def seekPercent(percent):
	return subprocess.check_output(['mpc seek']+percent)

def shuffle():
	return subprocess.check_output(['mpc shuffle'])

def searchSong(name):
	return subprocess.check_output(['mpc search']+name)

def repeatToggle():
	return subprocess.check_output(['mpc repeat'])

def repeatOn():
	return subprocess.check_output(['mpc repeat on'])

def repeatOff():
	return subprocess.check_output(['mpc repeat off'])

def randomToggle():
	return subprocess.check_output(['mpc random'])

def randomOn():
	return subprocess.check_output(['mpc random on'])

def randomOff():
	return subprocess.check_output(['mpc random off'])

def singleToggle():
	return subprocess.check_output(['mpc single'])

def singleOn():
	return subprocess.check_output(['mpc single on'])

def singleOff():
	return subprocess.check_output(['mpc single off'])











	
#Pic Helper

def clearScreen():
	ser1.write('#C')
	
def posX(x):
	ser1.write('#X'+x)

def posY(y):
	ser1.write('#X'+y)

def cursorHome():
	ser1.write('H')

##CONTROLLO FINE RIGA VIA PIC O QUI?
def lcdWrite(text):
	print(text)

	



#VARIE
def designGUI(songname,artist,vol,):
	lcdWrite('|---'+songname+'--by--'+artist+'-----|')
	lcdWrite('|_____________Vol: '+vol+'___|')


	
	
	
	
	
	
#CHIAMATE
#print (getFilesList(ciao))
designGUI('antani','ugo','22')

	