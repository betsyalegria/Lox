import os

template = """
# GENERATED FILE - DO NOT MANUALLY EDIT!
# Generated by generate_ast.py

from abc import ABC, abstractmethod


class Visitor(ABC):
{visitor_methods}

class {base_class_name}(ABC):
    @abstractmethod
    def accept(self, visitor):
        '''Call a method on the visitor based on your class name'''
        pass

{classes_code}
"""

def define_class(writer, base_class_name, class_name, fields):
    newline = '\n'
    return f"""class {class_name}({base_class_name}):

    def __init__(self, {', '.join(fields)}):
{''.join(f'        self.{field} = {field}{newline}' for field in fields)}
    def accept(self, visitor):
        return visitor.visit_{class_name}{base_class_name}(self)

"""

def define_ast(output_dir, filename, base_class_name, type_specs):
    path = os.path.join(output_dir, filename)
    class_strings = []
    visitor_method_strings = []
    for type_spec in type_specs:
        class_name = type_spec.split(':')[0].strip()
        fields = type_spec.split(':')[1].strip().split(', ')
        class_strings.append(define_class(class_name, base_class_name, class_name, fields))
        visitor_method_strings.append(
                f"    @abstractmethod\n"
                f"    def visit_{class_name}{base_class_name}(self):\n"
                f"        pass")
    with open(path, 'w') as f:
        f.write(template.format(
            base_class_name=base_class_name,
            classes_code='\n'.join(class_strings),
            visitor_methods='\n'.join(visitor_method_strings)
        ))


if __name__ == '__main__':
    define_ast('..', 'expr.py', "Expr", [
        "Assign   : name, value",
        "Binary   : left, operator, right",
        "Call     : callee, paren, arguments",
        "Grouping : expression",
        "Literal  : value",
        "Logical  : left, operator, right",
        "Unary    : operator, right",
        "Variable : name"
    ])

    define_ast('..', 'stmt.py', "Stmt", [
        "Block      : statements",
        "Expression : expression",
        "Function   : name, params, body",
        "If         : condition, then_branch, else_branch",
        "Print      : expression",
        "Var        : name, initializer",
        "While      : condition, body",
    ])
