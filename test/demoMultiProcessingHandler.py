from multiprocessing import Queue
from logbook.queues import MultiProcessingHandler
from test import queue

#queue = Queue(-1)
handler = MultiProcessingHandler(queue.queue)
