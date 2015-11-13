from logbook import FileHandler
from logbook import FingersCrossedHandler, GMailHandler

class TriggerHandler:
  
  def __init__(self):
    self.handler = GMailHandler("itsmeasmi25@gmail.com", "asmi9971026789", "asmita_sharma@outlook.com")

  def getTriggerHandler(self):
    return self.handler
