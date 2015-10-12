
class Publish:
  def __init__(self, f):
    self.f = f

  def __call__(self, f):
    #Start
    self.f()
    #Stop

