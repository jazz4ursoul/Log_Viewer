import PySimpleGUI as sg
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure

from matplotlib import dates
from log_pars import read_logs


def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


layout = [
    [sg.Canvas(size=(740, 580), key='-CANVAS-')],
    [sg.Text('File: '), sg.InputText(), sg.FileBrowse(), sg.Checkbox('rx1'), sg.Checkbox('rx2')],
    [sg.Button('Submit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14')],
    [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14')]
]

window = sg.Window("log_pars", layout, finalize=True)

canvas = window['-CANVAS-'].TKCanvas

fmt = dates.DateFormatter('%H:%M:%S')

fig, ax = plt.subplots()

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.grid()
fig_agg = draw_figure(canvas, fig)

while True:
    event, value = window.read()
    if event in ('Exit', None):
        break
    if event == 'Submit':
        path = value[0]
        need_to_print_rx1 = value[1]
        need_to_print_rx2 = value[2]
        time1, rx1, time2, rx2 = read_logs(path)
        ax.cla()
        if need_to_print_rx1:
            ax.plot(time1, rx1, c='r')
        if need_to_print_rx2:
            ax.plot(time2, rx2, c='g')

        ax.xaxis.set_major_formatter(fmt)

        ax.legend(["rx1", "rx2"])

        ax.grid()

        fig.autofmt_xdate()
        fig_agg.draw()

window.close()
