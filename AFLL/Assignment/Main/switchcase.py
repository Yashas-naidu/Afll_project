#G={V,T,P,S}
#V={s,condition,statement}
#T={while,ID,Number,=,{,},(,),;,<=,>=}
#S=s
#P=productions
#s->switch(expression){case expression1:{statement;break;} case expression2:{statement;break;} default:{statement;break;}}
#condition->ID==ID|Number==ID|ID==Number|Number==Number|ID<=Number|ID>=Number|ID<=ID|ID>=ID|
#expression->ID|Number|ID+Number|Number+ID|Number+Number
#expression1->ID|Number|ID+Number|Number+ID|Number+Number
#expression2->ID|Number|ID+Number|Number+ID|Number+Number
#statement->ID=ID;|ID=Number;|ID++|s|statement

import ply.lex as lex
import ply.yacc as yacc


reserved={'switch':'switch','case':'case','default':'default','break':'break'}

tokens=['EQUAL','LPAREN','RPAREN','NUMBER','ID','LCURLY','RCURLY','SEMICOLON','PLUS','LESS','MORE','MINUS','COLON']+list(reserved.values())

t_EQUAL=r'\='
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_LCURLY=r'\{'
t_RCURLY=r'\}'
t_SEMICOLON=r'\;'
t_COLON=r'\:'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_LESS=r'\<'
t_MORE=r'\>'
t_ignore=' '

def t_NUMBER(t):
   r'\d+'
   t.value=int(t.value)
   return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t


def t_error(t):
  print("Illegal character '%s'" % t.value[0]) 
  t.lexer.skip(1)

lexer = lex.lex()

def p_s(p):
 's : sw bl exp br cl ca exp co cl st brk cr ca exp co cl st brk cr def co cl st brk cr cr'

def p_sw(p):
 'sw : switch'

def p_case(p):
 'ca : case'

def p_brk(p):
 'brk : break se'

def p_defa(p):
  'def : default'

def p_exp(p):
 'exp : id'

def p_exp1(p):
 'exp : no'

def p_exp2(p):
 'exp : id pl no'

def p_exp3(p):
 'exp : no pl id'

def p_exp4(p):
 'exp : no pl no'

def p_exp5(p):
 'exp : id mi no'

def p_exp6(p):
 'exp : no mi id'

def p_exp7(p):
 'exp : no mi no'


def p_se(p):
 'se : SEMICOLON'

def p_co(p):
 'co : COLON'



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

def p_st1(p):
 'st : id eq no se st'

def p_st2(p):
 'st : id eq id se st'

def p_st3(p):
 'st : s'

def p_st4(p):
 'st : id pl pl se st'
def p_st5(p):
 'st : pl pl id se st'
def p_st6(p):
 'st : id mi mi se st'
def p_st7(p):
 'st : mi mi id se st'


def p_pl(p):
 'pl : PLUS'
def p_plm(p):
 'mi : MINUS'

def p_st8(p):
 'st : '



def p_gr(p):
 'gr : MORE'

def p_le(p):
 'le : LESS'

def p_error(t):
 if(t):
   print("Syntax error at %s" %t.value) 
 else:
   print("Syntax error: missing token")
parser = yacc.yacc()

while True:
 try:
   s = input('\nCommand > ')
   if s=='exit':
      print("\n")
      break
   else:
      parser.parse(s)
 except EOFError:
    break


