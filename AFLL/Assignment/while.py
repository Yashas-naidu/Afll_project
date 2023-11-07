import ply.lex as lex
import ply.yacc as yacc

tokens = ('if', 'else', 'condition','statement','statements', 'newline', 
'LPAREN',
'RPAREN', 'curlyopenbracket', 'curlyclosebracket', 'semicolon', )

t_ignore = ' \t'
t_newline = ' \\n'
t_curlyopenbracket = r'\{'
t_curlyclosebracket = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_semicolon = r';'
t_if = r'if'
t_else = r'else'
t_condition = r'condition'
t_statements = r'statements'
t_statement = r'statement'

def p_if_loop(p):
    '''assign : if expression
| if expression newline else statementsub
| if expression else statementsub'''

print("Syntax is correct.")
def p_expression(p):
    '''expression : conditionsub newline statementsub
| conditionsub statementsub'''
def p_conditionsub(p):
    '''conditionsub : LPAREN condition RPAREN 
| LPAREN assign RPAREN
| newline LPAREN condition LPAREN
'''
def p_statementsub(p):
    '''statementsub : curlyopenbracket newline statements semicolon newline 
       curlyclosebracket
| curlyopenbracket newline statements newline 
curlyclosebracket
| curlyopenbracket statement semicolon curlyclosebracket
| curlyopenbracket statement curlyclosebracket
| newline curlyopenbracket statements 
semicolon curlyclosebracket
| newline curlyopenbracket statements curlyclosebracket
| newline curlyopenbracket statements newline 
curlyclosebracket
'''

def p_error(p):
    print("Syntax error")
def t_error(p):
    print("Token error,")
lex.lex()
yacc.yacc()
data = '''if(condition)
{ 
statements;
}
else
{statements;}'''
yacc.parse(data)
