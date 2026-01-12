from interpreter.compiler import ByteCode, ByteCodeType, Compiler
from interpreter.parser import BinOp, Int

def test_compile_addition():
    tree = BinOp(
        "+",
        Int(3),
        Int(5),
    )
    bytecode = list(Compiler(tree).compile())
    assert bytecode == [
        ByteCode(ByteCodeType.PUSH, 3),
        ByteCode(ByteCodeType.PUSH, 5),
        ByteCode(ByteCodeType.BINOP, "+"),
    ]

def test_compile_subtraction():
    tree = BinOp(
        "-",
        Int(5),
        Int(2),
    )
    bytecode = list(Compiler(tree).compile())
    assert bytecode == [
        ByteCode(ByteCodeType.PUSH, 5),
        ByteCode(ByteCodeType.PUSH, 2),
        ByteCode(ByteCodeType.BINOP, "-"),
    ]