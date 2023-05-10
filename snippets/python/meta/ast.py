import ast
import operator as op
from ast import BinOp, Num, UnaryOp

MAP = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
}


def evaluate(node):
    match node:
        case Num():
            return node.n
        case BinOp():
            left, right = evaluate(node.left), evaluate(node.right)
            return MAP[type(node.op)](left, right)
        case UnaryOp():
            operand = evaluate(node.operand)
            return MAP[type(node.op)](operand)


root = ast.parse("1 + 1", mode="eval")
evaluate(root.body)
