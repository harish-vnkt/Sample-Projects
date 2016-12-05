from bokeh.plotting import figure
from bokeh.models import Select,Slider,ColumnDataSource
from bokeh.io import curdoc,output_file,show
from bokeh.layouts import widgetbox,row
import numpy as np
from numpy.random import randint 
x = np.linspace(0,100)
y = x+randint(100)
source = ColumnDataSource(data = {"x":x,"y":y})
def update_graph(attr,old,new):
	new = type_select.value
	start = slider_start.value
	end = slider_end.value
	new_range = np.linspace(start,end)
	if new=="Linear":
		new_data = {
			"x" : new_range,
			"y" : x+randint(100)
		}
	elif new=="Quadratic":
		new_data = {
			"x" : new_range,
			"y" : (randint(100)*(x**2)) + (randint(100)*x) + randint(100)
		}	
	elif new=="Exponential":
		new_data = {
			"x" : new_range,
			"y" : randint(100)*(x**randint(10))
		}
	elif new=="Logarithmic":
		new_data = {
			"x" : new_range,
			"y" : randint(100)*np.log(x) + randint(100)
		}
	else:
		new_data = {
			"x" : new_range,
			"y" : np.sin(x)
		}
	source.data = new_data
	plot.title.text(new)
	plot.x_range.start = min(data[x])
	plot.x_range.end = max(data[x])
	plot.y_range.start = min(data[y])
	plot.y_range.end = max(data[y])
plot = figure(x_axis_label="x",y_axis_label="y")
plot.line("x","y",source=source)
type_select = Select(title="Graph type",options=["Linear","Quadratic","Exponential","Logarithmic","Sinusoidal"],value="Linear")
type_select.on_change("value",update_graph)
slider_start = Slider(title="Start",start=-100,end=100,step=1,value=0)
slider_start.on_change("value",update_graph)
slider_end = Slider(title="Start",start=-100,end=100,step=1,value=100)
slider_end.on_change("value",update_graph)
layout = row(widgetbox(type_select,slider_start,slider_end),plot)
curdoc().add_root(layout)