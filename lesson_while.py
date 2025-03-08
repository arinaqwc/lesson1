#функция:
   # бесконечно выполяй следующее:
        #спроси у пользователя "как дела"
        #если он ответил "хорошо", то выйди

def ask_user():
    while True:
        answer=input('Как дела? ').strip().lower()
        if answer=='хорошо':
            break
    
ask_user()
        
        



    


