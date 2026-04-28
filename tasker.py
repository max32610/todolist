from task import Task
import json
def save(func):
     def wrapper(self,*args,**kwargs):
         before = [t.to_dict() for t in self.tasks]
         res = func(self,*args,**kwargs)
         after = [t.to_dict() for t in self.tasks]
         if before != after:
             self.save_tasks()
         return res
     return wrapper
class Tasker:
 def __init__(self):
    self.tasks = []
    self.next_id = 1 
 def save_tasks(self):
     with open('tasks.json', 'w', encoding='utf-8') as f:
         json.dump([t.to_dict() for t in self.tasks],f, indent=4, ensure_ascii=False)
 @save 
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
    task = Task(self.next_id, text, priority)
    self.tasks.append(task)
    self.next_id += 1
 def list_tasks(self):
    for task in self.tasks:
        print(f"{task.id}) {task.task} | {'✔' if task.done else '❌'} | 'Приоритет':{task.priority}")
 @save
 def mark_done(self, given_id):
    for task in self.tasks:
        if task.id == given_id:
            task.mark_done()
            print('Хорошая работа')
            return
    print('Задача не найдена')
 @save          
 def delete_task(self, task_id):  
    self.tasks = [t for t in self.tasks if t.id != task_id]
 def confirm_action(self):
     answ = input('Вы уверены (y/n): ')
     return answ == 'y'