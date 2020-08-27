# List of token names
tokens = (
        'TEXTO',
        'TAG',
        #'PIEZA',
        #'CASILLA',
        #'COLUMNA',
        #'FILA',
        #'CAPTURA',
        #'JAQUE',
        #'JMATE',
        #'JESP',
        'JUGADA',
        'NUMERO',
        'RESULTADO',
        'ABREPAREN',
        'CIERRAPAREN',
        'ABRELLAVE',
        'CIERRALLAVE'
)

# Regex para tokens (en orden de prioridad):

def t_TAG(t):
    r'\[.+\s\".+\"\]'
    return t

def t_NUMERO(t):
    r'(\d+\.(\.\.)?)'
    return t

def t_JUGADA(t):
    r'(P?[a-h]?[1-8]?x?[a-h][18]=[QRBN][+#])|([PRNBQK]?[a-h]?[1-8]?x?[a-h][1-8][+#]?)|(O\-O(\-O)?)'
    return t

def t_ABREPAREN(t):
    r'\('
    return t

def t_CIERRAPAREN(t):
    r'\)'
    return t

def t_ABRELLAVE(t):
    r'\{'
    return t

def t_CIERRALLAVE(t):
    r'\}'
    return t

def t_RESULTADO(t):
    r'1-0 | 0-1 | 1/2-1/2'
    return t

def t_TEXTO(t):
    r'.'
    return t

# La cadena con los caracteres a ignorar (espacios, tabulados y saltos de linea)
t_ignore = "  \t\n"

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    #raise BaseException('Error de lexer')
