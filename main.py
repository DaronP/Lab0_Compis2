
import sys
from antlr4 import *
from dist.typescriptLexer import typescriptLexer
from dist.typescriptParser import typescriptParser
from dist.typescriptVisitor import typescriptVisitor
from dist.typescriptListener import typescriptListener
from antlr4.tree.Trees import Trees

class TSfPrintListener(typescriptListener):
    pass


if __name__ == "__main__":
    f = input()
    data =  open(f, 'r+')
    text = data.read()
    data.close()
    txt =  InputStream(text)

    # lexer
    lexer = typescriptLexer(data)
    stream = CommonTokenStream(lexer)

    # parser
    parser = typescriptParser(stream)
    tree = parser.sAll()

    '''# evaluator
    visitor = typescriptVisitor()
    output = visitor.visitSAll(tree)
    print(output)'''

    printer = TSfPrintListener()

    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    print(Trees.toStringTree(tree, None, parser))