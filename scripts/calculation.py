class Calculation:

    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        return "相加只能整数型和浮点数形哦"

    def subtract(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a - b
        return "相减只能整数型和浮点数形哦"

    def multiply(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        return "相乘只能整数型和浮点数形哦"

    def divide(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a / b
        return "相除只能整数型和浮点数形哦"
