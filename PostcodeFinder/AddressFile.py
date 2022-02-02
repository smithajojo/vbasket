class Address:
    _flatno = 0
    _address = ""
    _street = ""
    _zipcode = ""
    _country = ""

    def __init__(self,flatno,address,street,zipcode,country):
        self._flatno = flatno
        self._address = address
        self._street = street
        self._zipcode = zipcode
        self._country = country


