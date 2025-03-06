def get_summ(one, two, delimiter='&'):
    a=f'{one}{delimiter}{two}'
    a=a.upper()
    return a

result=get_summ('Learn', 'Python', delimiter='&')
print(result)

