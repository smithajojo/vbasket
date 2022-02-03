import AddressFile

class AddressFinder:
    addresslist = []

    def AddAddress(self,address:AddressFile.Address):

        if not any((ad._flatno == address._flatno and ad._zipcode == address._zipcode) for ad in self.addresslist):
                self.addresslist.append(address)

    def GetAllAddress(self):
        return self.addresslist

    def SearchAddress(self,FlatNo):
        result = []
        for ad in self.addresslist:
            if(ad._flatno == FlatNo):
                result.append((ad))
        return result

    def SearchByZip(self,Zipcode):
        result = []
        for ad in self.addresslist:
            if((ad._zipcode).upper() == Zipcode.upper()):
                result.append((ad))
        return result

    def SearchByStreet(self,Street):
        result = []
        for ad in self.addresslist:
            if((ad._street).upper() == Street.upper()):
                result.append((ad))
        return result

    def SearchBy(self,inputproperty,inputpropertyvalue):
        print("Search " + inputproperty + "=" +str(inputpropertyvalue))

        result = []
        for ad in self.addresslist:
            if inputproperty == "FlatNo":
                if (ad._flatno == inputpropertyvalue):
                    result.append(ad)

            if inputproperty == "Street":
                if ((ad._street).upper() == inputpropertyvalue.upper()):
                    result.append(ad)

            if inputproperty == "Zipcode":
                if ((ad._zipcode).upper() == inputpropertyvalue.upper()):
                    result.append(ad)

        return result



