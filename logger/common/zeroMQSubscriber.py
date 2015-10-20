from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler
from logger.common.Constants import Constants

class MyZeroMQSubscriber:

  def __init__(self):
    self.subscriber = ZeroMQSubscriber(Constants.SOCKET)

  def startSubscriber(self):
    with TimedRotatingFileHandler('/home/asmi/compute/subscriber1/foo.log', date_format='%Y-%m-%d %H:%M'):
      self.subscriber.dispatch_forever()

