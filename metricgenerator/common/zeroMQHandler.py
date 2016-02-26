from logbook.queues import ZeroMQHandler
import zmq
import logging

log = logging.getLogger("metricgenerator")

class MyZeroMQHandler:
    def __init__(self, socket, zmqcontext):
        #print "queue socket : ", socket
        # multi = True to for connect() instead of bind() call on socket
        try:
            #print "@@@@@@@@@@@@@@ not using socket"
            self.handler = ZeroMQHandler(socket, context = zmqcontext, multi = True)
            #print "ZeroMQHandler instantiated"
        except zmq.error.ZMQError as error:
            log.error("Incorrect Context to ZMQ Handler : " + socket, error)
            raise Exception("Incorrect Context to ZMQ Handler : " + socket)

    def getZeroMQHandler(self):
        #print "returning ZeroMQHandler: ", `self.handler`
        return self.handler

