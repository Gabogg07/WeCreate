import unittest
from transcriptor import Transcriptor


class Test(unittest.TestCase):

	def testTranscriptor(self):
		T=Transcriptor('MA12112.pdf','Salida')
		self.assertNotEqual(T.f,'Error',"Error en la transcripcion")
		
