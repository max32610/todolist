from tasker import Tasker
user1 = Tasker()
print('Добро пожаловать в ваши Задачи')
while True:
 try:
  option = int(input('Выберите действие:1)Добавить задачу 2)Показать текущие задачи 3)Выполнить задачу 4)Выйти '))
 except ValueError:
    print('Пожалуйста введите число')
    continue

 if option == 1:
   print('Напишите какую задачу вы хотите добавить')
   user1.add_task(input(''))
 elif option == 2:
   print('Вот ваши текущие задачи')
   user1.list_tasks()
 elif option == 3:
   print('Введите id задачи которую уже выполнили')
   user1.mark_done(int(input('')))
 elif option == 4:
    print('До встречи')
    break