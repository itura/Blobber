import threading
from collections import deque

class SocketWrapper:
  def __init__(self, sock):
    self.sock = sock 

  #serialize the given key, data pair and send it 
  def sendData(self, key, data):
    serialPair = jsonpickle.encode((key, data))
    message = str(len(serialPair)) + " " + serialPair
    self.sock.send(message)

  #send the given message
  def sendMessage(self, message):
    self.sock.send(str(len(message)) + " " + message)

  def recvMessage(self):
    data = ''
    nextByte = ''
    while nextByte != ' ':
      nextByte = self.sock.recv(1)
      data += nextByte
    messageSize = int(data)
    message = self.sock.recv(messageSize)
    return message

class StoppableThread(threading.Thread):
    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop = threading.Event()
    def stop(self):
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()

class BBuffer:
  def __init__(self, maxSize):
    self.maxSize = maxSize
    self.lock = threading.Lock()
    self.buffer = deque()

  def push(self, data):
    if self.buffer.count == self.maxSize:
      return False

    self.lock.acquire()
    try:
      self.buffer.append(data)
    finally:
      self.lock.release()

    return True

  def pop(self):
    if self.buffer.count == 0:
      return None

    self.lock.acquire()
    try:
      data = self.buffer.popleft()
    finally:
      self.lock.release()

    return data