def get_answer():
    while True:
        response=input('Введите ваш вопрос: ').strip().lower()
        if response=='пока':
            break
        else:
            print('Не знаю как ответить')
        
get_answer()