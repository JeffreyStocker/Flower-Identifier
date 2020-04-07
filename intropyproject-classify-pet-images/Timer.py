import time

class Timer:
  def __init__(self, discription = ''):
    self.ended = False
    self.times = []
    self.stop_time = None
    self.start_time = self.mark(discription)

  def mark(self, discription = ''):
    if not self.ended:
      currentTime = time.time()
      self.times.append((time, discription))
    else:
      currentTime = None
    return currentTime

  def stop(self, discription = ''):
    if not self.ended:
      endTime = self.mark(discription)
      self.stop_time = endTime
      self.ended = True
      return self.delta()
    else:
      return None

  def delta(self, roundInt = 2):
    if self.start_time and self.stop_time:
      return round(float(self.stop_time - self.start_time), roundInt)
    else:
      return None

  def output_final(self):
    if self.ended:
      delta = self.delta()

      hours = str( int( (delta / 3600) ) )
      minutes = str( int(  ( (delta % 3600) % 60 ) ) )
      seconds = str( int(  ( (delta % 3600) / 60 )  ) )

      return hours  + ":" + minutes + ":" + seconds
    else:
      return 'Not Ended Yet'
