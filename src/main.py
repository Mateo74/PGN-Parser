import ply.lex as lex
import ply.yacc as yacc
import parser_rules
import lexer_rules
import pprint
import sys



lexer = lex.lex(module=lexer_rules)

name = input("Path al archivo: ")
with open(name, 'r') as input_pgn:
	data = input_pgn.read()
lexer.input(data)

# Este ciclo va a imprimir el contenido del archivo, pero tokenizado (para debuggear si estamos tokenizando bien).
while True:
	tok = lexer.token()
	if not tok:
	    break      # No more input
	#print(tok) #Para imprimir el archivo tokenizado hay que descomentar esta linea

parser = yacc.yacc(module=parser_rules)
pp = pprint.PrettyPrinter(indent=1)

try:
	expression = parser.parse(data, lexer)
	#pp.pprint(expression)
	print("La jugada inicial mas popular fue {0}, y la maxima profundidad {1}".format(max(expression.jugadas, key=expression.jugadas.get), expression.profundidad))

except BaseException as e:
	print(e)
