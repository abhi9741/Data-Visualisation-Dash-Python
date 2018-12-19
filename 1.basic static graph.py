import dash
import dash_core_components as dcc
import dash_html_components as html

myapp=dash.Dash();

myapp.layout=html.Div([

html.H1("Welcome to Graph World "),
dcc.Graph(id="graph-1",figure={
'data':[{'x':[1,2.5,3,4,5],'y':[6,7,8.8,9,10],'name':"Boats",'type':'line'},
{'x':[6,7.7,8,9,10],'y':[1.1,2,3,4,5],'type':'bar','name':"Cars"}
], #data input ends here
'layout':{'title':"Baisc-Graph-Demonstration"}
} # figure ends here
) #graph ends here 
])

if __name__ == "__main__":
  myapp.run_server()
