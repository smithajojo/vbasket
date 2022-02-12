class UserInfo:
    def __init__(self,username,email,phone,id):
        self.username = username
        self.email = email
        self.phone = phone
        self.id = id

    def __str__(self):
        return "{0} ,{1} ,{2} {3}".format(self.id ,self.username,self.email,self.phone)

class AddressInfo:
    def __init__(self,address1,address2,postcode,county):
        self.address1 = address1
        self.address2 = address2
        self.postcode = postcode
        self.county = county

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.address1,self.address2,self.postcode,self.county)

class ProductInfo:
    def __init__(self,pcode,pname,pprice):
        self.pcode = pcode
        self.pname = pname
        self.pprice = pprice

    def __str__(self):
        return "{0}, {1}, {2}".format(self.pcode, self.pname, self.pprice)

