class Task:
   def __init__(self,id,text,priority):
    self.id = id
    self.task = text
    self.done = False
    self.priority = priority
   def mark_done(self):
      self.done = True