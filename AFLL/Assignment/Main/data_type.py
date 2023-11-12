import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'let': 'LET',
    'const': 'CONST'
}

tokens = ['ID', 'EQUAL', 'SEMICOLON', 'NUMBER', 'STRING', 'BOOLEAN', 'ARRAY'] + list(reserved.values())

t_EQUAL = r'\='
t_SEMICOLON = r'\;'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = str(t.value[1:-1])  # Remove double quotes
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = (t.value == 'true')
    return t

def t_ARRAY(t):
    r'array'
    return t

t_ignore = ' '

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, column {find_column(t.lexer.lexdata, t)}")
    t.lexer.skip(1)

def find_column(input_text, token):
    last_cr = input_text.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

lexer = lex.lex()

def p_declaration(p):
    '''
    declaration : variable_declaration
                | type_declaration
    '''

def p_variable_declaration(p):
    '''
    variable_declaration : LET ID optional_assignment SEMICOLON
                        | CONST ID optional_assignment SEMICOLON
    '''

def p_optional_assignment(p):
    '''
    optional_assignment : EQUAL expression
                       | 
    '''

def p_type_declaration(p):
    '''
    type_declaration : ID EQUAL expression SEMICOLON
    '''

def p_expression(p):
    '''
    expression : NUMBER
               | STRING
               | BOOLEAN
               | ID
               | ARRAY
    '''

def p_error(p):
    print(f"Syntax error at line {p.lineno}, column {find_column(parser.lexdata, p)}")

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
