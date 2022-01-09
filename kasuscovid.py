#import libraries
import pandas as pd

from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import HoverTool, ColumnDataSource

"""Dataset"""

#membaca dataset dan melhat data teratas dari dataset
df = pd.read_csv("covid.csv")
df.head()

#mengubah tipe data date menjadi datetime
df['date'] = pd.to_datetime(df.date)

#melihat tipe data pada setiap kolom dataset
df.info()

#inisialisasi kedalam cds agar bisa ditampilkan di figure
cds_covid = ColumnDataSource(df)

"""Pembuatan figure kasus positif covid"""

#membuat figure kasus positif covid
fig_positive = figure(x_axis_label='date', 
                      y_axis_label="Positive Cases",
                      x_axis_type='datetime', 
                      sizing_mode="stretch_width", 
                      plot_height=500,
                      plot_width= 1600)

fig_positive.line(x= df['date'], y= df['acc_confirmed'], line_color='blue')
fig_positive.legend.location = "top_right"

#membuat fitur hover pada figure
hover_positive = fig_positive.circle(x = "date",y = "acc_confirmed", 
                                    source= cds_covid, 
                                    hover_fill_color='blue', 
                                    alpha=0.5)
tooltips = [('date', '@date{%F}'), ('total cases', '@acc_confirmed'),]
fig_positive.add_tools(HoverTool(tooltips=tooltips, formatters={'@date': 'datetime'}, renderers=[hover_positive]))

"""Pembuatan figure kasus negatif covid"""

#membuat figure kasus negatif covid
fig_negative = figure(x_axis_label='date', 
                      y_axis_label="Negative Cases",
                      x_axis_type='datetime', 
                      sizing_mode="stretch_width", 
                      plot_height=500,
                      plot_width= 1600)
fig_negative.line(x= df['date'], y= df['acc_negative'], line_color='red')
fig_negative.legend.location = "top_right"

#membuat fitur hover pada figure
hover_negative = fig_negative.circle(x = "date",y = "acc_negative", 
                                    source= cds_covid, 
                                    hover_fill_color='red', 
                                    alpha=0.5)
tooltips = [('date', '@date{%F}'), ('total cases', '@acc_negative'),]
fig_negative.add_tools(HoverTool(tooltips=tooltips, formatters={'@date': 'datetime'}, renderers=[hover_negative]))

"""Pembuatan fitur tab"""

#inisialisasi fitur tab kasus positif
tab1 = Panel(child=fig_positive, title='COVID-19 Positive Cases')

#inisialisasi fitur tab kasus negatif
tab2 = Panel(child=fig_negative, title='COVID-19 Negative Cases')

curdoc().add_root(Tabs(tabs=[tab1, tab2]))
