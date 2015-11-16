from logbook.queues import ZeroMQHandler
from monitorLog import monitorLog
import zmq

class MyZeroMQHandler:

  def __init__(self, socket):
    # multi = True to for connect() instead of bind() call on socket
    try:
      self.handler = ZeroMQHandler(socket, multi = True)
    except zmq.error.ZMQError as error:
      monitorLog.logError("Incorrect Context to ZMQ Handler : " + socket, error)
      raise Exception("Incorrect Context to ZMQ Handler : " + socket)

  def getZeroMQHandler(self):
    return self.handler

