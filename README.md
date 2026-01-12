# Simple Arithmetic Interpreter

A minimalist interpreter implementation that processes and evaluates basic arithmetic expressions (addition and subtraction). This project demonstrates the fundamental components of language interpretation through a clean, educational implementation.

## Overview

This interpreter processes mathematical expressions like `3 + 5` or `10 - 3` through a classic four-stage pipeline:

1. **Tokenization** - Converts raw text into tokens
2. **Parsing** - Builds an Abstract Syntax Tree (AST)
3. **Compilation** - Generates bytecode instructions
4. **Interpretation** - Executes bytecode using a stack-based virtual machine

## Features

- Single-digit integer support (0-9)
- Binary operations: addition (`+`) and subtraction (`-`)
- Stack-based bytecode execution
- Clean separation of concerns across interpretation stages

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd Interpreter

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Usage

Run the interpreter by providing an arithmetic expression as a command-line argument:

```bash
python main.py "3 + 5"
# Output:
# Done!
# Final stack state: Stack([8])

python main.py "9 - 4"
# Output:
# Done!
# Final stack state: Stack([5])
```

## Architecture

### Components

#### 1. Tokenizer ([tokenizer.py](src/interpreter/tokenizer.py))
Converts source code into a stream of tokens. Recognizes:
- `INT` - Single-digit integers
- `PLUS` - Addition operator (+)
- `MINUS` - Subtraction operator (-)
- `EOF` - End of input

#### 2. Parser ([parser.py](src/interpreter/parser.py))
Transforms tokens into an Abstract Syntax Tree (AST). Currently supports binary operations with two operands.

AST Nodes ([ast.py](src/interpreter/ast.py)):
- `Int` - Integer literal node
- `BinOp` - Binary operation node (holds operator and left/right operands)

#### 3. Compiler ([compiler.py](src/interpreter/compiler.py))
Generates bytecode instructions from the AST. Produces:
- `PUSH` - Push value onto stack
- `BINOP` - Execute binary operation

#### 4. Interpreter ([interpreter.py](src/interpreter/interpreter.py))
Stack-based virtual machine that executes bytecode instructions:
- Maintains an execution stack
- Processes PUSH and BINOP instructions
- Computes final result

#### 5. Stack ([stack.py](src/interpreter/stack.py))
Simple stack implementation supporting push, pop, and peek operations.

## Example Execution Flow

For the expression `3 + 5`:

1. **Tokenization**: `"3 + 5"` → `[INT(3), PLUS, INT(5), EOF]`
2. **Parsing**: Tokens → `BinOp("+", Int(3), Int(5))`
3. **Compilation**: AST → `[PUSH(3), PUSH(5), BINOP("+")]`
4. **Interpretation**: 
   - Execute `PUSH(3)` → Stack: `[3]`
   - Execute `PUSH(5)` → Stack: `[3, 5]`
   - Execute `BINOP("+")` → Pop 5, pop 3, push 8 → Stack: `[8]`

## Project Structure

```
.
├── main.py                    # Entry point
├── requirements.txt           # Python dependencies
├── pyproject.toml            # Package configuration
├── src/
│   └── interpreter/
│       ├── __init__.py
│       ├── tokenizer.py      # Lexical analysis
│       ├── token_types.py    # Token definitions
│       ├── parser.py         # Syntax analysis
│       ├── ast.py            # AST node definitions
│       ├── compiler.py       # Bytecode generation
│       ├── interpreter.py    # Bytecode execution
│       └── stack.py          # Stack data structure
└── tests/
    ├── test_tokenizer.py
    ├── test_parser.py
    ├── test_compiler.py
    └── test_interpreter.py
```

## Running Tests

```bash
pytest tests/
```
