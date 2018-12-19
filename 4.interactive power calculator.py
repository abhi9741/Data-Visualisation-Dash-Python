import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
       html.H1("Basic Interactive Power Calculator"),
       dcc.Input(id="input",value="Enter a name",type='text'),
       html.Div(id="output")
      ])     
      
@app.callback(
           Output(component_id='output',component_property='children'),
           [Input(component_id='input',component_property='value')]
           )
           
def update_value(input_data):
   try :
	return "the power of given number :{}".format(str(float(input_data)**2))
   except :
        return "please enter a  number "

if __name__=='__main__':
	app.run_server(debug=True)
