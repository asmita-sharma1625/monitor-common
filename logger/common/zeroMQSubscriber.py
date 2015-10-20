from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler

class MyZeroMQSubscriber:

  def __init__(self, socket):
    self.subscriber = ZeroMQSubscriber(socket)

  def startSubscriber(self):
    with TimedRotatingFileHandler('/home/asmi/compute/subscriber1/foo.log', date_format='%Y-%m-%d %H:%M'):
      self.subscriber.dispatch_forever()

