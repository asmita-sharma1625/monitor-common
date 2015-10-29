from logbook.queues import ZeroMQHandler

class MyZeroMQHandler:

  def __init__(self, socket):
    # multi = True to for connect() instead of bind() call on socket
    self.handler = ZeroMQHandler(socket, multi = True)

  def getZeroMQHandler(self):
    return self.handler

