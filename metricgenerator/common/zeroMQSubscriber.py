from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler, GMailHandler
from logger.common.Constants import Constants
import zmq

class MyZeroMQSubscriber:

  def __init__(self):
    print "subscriber initiated"
    # multi = True for bind() call on socket
    try:	
      self.subscriber = ZeroMQSubscriber(Constants.getSocket(), multi = True)
    except zmq.error.ZMQError as error:
      print "error while binding to socket :" + Constants.getSocket()
      raise zmq.error.ZMQError("error while binding to socket :" + Constants.getSocket())

  def startSubscriber(self, filepath):
    print "subscriber started"
    with TimedRotatingFileHandler(filepath, date_format='%Y-%m-%d %H:%M', level = "ERROR"):
      print "log received : "
      self.subscriber.dispatch_forever()


