class Time:
    def __init__(self, hr, min, sec):
        self.__hr = hr
        self.__min = min
        self.__sec = sec

    def __add__(self, other):
        second = (self.__sec + other.__sec)%60
        minute = (self.__min + other.__min)%60 + (self.__sec + other.__sec)//60
        hour = (self.__hr + other.__hr)%60 + (self.__min + other.__min)//60
        sum = Time(hour, minute, second)
        sum.get_time()

    def get_time(self):
        #format_time = lambda time: "0"+str(time) if len(str(time)<2)
        print(f"{self.__hr}:{self.__min}:{self.__sec}")


hour, minute, second = map(int, input("Enter time: Hour, Minute, second: ").split())
T1 = Time(hour, minute, second)

hour, minute, second = map(int, input("Enter time: Hour, Minute, second: ").split())
T2 = Time(hour, minute, second)

T1+T2
