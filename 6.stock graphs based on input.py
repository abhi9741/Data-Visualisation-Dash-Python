import dash
from dash.dependencies import Input, Output
import dash_core_components as core
import dash_html_components as html

import pandas_datareader.data as web
import datetime


app=dash.Dash()
app.layout = html.Div([
 
 html.Div(
 html.Div("Stock Graphs"),style={'color':'blue','font':'heldgsgevitica','fontSize':60,'align':'center'}  ),
 
core.Input(id='input1',value='enter the stock id ',type='text'), 

html.Div(id="output-graph")
],style={'marginBottom': 50, 'marginTop': 25}) 


@app.callback(
       Output(component_id='output-graph',component_property='children'),
       [Input(component_id='input1',component_property='value')]
               )
def update_graph(input1_data):
      
      start = datetime.datetime(2015,1,1)
      end = datetime.datetime.now()
      stock =input1_data
      df = web.DataReader(stock,'google',start,end)
      return core.Graph(id="graph-2",figure={
            'data':[{'x':df.index,'y':df.Close,'name':stock,'type':'line'},
             ],
             'layout':{'title':stock+" stock"}})

if __name__ == '__main__' :
	app.run_server(debug=True)
	
	







