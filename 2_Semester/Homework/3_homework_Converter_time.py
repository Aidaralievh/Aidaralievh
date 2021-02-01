class Time:
    def __init__(self):
        self.time = int(input('Enter amount of seconds: '))

    def converter(self):
        days = self.time // 86400
        hours = (self.time % 86400) // 3600
        minutes = (self.time % 3600) // 60
        seconds = (self.time % 60)
        print("Converted time:", days, "days,", hours, "hours,", minutes, "minutes,", "and", seconds, "seconds.")


time = Time()
time.converter()