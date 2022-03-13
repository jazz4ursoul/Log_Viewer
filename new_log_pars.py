import datetime as dt


def read_logs(log: str):
    file = open(log, 'r')
    s = file.readline()
    logs_rx1 = []
    t1 = []
    logs_rx2 = []
    t2 = []
    while s:
        s = s.split()
        mod = 0
        if len(s) > 4:
            if s[2] == 'rx' and s[4] == 'snr':
                mod = 1
            elif s[2] == 'rx2' and s[4] == 'snr':
                mod = 2
        if mod == 1:
            s = file.readline().split()
            time = s[0][1:s[0].rfind(':')]
            signal = max(0.0, float(s[-1]))
            logs_rx1.append(signal)
            t1.append(time)
        if mod == 2:
            s = file.readline().split()
            time = s[0][1:s[0].rfind(':')]
            signal = max(0.0, float(s[-1]))
            logs_rx2.append(signal)
            t2.append(time)
        s = file.readline()

    t1 = [dt.datetime.strptime(i, "%H:%M:%S") for i in t1]
    t2 = [dt.datetime.strptime(i, "%H:%M:%S") for i in t2]
    return (t1, logs_rx1, t2, logs_rx2)
