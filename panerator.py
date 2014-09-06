
#Авторство
__author__='Major Tom'
#Импорт модулей
from random import choice

#Ввод данных

size=int(input('Введите размер пароля: '))
print('[1] Сгенерировать пароль из заглавных букв\n[2] Сгенерировать пароль из строчных букв\n[3] Сгенерировать пароль из цифр\nВы можете комбинировать пароли.При комбинации вводите параметры по возрастанию')

zag='A','B','C''D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
stro='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
cifr='1','2','3','4','5','6','7','8','9','0'
password=''
a=str(input('Введите параметры пароля: '))
#Генерация
if a=='1':
 print( password.join([choice(zag) for i in range(size)]))
elif a=='2':
 print( password.join([choice(stro) for i in range(size)]))
elif a=='3':
 print( password.join([choice(cifr) for i in range(size)]))
elif a=='12' :
 print( password.join([choice(zag+stro) for i in range(size)]))
elif a=='13' :
 print( password.join([choice(zag+cifr) for i in range(size)]))
elif a=='23':
 print( password.join([choice(stro+cifr) for i in range(size)]))
elif a=='123' :
 print( password.join([choice(stro+cifr+zag) for i in range(size)]))
print('Пароль сгенерирован')
