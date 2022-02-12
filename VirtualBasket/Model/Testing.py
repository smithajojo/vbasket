import json
from VirtualBasket.Model.DomainEntities import UserInfo,AddressInfo,ProductInfo

x = UserInfo("abc@123.com","abc@123.com","99999999",2)
print(x)

js = ''' {
        "username":"sm@123.com",
        "email":"sm@123.com",
        "phone":"8977663456",
        "id":1
    } '''


userfromjson = json.loads(js)
y = UserInfo(**userfromjson)

print(y)

address = AddressInfo("Sankeerthanam","Pazhaveedu","688009","Alappuzha")
print(address)

a_js = '''{
             "address1":"BGP",
             "address2":"Pazhaveedu",
             "postcode":"688007",
             "county":"Alappuzha"
            }'''
print(AddressInfo(**json.loads(a_js)))



print(ProductInfo("C265","Computer",280))

p_js = '''{
        "pcode" : "L110",
        "pname" : "Laptop",
        "pprice" : 500
        }'''

print(ProductInfo(**json.loads(p_js)))