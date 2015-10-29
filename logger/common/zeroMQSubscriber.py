from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler
from logger.common.Constants import Constants

class MyZeroMQSubscriber:

  def __init__(self):
    print "subscriber initiated"
    # multi = True for bind() call on socket
    self.subscriber = ZeroMQSubscriber(Constants.getSocket(), multi = True)

  def startSubscriber(self, filepath):
    print "subscriber started"
    with TimedRotatingFileHandler(filepath, date_format='%Y-%m-%d %H:%M'):
      print "log received : ", self.subscriber.recv()
      self.subscriber.dispatch_forever()

