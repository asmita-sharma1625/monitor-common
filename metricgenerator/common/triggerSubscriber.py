from logbook.queues import ZeroMQSubscriber
from common.fingersCrossedHandler import TriggerHandler

class TriggerSubscriber:

    def __init__(self):
        print "subscriber initiated"
        # multi = True for bind() call on socket
        self.subscriber = ZeroMQSubscriber(Constants.getSocket(), multi = True)

    def startSubscriber(self, filepath):
        print "subscriber started"
        with GmailHandler("itsmeasmi25@gmail.com", "asmi9971026789", "asmita_sharma@outlook.com"):
            print "log received : ", self.subscriber.recv()
            self.subscriber.dispatch_forever()
