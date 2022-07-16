'''
Jorge Andres Perez - 16362
Andres Quan - 17652
'''



import antlr4
import sys
from antlr4 import *
from dist.typescriptLexer import typescriptLexer
from dist.typescriptParser import typescriptParser
from dist.typescriptVisitor import typescriptVisitor
from dist.typescriptListener import typescriptListener
from antlr4.tree.Trees import Trees

from dist.yaplLexer import yaplLexer
from dist.yaplParser import yaplParser
from dist.yaplVisitor import yaplVisitor
from dist.yaplListener import yaplListener

#antlr4 -Dlanguage=Python3 .\typescript.g4 -visitor -o dist

class YAPLfPrintListener(yaplListener):
    pass

class TSfPrintListener(typescriptListener):
    pass


if __name__ == "__main__":
    language = input('Especifique el lenguaje: 1 - TypeScript, 2 - YAPL \n')
    if language == 1 or language == '1':
        data =  open('test_ts.txt', 'r+')
        text = data.read()
        data.close()
        inputStream =  antlr4.InputStream(text)

        # lexer
        lexer = typescriptLexer(inputStream)
        stream = CommonTokenStream(lexer)

        # parser
        parser = typescriptParser(stream)
        tree = parser.sAll()
        
        # evaluator
        visitor = typescriptVisitor()
        output = visitor.visitSAll(tree)
        print(output)

        printer = TSfPrintListener()

        walker = ParseTreeWalker()
        walker.walk(printer, tree)

        print(Trees.toStringTree(tree, None, parser))

    else:
        data =  open('test_yapl.txt', 'r+')
        text = data.read()
        data.close()
        inputStream =  antlr4.InputStream(text)

        # lexer
        lexer = yaplLexer(inputStream)
        stream = CommonTokenStream(lexer)

        # parser
        parser = yaplParser(stream)
        tree = parser.program()

        # evaluator
        visitor = yaplVisitor()
        output = visitor.visitProgram(tree)
        print(output)

        printer = TSfPrintListener()

        walker = ParseTreeWalker()
        walker.walk(printer, tree)

        print(Trees.toStringTree(tree, None, parser))
