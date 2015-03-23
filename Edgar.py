#
import sys
import codecs
from antlr4 import *
from EdgarLexer import EdgarLexer
from EdgarParser import EdgarParser
from EdgarListener import EdgarListener


class RPrinter(EdgarListener) :     

    def exitSentence(self, ctx) :
        print('Sentence#',ctx.getText(),'#')

    # Exit a parse tree produced by EdgarParser#paren_sentence.
    def exitParen_sentence(self, ctx):
        print('paren_sentence (', ctx.getText(), ')')

    # Exit a parse tree produced by EdgarParser#paragraph.
    def exitParagraph(self, ctx):
        print('Paragraph [', ctx.getText(), ']')
        pass

    # Exit a parse tree produced by EdgarParser#quoted_paragraph.
    #def exitQuoted_paragraph(self, ctx):
    #    pass

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
    print(tree.toStringTree())


if __name__ == '__main__':
    main(sys.argv)
