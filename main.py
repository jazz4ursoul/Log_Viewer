import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as dt

from matplotlib import dates
from log_pars import read_logs

path = "/Users/Dmitry/Downloads/Telegram Desktop/mon_logs/isat/00.log"

time1, rx1, time2, rx2 = read_logs(path)

fmt = dates.DateFormatter('%H:%M:%S')

fig, ax = plt.subplots()

ax.plot(time1, rx1, c='r')
ax.plot(time2, rx2, c='g')

ax.xaxis.set_major_formatter(fmt)

ax.legend(["rx1", "rx2"])

ax.grid()

fig.autofmt_xdate()
fig.set_figwidth(12)
fig.set_figheight(7)

plt.show()