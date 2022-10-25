# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
cas = [{'bin': bin(i),'dec':int(i),'hex': hex(i),'oct': oct(i)} for i in range(16)]
pprint(cas)