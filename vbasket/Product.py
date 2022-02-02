class Product:
    pcode = ""
    pname = ""
    pprice = 0

    def __init__(self, code,name,price):
        self.pcode = code
        self.pname = name
        self.pprice = price