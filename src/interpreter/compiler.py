from .ast import BinOp

from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Generator

class ByteCodeType(StrEnum):
    BINOP = auto()
    PUSH = auto()

@dataclass
class ByteCode:
    type: ByteCodeType
    value: Any = None

class Compiler:
    def __init__(self, tree: BinOp) -> None:
        self.tree = tree

    def compile(self) -> Generator[ByteCode, None, None]:
        left = self.tree.left
        yield ByteCode(ByteCodeType.PUSH, left.value)

        right = self.tree.right
        yield ByteCode(ByteCodeType.PUSH, right.value)

        yield ByteCode(ByteCodeType.BINOP, self.tree.op)