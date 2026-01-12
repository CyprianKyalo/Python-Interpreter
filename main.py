import sys
from src.interpreter.compiler import Compiler
from src.interpreter.interpreter import Interpreter
from src.interpreter.parser import Parser
from src.interpreter.token_types import TokenType
from src.interpreter.tokenizer import Tokenizer

if __name__ == "__main__":
    # code = "3 + 5 - 2"
    # tokenizer = Tokenizer(code)
    # print(code)

    # # while (tok := tokenizer.next_token()).type != TokenType.EOF:
    # #     print(f"\t{tok.type}, {tok.value}")
    # for tok in tokenizer:
    #     print(f"\t{tok.type}, {tok.value}")

    # code = "3 + 5"
    # parser = Parser(list(Tokenizer(code)))
    # print(parser.parse())

    # compiler = Compiler(Parser(list(Tokenizer(code))).parse())
    # for bc in compiler.compile():
    #     print(bc)

    code = sys.argv[1]
    tokens = list(Tokenizer(code))
    tree = Parser(tokens).parse()
    bytecode = list(Compiler(tree).compile())
    Interpreter(bytecode).interpret()