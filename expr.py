
# GENERATED FILE - DO NOT MANUALLY EDIT!
# Generated by generate_ast.py

from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_AssignExpr(self):
        pass
    @abstractmethod
    def visit_BinaryExpr(self):
        pass
    @abstractmethod
    def visit_CallExpr(self):
        pass
    @abstractmethod
    def visit_GroupingExpr(self):
        pass
    @abstractmethod
    def visit_LiteralExpr(self):
        pass
    @abstractmethod
    def visit_LogicalExpr(self):
        pass
    @abstractmethod
    def visit_UnaryExpr(self):
        pass
    @abstractmethod
    def visit_VariableExpr(self):
        pass

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor):
        '''Call a method on the visitor based on your class name'''
        pass

class Assign(Expr):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        return visitor.visit_AssignExpr(self)


class Binary(Expr):

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_BinaryExpr(self)


class Call(Expr):

    def __init__(self, callee, paren, arguments):
        self.callee = callee
        self.paren = paren
        self.arguments = arguments

    def accept(self, visitor):
        return visitor.visit_CallExpr(self)


class Grouping(Expr):

    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_GroupingExpr(self)


class Literal(Expr):

    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_LiteralExpr(self)


class Logical(Expr):

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_LogicalExpr(self)


class Unary(Expr):

    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_UnaryExpr(self)


class Variable(Expr):

    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.visit_VariableExpr(self)


