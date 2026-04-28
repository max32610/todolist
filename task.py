class Task:
   def __init__(self,id,text,priority):
    self.id = id
    self.task = text
    self.done = False
    self.priority = priority
   def mark_done(self):
      self.done = True
   def to_dict(self):
     return {
        "id": self.id,
        "task": self.task,
        "priority": self.priority,
        "done": self.done
    }
   