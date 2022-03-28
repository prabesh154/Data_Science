# Json means Java script Object Notation
# Json is data exchange format
book= { }
book['Prayash']= {
    'name':'tom',
    'address':'ktm',
    'phone':98349,
}

book['Prabesh']= {
    'name':'ram',
    'address':'pkr',
    'phone':24542,
}
# import json
# s=json.dumps(book)
# print(s)

# Output
# {"Prayash": {"name": "tom", "address": "ktm", "phone": 98349}, "Prabesh": {"name": "ram", "address": "pkr", "phone": 24542}}

import json
s=json.dumps(book)
with open("c://Users//Acer//PycharmProjects//book.txt","w") as f:
    f.write(s)
# write in a file as json
 # {"Prayash": {"name": "tom", "address": "ktm", "phone": 98349},
 #  "Prabesh": {"name": "ram", "address": "pkr", "phone": 24542}} in book.txt

 # read as a json
 #f=open("c://Users//Acer//PycharmProjects//book.txt" ,"r")
# s=f.read()
# s
# its a string
# '{"Prayash": {"name": "tom", "address": "ktm", "phone": 98349}, "Prabesh": {"name": "ram", "address": "pkr", "phone": 24542}}'

# import json
# book=json.loads(s)
# book
# {'Prayash': {'name': 'tom', 'address': 'ktm', 'phone': 98349}, 'Prabesh': {'name': 'ram', 'address': 'pkr', 'phone': 24542}}
# type(book)
# <class 'dict'>

# book['Prayash']
# {'name': 'tom', 'address': 'ktm', 'phone': 98349}
# book['Prayash']['phone']
# 98349
# for person in book:
#     print(book[person])
#
# {'name': 'tom', 'address': 'ktm', 'phone': 98349}
# {'name': 'ram', 'address': 'pkr', 'phone': 24542}
