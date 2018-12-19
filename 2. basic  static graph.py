import dash
import dash_core_components as core
import dash_html_components as html

app=dash.Dash()
app.layout = html.Div([
 
 html.Div(
 html.Div(""),style={'color':'blue','font':'heldgsgevitica','fontSize':60,'align':'center'}  ),
 
 

core.Graph(id="graph-2",figure={
'data':[{'x':[1,2,3,4,5,6],'y':[43,53,50,57,59,67],'name':'temp in hyd','type':'line'},
{'x':[1,2,3,4,5,6],'y':[67,59,57,50,53,43],'name':"temp in banglore",'type':'line'}
],'layout':{'title':"Temparature graphs"}})
],style={'marginBottom': 50, 'marginTop': 25}) #  

if __name__ == '__main__' :
	app.run_server(debug=True)
	
	
	
'''
core.Graph(id="graph-1",figure={
'data':[{'x':[1,2,3,4,5],'y':[6,7,8,9,10],'name':"temperature",'type':'line'},
{'x':[6,7,8,9],'y':[1,2,3,4,5],'name':"temp 2",'type':'bar'}
],'layout':{'title':"Basic Graph Demonstration"}
}) # figure
'''	
