// Define a grammar
grammar Edgar;
r: 
        (( ' ' | TAB )* '\n')* ( paragraph )*
      ;

paragraph:
	( sentence ) ( (' '|'\n')* sentence )* ( ' ' | TAB )* '\n'+
	| ( paren_sentence ( '\n' | '.' )* )+
	| ( ' ' | TAB )* '\n'+
	| ( quoted_paragraph ( '\n' )* )+
	;

sentence:
	'%'? words (':' | '.' )
	;

paren_sentence:
	( ' ' | TAB )* '(' WORD ( ( ' ' | TAB | '\n' | ',' | '[' | ']' | ':' | '-' | '/' )+  WORD )* ( ' ' | TAB )* ')' ';'?
	;

quoted_paragraph:
	( ' ' | TAB )* '“' words ('.')? ( (' '|'\n')* words ('.')? )* '”'	
	;

words:	
	( ' ' | TAB )* word ( ( ' ' | TAB | '\n' | ',' | '&' | '[' | ']' | ':' | '-' | '/' )+  word )* ( ' ' | TAB )*
	;


WHITE   : ( ' ' | '\t' ) ;

TAB	: '\t' ;

word:
	WORD
	| paren_sentence
	;

WORD :
        ULWORD 
	| DOTWORD 
	| EMAIL 
	| URL 
	| VALUE 
	| '[' VALUE ']' 
	| '[' ( ' ' | TAB )*  ']' 
	| [0-9]+ '(' [0-9a-z]+ ')'
	| [0-9a-zA-Z\-\']+
	| '(' [0-9]+ ')'
	| LITERAL
	;

LITERAL:
	  '“' WORD ( [ \t\n]+ WORD)* ('.'|',')? '”'
	| '"' WORD ( [ \t\n]+ WORD)* ('.'|',')? '"'
	| '“+”'
	| '“-”'
	;

fragment
DOTWORD:
	P_O_ | U_S_ | U_S_A_ | I_E_ | E_G_ | D_C_ | I_R_S_ | N_Y_ | B_V_ 
	| N_E_ | N_W_ | S_E_ | S_W_ | J_A_
	| L_P_ | U_S_C_ | NonU_S_ | U_S_based | MRR_ | LTD_ | CORP_ | INC_ 
	| NO_ | ENGR_ | TECH_ | DIR_ | DR_ | ST_ | AVE_ | LN_ 
	| NSWE | A_M_ | P_M_
	| JAN_ | FEB_ | MAR_ | APR_ | MAY_ | JUN_ | JUL_ | AUG_ | SEP_ | OCT_ | NOV_ | DEC_
	;

ULWORD :
	 ( ( [A-Za-z+\*] | LATIN )( [A-Za-z_0-9\-+'&/;\*] | LATIN )* )	 
	 ;

LATIN:
	 ('•' | '—' | '˜' | '™' | '›' | 'œ' | '¡' | '¢' | '¤' | '§' | '©' | 'ª' | '«' | '¬'| '®' | '¯' | '°' | 
	  '±' | 'µ' | '¶' | '·' | 'º' | '»' | '¼' | '½' | '¾' | '¿' | 'À' | 'Á'
	  'É' | 'É' | 'Í' | '×' | 'Ü' | 'Ý' | 'Þ' | 'ß' | 'à' | 'á' | 'â' | 'ã' | 'ä' | 'å' | 'æ' | 'ç' | 'è' | 'é' |
	  'ê' | 'ë' | 'ì' | 'í' | 'î' | 'ï' | 'ð' | 'ñ' | 'ò' | 'ó' | 'ô' | 'õ' | 'ö' | '÷' | 'ø' | 'ù' | 'ú' | 'û' |
	  'ü' | 'ý' | 'þ' | 'ÿ' | '‘' | '’' | '†' | '‡' | '…' | '‰' | '€' | '€' | '™' | '≦' | '≧' | '●' )
	 ;

TWORD :  /* Capital first and upper/lower follows */
	 ( [A-Z][A-Za-z_\-]* )
	 ;


UNICODE:
	   '\u00B7'
	 | '\u0300'..'\u036F'
	 | '\u203F'..'\u2040'
	 ; 

VALUE	 : [0-9]+
	 | '$' ( '\n' | ' ' | '\t' )* [0-9,]+ ( '.' [0-9]+ )*
	 | '$' ( '\n' | ' ' | '\t' )* '(' [0-9,]+ ( '.' [0-9]+ )* ( '\n' | ' ' | '\t' )* ')'
	 | '$' '(' [0-9,]+ ( '.' [0-9]+ )* ')'
	 | [0-9]+ ( '.' [0-9]+ )* ( '\n' | ' ' | '\t' )* '%'
	 | ' (' [0-9]+ ( '.' [0-9]+ )* ( '\n' | ' ' | '\t' )* ')%'
	 | [A-Z]+
	 ;

EMAIL:	[A-Za-z.\-]+ '@' [A-Za-z.\-]+	;
URL  :  'http://' [A-Za-z.\-]+ ;

DOLLAR   : '$'  ( '\n' | ' ' | '\t' )* '-' ( '\n' ) -> skip ;
ALLDASH  : ( '-' )+ -> skip ;
ALLUNSCO : ( '_' )+ -> skip ;
BAR      : ( '|' | ' ' )+ '\n' -> skip ;
BARX	 : '|X|' ' '* '\n' -> skip ;
NO	 : 'No' ' '* '\n' -> skip ;
TOPLINE  : '-----BEGIN PRIVACY-ENHANCED MESSAGE-----' ~'\n'+  -> skip ;


A_M_	: 'A.M.' ;
P_M_	: 'P.M.' ;
P_O_	: 'P.O.' ;
U_S_	: 'U.S.' ;
U_S_A_	: 'U.S.A.' ;
I_E_    : 'i.e.' | 'I.E.' ;
E_G_    : 'e.g.' | 'E.G.' ;
D_C_	: 'D.C.' ;
I_R_S_	: 'I.R.S.' ;
N_Y_	: 'N.Y.' ;
B_V_	: 'B.V.' ;
N_E_	: 'N.E.'  ;
N_W_	: 'N.W.'  ;
S_E_	: 'S.E.'  ;
S_W_	: 'S.W.' ;
J_A_	: 'J.A.' ;
L_P_	: 'L.P.' ;
U_S_C_	: 'U.S.C.' ;
NonU_S_	: 'Non-U.S.' ;
U_S_based : 'U.S.-based' ;
MRR_	: ( 'Mr.' | 'Mrs.' | 'Ms.' | 'MR.' | 'MRS.' | 'MS.' ) ;
LTD_	: 'LTD.' | 'Ltd.' ;
CORP_	: 'Corp.' | 'CORP.' ;
INC_ 	: ( 'Inc.' | 'INC.' ) ;
NO_	: 'No.'  ;
ENGR_	: 'Engr.' ;
TECH_   : 'Tech.' ;
DIR_	: 'Dir.' ;
DR_	: 'Dr.' | 'DR.' ;
ST_	: 'ST.' ;
AVE_    : 'AVE.' ;
LN_	: 'LN.' ;
NSWE	: ( ' N.' | ' S.' | ' W.' | ' E.' ) ;
JAN_	: 'Jan.' | 'JAN.' ;
FEB_	: 'Feb.' | 'FEB.' ;
MAR_	: 'Mar.' | 'MAR_' ;
APR_	: 'Apr.' | 'APR.' ;
MAY_	: 'May ' | 'MAY.' ;
JUN_	: 'Jun.' | 'JUN.' ;
JUL_	: 'Jul.' | 'JUL.' ;
AUG_	: 'Aug.' | 'AUG.' ;
SEP_	: 'Sep.' | 'SEP.' ;
OCT_	: 'Oct.' | 'OCT.' ;
NOV_	: 'Nov.' | 'NOV.' ;
DEC_	: 'Dec.' | 'DEC.' ;
