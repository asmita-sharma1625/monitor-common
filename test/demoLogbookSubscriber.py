from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler
#from logger.common.logbookRotator import rotator

subscriber = ZeroMQSubscriber('tcp://127.0.0.1:6000')
#controller = subscriber.dispatch_in_background(TimedRotatingFileHandler('/home/asmi/compute/foo.log', date_format='%Y-%m-%d %H:%M'))
#a = 1
#while a > 0:
#  record = subscriber.recv()
#  print "**** Log Record **** \n" , record.message
#controller.stop()

with TimedRotatingFileHandler('/home/asmi/compute/foo.log', date_format='%Y-%m-%d %H:%M'):
  subscriber.dispatch_forever()

