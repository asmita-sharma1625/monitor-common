from logbook import TimedRotatingFileHandler
from multiprocessing import Queue
from logbook.queues import MultiProcessingSubscriber
from test import queue

#queue = Queue(-1)
subscriber = MultiProcessingSubscriber(queue.queue)
controller = subscriber.dispatch_in_background(TimedRotatingFileHandler('multiprocessfoo.log'))
subscriber.dispatch_in_background(TimedRotatingFileHandler('foo.log'))
a = 1
while a > 0:
  record = subscriber.recv()
  print "**** Log Record **** \n" , record
controller.stop()

