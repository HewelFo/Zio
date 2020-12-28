import speech_recognition as Es
import archivoTxT as art

#banco de las palabras claves
Wbank  = ["Zio",
          "write"
    ]
def gtZio(Zio):
    pin = False
    nzio = Zio[0:3]
    #comienza a tomar evaluar las palabras clave
    if(nzio == Wbank[0]):
        Zio = Zio[3:len(Zio)]
        pin = True
    #evalua si se vaa escrbir
    elif(Zio[0:5] == Wbank[1]):
        Zio = Zio[5:len(Zio)]
        pin = True
    else:
        pin = False
    #confirmacion
    if pin == True:
        #comentado para cuando se creen las demas opciones 
        #Menj = ["es", Zio]
        return Zio
    else:
        return "NO NO NO NO NO NO"

def TakeVoice():
	r = Es.Recognizer()
	with Es.Microphone() as base:
		print("all ok :)")
		sound = r.listen(base)
		try:
           FoSound = r.recognize_google(sound)
		   order = gtZio(FoSound)
           art.InserTask(order)            
		except:
			print("didn't get anything")


