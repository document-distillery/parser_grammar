#
import sys
import codecs, re
from antlr4 import *
from EdgarLexer import EdgarLexer
from EdgarParser import EdgarParser
from EdgarListener import EdgarListener


class RPrinter(EdgarListener) :     

    def exitSentence(self, ctx) :
        o1 = ctx.getText()
        o2 = re.sub('\$[ \t\n]*\([0-9,]+(\.[0-9]+)?\)', '$\1', o1)
        print('SENTENCE #', o2, '#')

    # Exit a parse tree produced by EdgarParser#paren_sentence.
    def exitParen_paragraph(self, ctx):
        o1 = ctx.getText()
        o2 = o1.replace('\n', ' ')
        #o2 = re.sub('\$[ \t\n]+\([0-9,]+(\.[0-9]+)?\)', '$\1', o1)
        print('PAREN_PARAGRAPH (', o2, ')')

    # Exit a parse tree produced by EdgarParser#paragraph.
    def exitText_element(self, ctx):
        o1 = ctx.getText()
        #o2 = re.sub('\$[ \t\n]*\([0-9,]+(\.[0-9]+)?\)', '$\1', o1)
        o2 = o1.replace('\n', ' ')
        print('TEXT-ELEMENT [', o2, ']')

    # Exit a parse tree produced by EdgarParser#paragraph.
    def exitSection_title(self, ctx):
        o1 = ctx.getText()
        #o2 = re.sub('\$[ \t\n]*\([0-9,]+(\.[0-9]+)?\)', '$\1', o1)
        o2 = o1.replace('\n', ' ')
        print('SECTION-TITLE [', o2, ']')

    # Exit a parse tree produced by EdgarParser#quoted_paragraph.
    def exitWord(self, ctx):
        #o1 = ctx.getText()
        #o2 = re.sub('[ \t\n]', '', o1)
        #print(o2)
        pass

"""
"""
def main(argv):
    input = FileStream(argv[1], 'utf-8')

    lexer = EdgarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = EdgarParser(stream)
    tree = parser.r()
    #
    printer = RPrinter()  # add
    walker = ParseTreeWalker()  # add
    walker.walk(printer, tree)  # add
    # print(tree.toStringTree())


if __name__ == '__main__':
    main(sys.argv)
