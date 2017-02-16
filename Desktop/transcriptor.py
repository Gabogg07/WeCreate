import textract

from asyncore import write
from django.contrib.sessions.backends import file

class Transcriptor(object):
    def __init__(self, file ,salida,text=None,f=None):
        self.file=file
        self.salida=salida
        self.f= open(self.salida ,'wb')

        try:
            self.text=textract.process(file)
            self.f.write(self.text)
            
        except:
            print("Archivo PDF Invalido")
