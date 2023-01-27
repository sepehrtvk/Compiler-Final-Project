class Validation:
    def __init__(self):
        pass

    def check_operands_type(self, p):
        if (type(p[1]) == int or type(p[1]) == float) and (type(p[3]) == int or type(p[3]) == float):
            return False
        return True

    def check_operands_boolean(self, p):
        if type(p[1]) == type(p[3]) == bool:
            return True
        return False
