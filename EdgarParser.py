# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .EdgarListener import EdgarListener
else:
    from EdgarListener import EdgarListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3Q")
        buf.write("\u00b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\7\2\30\n")
        buf.write("\2\f\2\16\2\33\13\2\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3")
        buf.write("\3\3\7\3%\n\3\f\3\16\3(\13\3\3\3\7\3+\n\3\f\3\16\3.\13")
        buf.write("\3\3\3\7\3\61\n\3\f\3\16\3\64\13\3\3\3\6\3\67\n\3\r\3")
        buf.write("\16\38\3\3\3\3\7\3=\n\3\f\3\16\3@\13\3\6\3B\n\3\r\3\16")
        buf.write("\3C\3\3\7\3G\n\3\f\3\16\3J\13\3\3\3\6\3M\n\3\r\3\16\3")
        buf.write("N\3\3\3\3\7\3S\n\3\f\3\16\3V\13\3\6\3X\n\3\r\3\16\3Y\5")
        buf.write("\3\\\n\3\3\4\5\4_\n\4\3\4\3\4\3\4\3\5\7\5e\n\5\f\5\16")
        buf.write("\5h\13\5\3\5\3\5\3\5\6\5m\n\5\r\5\16\5n\3\5\7\5r\n\5\f")
        buf.write("\5\16\5u\13\5\3\5\7\5x\n\5\f\5\16\5{\13\5\3\5\3\5\5\5")
        buf.write("\177\n\5\3\6\7\6\u0082\n\6\f\6\16\6\u0085\13\6\3\6\3\6")
        buf.write("\3\6\5\6\u008a\n\6\3\6\7\6\u008d\n\6\f\6\16\6\u0090\13")
        buf.write("\6\3\6\3\6\5\6\u0094\n\6\7\6\u0096\n\6\f\6\16\6\u0099")
        buf.write("\13\6\3\6\3\6\3\7\7\7\u009e\n\7\f\7\16\7\u00a1\13\7\3")
        buf.write("\7\3\7\6\7\u00a5\n\7\r\7\16\7\u00a6\3\7\7\7\u00aa\n\7")
        buf.write("\f\7\16\7\u00ad\13\7\3\7\7\7\u00b0\n\7\f\7\16\7\u00b3")
        buf.write("\13\7\3\b\3\b\5\b\u00b7\n\b\3\b\2\2\t\2\4\6\b\n\f\16\2")
        buf.write("\b\4\2\3\3\24\24\3\2\3\4\3\2\4\5\4\2\5\5\7\7\6\2\3\4\7")
        buf.write("\7\t\r\24\24\7\2\3\4\7\7\t\r\22\22\24\24\u00d1\2\31\3")
        buf.write("\2\2\2\4[\3\2\2\2\6^\3\2\2\2\bf\3\2\2\2\n\u0083\3\2\2")
        buf.write("\2\f\u009f\3\2\2\2\16\u00b6\3\2\2\2\20\22\t\2\2\2\21\20")
        buf.write("\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\26\3\2\2\2\25\23\3\2\2\2\26\30\7\4\2\2\27\23\3\2\2\2")
        buf.write("\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\37\3\2\2")
        buf.write("\2\33\31\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2\2\36!\3\2\2")
        buf.write("\2\37\35\3\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\37\3\2\2\2\"")
        buf.write(",\5\6\4\2#%\t\3\2\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3")
        buf.write("\2\2\2\')\3\2\2\2(&\3\2\2\2)+\5\6\4\2*&\3\2\2\2+.\3\2")
        buf.write("\2\2,*\3\2\2\2,-\3\2\2\2-\62\3\2\2\2.,\3\2\2\2/\61\t\2")
        buf.write("\2\2\60/\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2")
        buf.write("\2\2\63\66\3\2\2\2\64\62\3\2\2\2\65\67\7\4\2\2\66\65\3")
        buf.write("\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29\\\3\2\2\2:>")
        buf.write("\5\b\5\2;=\t\4\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2")
        buf.write("\2\2?B\3\2\2\2@>\3\2\2\2A:\3\2\2\2BC\3\2\2\2CA\3\2\2\2")
        buf.write("CD\3\2\2\2D\\\3\2\2\2EG\t\2\2\2FE\3\2\2\2GJ\3\2\2\2HF")
        buf.write("\3\2\2\2HI\3\2\2\2IL\3\2\2\2JH\3\2\2\2KM\7\4\2\2LK\3\2")
        buf.write("\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\\\3\2\2\2PT\5\n\6")
        buf.write("\2QS\7\4\2\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U")
        buf.write("X\3\2\2\2VT\3\2\2\2WP\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3")
        buf.write("\2\2\2Z\\\3\2\2\2[\"\3\2\2\2[A\3\2\2\2[H\3\2\2\2[W\3\2")
        buf.write("\2\2\\\5\3\2\2\2]_\7\6\2\2^]\3\2\2\2^_\3\2\2\2_`\3\2\2")
        buf.write("\2`a\5\f\7\2ab\t\5\2\2b\7\3\2\2\2ce\t\2\2\2dc\3\2\2\2")
        buf.write("eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3\2\2\2ij\7")
        buf.write("\b\2\2js\7\25\2\2km\t\6\2\2lk\3\2\2\2mn\3\2\2\2nl\3\2")
        buf.write("\2\2no\3\2\2\2op\3\2\2\2pr\7\25\2\2ql\3\2\2\2ru\3\2\2")
        buf.write("\2sq\3\2\2\2st\3\2\2\2ty\3\2\2\2us\3\2\2\2vx\t\2\2\2w")
        buf.write("v\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{y\3")
        buf.write("\2\2\2|~\7\16\2\2}\177\7\17\2\2~}\3\2\2\2~\177\3\2\2\2")
        buf.write("\177\t\3\2\2\2\u0080\u0082\t\2\2\2\u0081\u0080\3\2\2\2")
        buf.write("\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3")
        buf.write("\2\2\2\u0084\u0086\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087")
        buf.write("\7\20\2\2\u0087\u0089\5\f\7\2\u0088\u008a\7\5\2\2\u0089")
        buf.write("\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0097\3\2\2\2")
        buf.write("\u008b\u008d\t\3\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3")
        buf.write("\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0093\5\f\7\2\u0092")
        buf.write("\u0094\7\5\2\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0096\3\2\2\2\u0095\u008e\3\2\2\2\u0096\u0099\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\7\21\2\2\u009b")
        buf.write("\13\3\2\2\2\u009c\u009e\t\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00ab\5")
        buf.write("\16\b\2\u00a3\u00a5\t\7\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\u00aa\5\16\b\2\u00a9\u00a4")
        buf.write("\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00b1\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ae\u00b0\t\2\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3")
        buf.write("\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\r")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7\7\25\2\2\u00b5")
        buf.write("\u00b7\5\b\5\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2")
        buf.write("\u00b7\17\3\2\2\2 \23\31\37&,\628>CHNTY[^fnsy~\u0083\u0089")
        buf.write("\u008e\u0093\u0097\u009f\u00a6\u00ab\u00b1\u00b6")
        return buf.getvalue()


class EdgarParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"' '", u"'\n'", u"'.'", u"'%'", u"':'", 
                     u"'('", u"','", u"'['", u"']'", u"'-'", u"'/'", u"')'", 
                     u"';'", u"'“'", u"'”'", u"'&'", u"<INVALID>", u"'\t'", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'A.M.'", u"'P.M.'", u"'P.O.'", u"'U.S.'", u"'U.S.A.'", 
                     u"<INVALID>", u"<INVALID>", u"'D.C.'", u"'I.R.S.'", 
                     u"'N.Y.'", u"'B.V.'", u"'N.E.'", u"'N.W.'", u"'S.E.'", 
                     u"'S.W.'", u"'J.A.'", u"'L.P.'", u"'U.S.C.'", u"'Non-U.S.'", 
                     u"'U.S.-based'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'No.'", u"'Engr.'", u"'Tech.'", u"'Dir.'", 
                     u"<INVALID>", u"'ST.'", u"'AVE.'", u"'LN.'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"WHITE", u"TAB", u"WORD", u"LITERAL", 
                      u"ULWORD", u"LATIN", u"TWORD", u"UNICODE", u"VALUE", 
                      u"EMAIL", u"URL", u"DOLLAR", u"ALLDASH", u"ALLUNSCO", 
                      u"BAR", u"BARX", u"NO", u"TOPLINE", u"A_M_", u"P_M_", 
                      u"P_O_", u"U_S_", u"U_S_A_", u"I_E_", u"E_G_", u"D_C_", 
                      u"I_R_S_", u"N_Y_", u"B_V_", u"N_E_", u"N_W_", u"S_E_", 
                      u"S_W_", u"J_A_", u"L_P_", u"U_S_C_", u"NonU_S_", 
                      u"U_S_based", u"MRR_", u"LTD_", u"CORP_", u"INC_", 
                      u"NO_", u"ENGR_", u"TECH_", u"DIR_", u"DR_", u"ST_", 
                      u"AVE_", u"LN_", u"NSWE", u"JAN_", u"FEB_", u"MAR_", 
                      u"APR_", u"MAY_", u"JUN_", u"JUL_", u"AUG_", u"SEP_", 
                      u"OCT_", u"NOV_", u"DEC_" ]

    RULE_r = 0
    RULE_paragraph = 1
    RULE_sentence = 2
    RULE_paren_sentence = 3
    RULE_quoted_paragraph = 4
    RULE_words = 5
    RULE_word = 6

    ruleNames =  [ "r", "paragraph", "sentence", "paren_sentence", "quoted_paragraph", 
                   "words", "word" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    WHITE=17
    TAB=18
    WORD=19
    LITERAL=20
    ULWORD=21
    LATIN=22
    TWORD=23
    UNICODE=24
    VALUE=25
    EMAIL=26
    URL=27
    DOLLAR=28
    ALLDASH=29
    ALLUNSCO=30
    BAR=31
    BARX=32
    NO=33
    TOPLINE=34
    A_M_=35
    P_M_=36
    P_O_=37
    U_S_=38
    U_S_A_=39
    I_E_=40
    E_G_=41
    D_C_=42
    I_R_S_=43
    N_Y_=44
    B_V_=45
    N_E_=46
    N_W_=47
    S_E_=48
    S_W_=49
    J_A_=50
    L_P_=51
    U_S_C_=52
    NonU_S_=53
    U_S_based=54
    MRR_=55
    LTD_=56
    CORP_=57
    INC_=58
    NO_=59
    ENGR_=60
    TECH_=61
    DIR_=62
    DR_=63
    ST_=64
    AVE_=65
    LN_=66
    NSWE=67
    JAN_=68
    FEB_=69
    MAR_=70
    APR_=71
    MAY_=72
    JUN_=73
    JUL_=74
    AUG_=75
    SEP_=76
    OCT_=77
    NOV_=78
    DEC_=79

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paragraph(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EdgarParser.ParagraphContext)
            else:
                return self.getTypedRuleContext(EdgarParser.ParagraphContext,i)


        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(EdgarParser.TAB)
            else:
                return self.getToken(EdgarParser.TAB, i)

        def getRuleIndex(self):
            return EdgarParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.exitR(self)




    def r(self):

        localctx = EdgarParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 17
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==EdgarParser.T__0 or _la==EdgarParser.TAB:
                        self.state = 14
                        _la = self._input.LA(1)
                        if not(_la==EdgarParser.T__0 or _la==EdgarParser.TAB):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 19
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 20
                    self.match(EdgarParser.T__1) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EdgarParser.T__0) | (1 << EdgarParser.T__1) | (1 << EdgarParser.T__3) | (1 << EdgarParser.T__5) | (1 << EdgarParser.T__13) | (1 << EdgarParser.TAB) | (1 << EdgarParser.WORD))) != 0):
                self.state = 26
                self.paragraph()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParagraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EdgarParser.SentenceContext)
            else:
                return self.getTypedRuleContext(EdgarParser.SentenceContext,i)


        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(EdgarParser.TAB)
            else:
                return self.getToken(EdgarParser.TAB, i)

        def paren_sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EdgarParser.Paren_sentenceContext)
            else:
                return self.getTypedRuleContext(EdgarParser.Paren_sentenceContext,i)


        def quoted_paragraph(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EdgarParser.Quoted_paragraphContext)
            else:
                return self.getTypedRuleContext(EdgarParser.Quoted_paragraphContext,i)


        def getRuleIndex(self):
            return EdgarParser.RULE_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.enterParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.exitParagraph(self)




    def paragraph(self):

        localctx = EdgarParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_paragraph)
        self._la = 0 # Token type
        try:
            self.state = 89
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.sentence()
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 36
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 33
                                _la = self._input.LA(1)
                                if not(_la==EdgarParser.T__0 or _la==EdgarParser.T__1):
                                    self._errHandler.recoverInline(self)
                                else:
                                    self.consume() 
                            self.state = 38
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                        self.state = 39
                        self.sentence() 
                    self.state = 44
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==EdgarParser.T__0 or _la==EdgarParser.TAB:
                    self.state = 45
                    _la = self._input.LA(1)
                    if not(_la==EdgarParser.T__0 or _la==EdgarParser.TAB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 52 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 51
                        self.match(EdgarParser.T__1)

                    else:
                        raise NoViableAltException(self)
                    self.state = 54 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 56
                        self.paren_sentence()
                        self.state = 60
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 57
                                _la = self._input.LA(1)
                                if not(_la==EdgarParser.T__1 or _la==EdgarParser.T__2):
                                    self._errHandler.recoverInline(self)
                                else:
                                    self.consume() 
                            self.state = 62
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)


                    else:
                        raise NoViableAltException(self)
                    self.state = 65 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==EdgarParser.T__0 or _la==EdgarParser.TAB:
                    self.state = 67
                    _la = self._input.LA(1)
                    if not(_la==EdgarParser.T__0 or _la==EdgarParser.TAB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 74 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 73
                        self.match(EdgarParser.T__1)

                    else:
                        raise NoViableAltException(self)
                    self.state = 76 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 78
                        self.quoted_paragraph()
                        self.state = 82
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 79
                                self.match(EdgarParser.T__1) 
                            self.state = 84
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)


                    else:
                        raise NoViableAltException(self)
                    self.state = 87 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def words(self):
            return self.getTypedRuleContext(EdgarParser.WordsContext,0)


        def getRuleIndex(self):
            return EdgarParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = EdgarParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if _la==EdgarParser.T__3:
                self.state = 91
                self.match(EdgarParser.T__3)


            self.state = 94
            self.words()
            self.state = 95
            _la = self._input.LA(1)
            if not(_la==EdgarParser.T__2 or _la==EdgarParser.T__4):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Paren_sentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(EdgarParser.WORD)
            else:
                return self.getToken(EdgarParser.WORD, i)

        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(EdgarParser.TAB)
            else:
                return self.getToken(EdgarParser.TAB, i)

        def getRuleIndex(self):
            return EdgarParser.RULE_paren_sentence

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.enterParen_sentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.exitParen_sentence(self)




    def paren_sentence(self):

        localctx = EdgarParser.Paren_sentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paren_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EdgarParser.T__0 or _la==EdgarParser.TAB:
                self.state = 97
                _la = self._input.LA(1)
                if not(_la==EdgarParser.T__0 or _la==EdgarParser.TAB):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(EdgarParser.T__5)
            self.state = 104
            self.match(EdgarParser.WORD)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 106 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 105
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EdgarParser.T__0) | (1 << EdgarParser.T__1) | (1 << EdgarParser.T__4) | (1 << EdgarParser.T__6) | (1 << EdgarParser.T__7) | (1 << EdgarParser.T__8) | (1 << EdgarParser.T__9) | (1 << EdgarParser.T__10) | (1 << EdgarParser.TAB))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 108 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EdgarParser.T__0) | (1 << EdgarParser.T__1) | (1 << EdgarParser.T__4) | (1 << EdgarParser.T__6) | (1 << EdgarParser.T__7) | (1 << EdgarParser.T__8) | (1 << EdgarParser.T__9) | (1 << EdgarParser.T__10) | (1 << EdgarParser.TAB))) != 0)):
                            break

                    self.state = 110
                    self.match(EdgarParser.WORD) 
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EdgarParser.T__0 or _la==EdgarParser.TAB:
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==EdgarParser.T__0 or _la==EdgarParser.TAB):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(EdgarParser.T__11)
            self.state = 124
            _la = self._input.LA(1)
            if _la==EdgarParser.T__12:
                self.state = 123
                self.match(EdgarParser.T__12)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Quoted_paragraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def words(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EdgarParser.WordsContext)
            else:
                return self.getTypedRuleContext(EdgarParser.WordsContext,i)


        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(EdgarParser.TAB)
            else:
                return self.getToken(EdgarParser.TAB, i)

        def getRuleIndex(self):
            return EdgarParser.RULE_quoted_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.enterQuoted_paragraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.exitQuoted_paragraph(self)




    def quoted_paragraph(self):

        localctx = EdgarParser.Quoted_paragraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_quoted_paragraph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EdgarParser.T__0 or _la==EdgarParser.TAB:
                self.state = 126
                _la = self._input.LA(1)
                if not(_la==EdgarParser.T__0 or _la==EdgarParser.TAB):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(EdgarParser.T__13)
            self.state = 133
            self.words()
            self.state = 135
            _la = self._input.LA(1)
            if _la==EdgarParser.T__2:
                self.state = 134
                self.match(EdgarParser.T__2)


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EdgarParser.T__0) | (1 << EdgarParser.T__1) | (1 << EdgarParser.T__5) | (1 << EdgarParser.TAB) | (1 << EdgarParser.WORD))) != 0):
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 137
                        _la = self._input.LA(1)
                        if not(_la==EdgarParser.T__0 or _la==EdgarParser.T__1):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume() 
                    self.state = 142
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                self.state = 143
                self.words()
                self.state = 145
                _la = self._input.LA(1)
                if _la==EdgarParser.T__2:
                    self.state = 144
                    self.match(EdgarParser.T__2)


                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(EdgarParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WordsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EdgarParser.WordContext)
            else:
                return self.getTypedRuleContext(EdgarParser.WordContext,i)


        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(EdgarParser.TAB)
            else:
                return self.getToken(EdgarParser.TAB, i)

        def getRuleIndex(self):
            return EdgarParser.RULE_words

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.enterWords(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.exitWords(self)




    def words(self):

        localctx = EdgarParser.WordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_words)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 154
                    _la = self._input.LA(1)
                    if not(_la==EdgarParser.T__0 or _la==EdgarParser.TAB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 160
            self.word()
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 162 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 161
                            _la = self._input.LA(1)
                            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EdgarParser.T__0) | (1 << EdgarParser.T__1) | (1 << EdgarParser.T__4) | (1 << EdgarParser.T__6) | (1 << EdgarParser.T__7) | (1 << EdgarParser.T__8) | (1 << EdgarParser.T__9) | (1 << EdgarParser.T__10) | (1 << EdgarParser.T__15) | (1 << EdgarParser.TAB))) != 0)):
                                self._errHandler.recoverInline(self)
                            else:
                                self.consume()

                        else:
                            raise NoViableAltException(self)
                        self.state = 164 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                    self.state = 166
                    self.word() 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    _la = self._input.LA(1)
                    if not(_la==EdgarParser.T__0 or _la==EdgarParser.TAB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume() 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(EdgarParser.WORD, 0)

        def paren_sentence(self):
            return self.getTypedRuleContext(EdgarParser.Paren_sentenceContext,0)


        def getRuleIndex(self):
            return EdgarParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, EdgarListener ):
                listener.exitWord(self)




    def word(self):

        localctx = EdgarParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_word)
        try:
            self.state = 180
            token = self._input.LA(1)
            if token in [EdgarParser.WORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(EdgarParser.WORD)

            elif token in [EdgarParser.T__0, EdgarParser.T__5, EdgarParser.TAB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.paren_sentence()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




