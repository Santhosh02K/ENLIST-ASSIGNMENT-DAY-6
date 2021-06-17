a={"a":"apple","b":"ball","c":"cat"}

print(a['a'])
print(a['b'])

print(a.values())

a['d']='dog'
a

a['a']="ant"
a

del a['a']
a

csk={"dhoni","bravo","jadeja"}

csk.add("raina")
csk


csk.remove("raina")
csk

csk.discard('bravo')
csk

dict1={'a':'apple','b':'ball','c':'cat'}
dict2={'d':'dog','e':'egg','f':'fish'}

dict3=dict1.update(dict2)
print(dict1)
dict1

del dict1['a']
dict1

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[1,2,3]
d=[100,200,300]

l1=dict(zip(a,b))
l2=dict(zip(c,d))

print(l1)
print(l2)

set1={'apple','orange','grapes'}
print(len(set1))

set1={'apple','orange','grapes'}
set2={'apple','orange','mango'}
result= set2-set1

