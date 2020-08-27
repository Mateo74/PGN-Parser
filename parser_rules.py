from lexer_rules import tokens
from clases import *
import sys

def p_pgn(p) :
	'pgn : partida pgn'
	dic = p[2].jugadas
	ini = p[1].inicial
	if ini not in dic:
		dic[ini] = 1
	else:
		dic[ini] += 1
	prof = max(p[1].profundidad, p[2].profundidad)
	p[0] = PGN_Attributes(dic, prof)


def p_pgnPartida(p) :
	'pgn : partida'
	dic = { p[1].inicial : 1 }
	prof = p[1].profundidad
	p[0] = PGN_Attributes(dic, prof)


def p_partida(p) :
	'partida : tags secuencia RESULTADO'
	p[0] = p[2]

def p_tags(p) :
	'tags : TAG tags'

def p_tagsEmpty(p) :
	'tags :'

def p_secuenciaTurnos(p) :
	'secuencia : turno secuencia'
	ini = p[1].inicial
	prof = max(p[1].profundidad, p[2].profundidad)
	p[0] = Inicial_Profundidad(ini, prof)


def p_secuenciaTurno(p) :
	'secuencia : turno'
	p[0] = p[1]

def p_turno(p) :
	'turno : NUMERO turno2'
	p[0] = p[2]

def p_turno2(p) :
	'turno2 : JUGADA posibleComentario turno2'
	ini = p[1]
	prof = max(p[2].profundidad, p[3].profundidad)
	p[0] = Inicial_Profundidad(ini, prof)

def p_turno2Empty(p) :
	'turno2 :'
	p[0] = Inicial_Profundidad()

def p_posibleComentarioEmpty(p) :
	'posibleComentario :'
	p[0] = Jugada_Profundidad()

def p_posibleComentarioComentario(p) :
	'posibleComentario : comentario'
	p[0] = p[1]

def p_comentarioParen(p) :
	'comentario : ABREPAREN contenido CIERRAPAREN'
	p[0] = p[2]

def p_comentarioLlave(p) :
	'comentario : ABRELLAVE contenido CIERRALLAVE'
	p[0] = p[2]

def p_contenidoPalabra(p) :
	'contenido : palabra contenido'
	if p[2].jugada:
		p[0] = Jugada_Profundidad(True, p[2].profundidad)
	elif p[1]:
		p[0] = Jugada_Profundidad(True, 1)
	else:
		p[0] = Jugada_Profundidad()

def p_contenidoComentario(p) :
	'contenido : comentario contenido'
	p[0] = Jugada_Profundidad()
	if p[1].jugada:
		p[0] = Jugada_Profundidad(True, p[1].profundidad + 1)
	if p[2].jugada:
		p[0].jugada = True
		p[0].profundidad = max(p[0].profundidad, p[2].profundidad)


def p_contenidoEmpty(p):
	'contenido :'
	p[0] = Jugada_Profundidad()

def p_palabra_texto(p):
	'palabra : TEXTO'
	p[0] = False

def p_palabra_jugada(p):
	'palabra : JUGADA'
	p[0] = True

def p_palabra_numero(p):
	'palabra : NUMERO'
	p[0] = False

def p_palabra_tag(p):
	'palabra : TAG'
	p[0] = False

def p_palabra_resultado(p):
	'palabra : RESULTADO'
	p[0] = False

def p_error(t):
	"""
	Si llega al final del archivo, t sera igual a None. Pareceria (puede fallar) que eso solo pasa cuando
	hubo un comentario sin cerrar.
	"""
	if t:
		print("Error de sintaxis: '%s' inesperado." % t.value)
	else:
		print("Error: EOF no esperado")
	sys.exit()
