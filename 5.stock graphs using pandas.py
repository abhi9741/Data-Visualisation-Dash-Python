import dash
from dash.dependencies import Input, Output
import dash_core_components as core
import dash_html_components as html

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015,1,1)
end = datetime.datetime.now()

stock ='TSLA'

df = web.DataReader(stock,'google',start,end)

app=dash.Dash()
app.layout = html.Div([
 
 html.Div(
 html.Div("Stock Graphs"),style={'color':'blue','font':'heldgsgevitica','fontSize':60,'align':'center'}  ),
 
 

core.Graph(id="graph-2",figure={
'data':[{'x':df.index,'y':df.Close,'name':stock,'type':'line'},
],
'layout':{'title':stock+" stock"}})
],style={'marginBottom': 50, 'marginTop': 25}) #  



if __name__ == '__main__' :
	app.run_server(debug=True)
	
	














# print(df.head())
