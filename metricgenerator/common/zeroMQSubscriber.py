from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler, GMailHandler
from metricgenerator.common.Constants import Constants
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
        print "subscriber started" + `self.subscriber`
        with TimedRotatingFileHandler(filepath, date_format='%Y-%m-%d %H:%M'):
            print "log received : " + self.subscriber.recv().message
            self.subscriber.dispatch_forever()
