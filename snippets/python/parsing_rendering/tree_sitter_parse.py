import tree_sitter_typescript as ts
from tree_sitter import Language, Parser

TS_LANGUAGE = Language(ts.language_tsx())

parser = Parser(TS_LANGUAGE)
tree = parser.parse(bytes(..., "utf8"))
