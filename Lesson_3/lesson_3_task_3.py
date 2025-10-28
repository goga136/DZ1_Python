from address import Address
from mailing import Mailing

to_address = Address(123456, "Moscow", "Lenina", 1, 11)
from_address = Address(234567, "Tula", "Lenina", 2, 22)
cost = 1000
trask = 123456

my_mailing = Mailing(to_address, from_address, 1000, "123456")
print(my_mailing)
