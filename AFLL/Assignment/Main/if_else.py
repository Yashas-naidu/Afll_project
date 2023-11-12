import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'if': 'IF',
    'else': 'ELSE'
}

tokens = ['EQUAL', 'LPAREN', 'RPAREN', 'NUMBER', 'ID', 'LCURLY', 'RCURLY', 'SEMICOLON', 'PLUS', 'LESS', 'MORE', 'MINUS'] + list(reserved.values())

t_EQUAL = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_SEMICOLON = r'\;'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LESS = r'\<'
t_MORE = r'\>'
t_ignore = ' '

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_s(p):
    '''s : i bl con br cl st cr el cl st cr
    '''

def p_i(p):
    'i : IF'

def p_el(p):
    'el : ELSE'

def p_con1(p):
    'con : id eq eq id'

def p_con2(p):
    'con : id eq eq no'

def p_con3(p):
    'con : no eq eq id'

def p_con4(p):
    'con : no eq eq no'

def p_con5(p):
    'con : id le eq no'

def p_con6(p):
    'con : id gr eq no'

def p_con7(p):
    'con : id le eq id'

def p_con8(p):
    'con : id gr eq id'

def p_con9(p):
    'con : id le no'

def p_con10(p):
    'con : id gr no'

def p_con11(p):
    'con : id le id'

def p_con12(p):
    'con : id gr id'

def p_id(p):
    'id : ID'

def p_eq(p):
    'eq : EQUAL'

def p_no(p):
    'no : NUMBER'

def p_cl(p):
    'cl : LCURLY'

def p_cr(p):
    'cr : RCURLY'

def p_bl(p):
    'bl : LPAREN'

def p_br(p):
    'br : RPAREN'

def p_st(p):
    '''st : id eq no SEMICOLON
          | id eq id SEMICOLON
          | s
          | id PLUS PLUS SEMICOLON
          | PLUS PLUS id SEMICOLON
          | id MINUS MINUS SEMICOLON
          | MINUS MINUS id SEMICOLON
          | empty
    '''

def p_empty(p):
    'empty :'
    pass

def p_gr(p):
    'gr : MORE'

def p_le(p):
    'le : LESS'

def p_error(t):
    if t:
        print("Syntax error at %s" % t.value)
    else:
        print("Syntax error: missing token")

parser = yacc.yacc()

while True:
    try:
        s = input('\nCommand > ')
        if s == 'exit':
            print("\n")
            break
        else:
            parser.parse(s)
    except EOFError:
        break
