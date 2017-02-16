import unittest
from transcriptor import Transcriptor


class Test(unittest.TestCase):

	def testTranscriptor(self):
		T=Transcriptor('MA1112.pdf','Salida')
		self.assertNotEqual(T.f,'Error',"Error en la transcripcion")
	
	def testMalicioso(self):
		#Se prueba con un archivo que no existe
		T=Transcriptor('QWERTY','Salida')
		self.assertEqual(T.f,'Error',"Error en apertura de archivo")
		
			
		
