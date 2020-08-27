class Jugada_Profundidad:
	def __init__(self, j=False, p=0):
		self.jugada = j
		self.profundidad = p

class Inicial_Profundidad:
	def __init__(self, i='_', p=0):
		self.inicial = i
		self.profundidad = p

class PGN_Attributes:
	def __init__(self, dic = {}, p = 0):
		self.jugadas = dic
		self.profundidad = p
