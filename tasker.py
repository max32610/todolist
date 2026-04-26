from task import Task
class Tasker:
 def __init__(self):
    self.tasks = []
    self.next_id = 1  
 def add_task(self,text):
    print('Выберите насколько важна ваша задача: ')
    try:
       answ = int(input('low-1 medium-2 high-3 '))
    except ValueError:
       print('Введите число')
       return
    if answ == 1:
          priority = 'low'
    elif answ == 2:
          priority = 'medium'
    elif answ == 3:
          priority = 'high'
    task = Task(1, text, priority)
    self.tasks.append(task)
    self.next_id += 1
    return self.tasks
 def list_tasks(self):
    for task in self.tasks:
        print(f"{task.id}) {task.task} | {'✔' if task.done else '❌'} | 'Приоритет':{task.priority}")
 def mark_done(self, given_id):
    for task in self.tasks:
        if task.id == given_id:
            task.mark_done()
            print('Хорошая работа')
            return
    print('Задача не найдена')
            
 def delete_task(self, task_id):  
    self.tasks = [t for t in self.tasks if t.id != task_id]
 def confirm_action(self):
     answ = input('Вы уверены (y/n): ')
     return answ == 'y'
 