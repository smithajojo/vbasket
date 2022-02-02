import AddressFinder
import AddressFile

adf = AddressFinder.AddressFinder()
adf.AddAddress(AddressFile.Address(71,"Northum","Cedar","SM25Fr","UK"))
adf.AddAddress(AddressFile.Address(72,"Northum","Cedar","SM25Fr","UK"))
adf.AddAddress(AddressFile.Address(73,"Northum","Cedar","SM25Fr","UK"))
adf.AddAddress(AddressFile.Address(74,"Northum","Wellesley","SM25Fr","UK"))
adf.AddAddress(AddressFile.Address(72,"Northum","Cedar","SM15Fr","UK"))

addresslist = adf.GetAllAddress()
for ad in addresslist:
    print(ad._flatno,ad._address,ad._street,ad._zipcode)

print("Search for flatno 72")
result = adf.SearchAddress(71)

for res in result:
    print(res._flatno, res._zipcode)

if len(result) == 0:
    print("No results")
else:
    print(str(len(result))+" results found")

result = adf.SearchByZip("SM25FR")

for res in result:
    print(res._flatno, res._zipcode)

result = adf.SearchByStreet("wellesley")

for res in result:
    print(res._flatno,res._street, res._zipcode)

x = adf.SearchBy("FlatNo",71)
y = adf.SearchBy("Street","Cedar")
