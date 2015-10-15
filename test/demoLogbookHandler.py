from logbook.queues import ZeroMQHandler

mySocket1 = 'tcp://127.0.0.1:6000'
mySocket2 = 'tcp://127.0.0.1:5000'
handler = ZeroMQHandler(mySocket2)

