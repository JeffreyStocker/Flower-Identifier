import time

class Timer:
  def __init__(self, discription):
    self.times = []
    self.start = self.mark(discription)
    self.stop = None

  def mark(self, discription):
    if not self.stop:
      time = time()
      self.times.append((time, discription))
    else:
      time = None
    return time

  def stop(self, discription):
    if not self.stop:
      endTime = self.mark(discription)
      self.stop = endTime
      return self.delta()
    else:
      return None

  def delta(self, roundInt = 2):
    if self.start and self.stop:
      return round(float(self.stop - self.start), roundInt)
    else:
      return None

  def __str__(self):
    delta = self.delta()

    hours = str( int( (delta / 3600) ) )
    minutes = str( int(  ( (delta % 3600) % 60 ) ) )
    seconds = str( int(  ( (delta % 3600) / 60 )  ) )

    return hours  + ":" + minutes + ":" + seconds
