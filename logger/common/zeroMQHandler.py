from logbook.queues import ZeroMQHandler

class MyZeroMQHandler:

  def __init__(self, socket):
    self.handler = ZeroMQHandler(socket)

  def getZeroMQHandler(self):
    return self.handler

