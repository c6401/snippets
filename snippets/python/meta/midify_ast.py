import ast
from pathlib import Path

code = Path("____").read_text()

tree = ast.parse(code)
print(ast.dump(tree, indent=4))


def walk_ast(node, path=()):
    match node:
        case ast.AST():
            return type(node)(
                **{
                    k: walk_ast(v, path + (type(node), k))
                    for k, v in ast.iter_fields(node)
                }
            )
        case list():
            return [walk_ast(x, path + (list,)) for x in node]
    return node


new = walk_ast(tree)
print(ast.unparse(new))
