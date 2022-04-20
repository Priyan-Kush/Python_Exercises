class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
    def addTime(self, time1, time2):
        return Time(time1.hours + time2.hours, time1.minutes + time2.minutes)
    def displayTime(self):
        print(self.hours, "hr", self.minutes, "min")
    def displayMinute(self):
        print( self.hours * 60 + self.minutes,"mins")

time1 = Time(1,2)
time2 = Time(1,2)
addedTime = Time().addTime(time1, time2)
addedTime.displayTime()
addedTime.displayMinute()
