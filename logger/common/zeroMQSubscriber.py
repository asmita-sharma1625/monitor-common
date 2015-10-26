from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler
from logger.common.Constants import Constants

class MyZeroMQSubscriber:

  def __init__(self):
   # print "subscriber initiated"
    self.subscriber = ZeroMQSubscriber(Constants.getSocket())

  def startSubscriber(self, filepath):
   # print "subscriber started"
    with TimedRotatingFileHandler(filepath, date_format='%Y-%m-%d %H:%M'):
      self.subscriber.dispatch_forever()

