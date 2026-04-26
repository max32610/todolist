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
   user1.add_task(input('Введите задачу: '))

 elif option == 2:
    user1.list_tasks()

 elif option == 3:
    print('Введите id задачи которую уже выполнили')
    task_id = int(input())
    if user1.confirm_action():
        user1.mark_done(task_id)
 elif option == 4:
    print('До встречи')
    break