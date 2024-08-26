from person import Person,Manager
bob=Person('Bod Smith')
sue=Person('Sue JAne',job='teacher',pay=10000)
john=Manager('John Paul',3000)

import shelve
db=shelve.open('persondb')
for obj in (bob,sue,john):
    db[obj.name]=obj
db.close()