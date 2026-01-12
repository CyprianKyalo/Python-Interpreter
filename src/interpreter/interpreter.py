from .compiler import ByteCode, ByteCodeType
from .stack import Stack

class Interpreter:
    def __init__(self, bytecode: list[ByteCode]) -> None:
        self.stack = Stack()
        self.bytecode = bytecode
        self.ptr: int = 0

    def interpret(self) -> None:
        for bc in self.bytecode:
            if bc.type == ByteCodeType.PUSH:
                self.stack.push(bc.value)
            elif bc.type == ByteCodeType.BINOP:
                right = self.stack.pop()
                left = self.stack.pop()

                if bc.value == "+":
                    result = left + right
                elif bc.value == "-":
                    result = left - right
                else:
                    raise RuntimeError(f"Unknown operator {bc.value}.")

                self.stack.push(result)

        print("Done!")
        print(f"Final stack state: {self.stack}")