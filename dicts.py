a={
    'city':"Москва", 'temperature':'20'
}
print(a['city'])
a['temperature']=int(a['temperature'])-5
print(a)

print(a.get('country', 'Россия'))
a['date']='27.05.2019'
print(a)
print(len(a))