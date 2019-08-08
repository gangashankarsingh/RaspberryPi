import tm1637
from time import sleep, localtime

tm = tm1637.TM1637(CLK=40, DIO=38, brightness=1.0)


while True:
    tm.Clear()
    t = localtime()
    hr = str(t.tm_hour)
    mins = str(t.tm_min)

    if len(hr) < 2:
        hr = '0' + hr
    if len(mins) < 2:
        mins = '0' + mins 

    data = [ int(hr[0]) , int(hr[1]),int(mins[0]) , int(mins[1])]

    tm.Show(data)
    tm.ShowDoublepoint(True)
    sleep(1)
    

