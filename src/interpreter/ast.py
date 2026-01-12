from dataclasses import dataclass

@dataclass
class TreeNode:
    pass

@dataclass
class BinOp(TreeNode):
    op: str
    left: "Int"
    right: "Int"

@dataclass
class Int(TreeNode):
    value: int