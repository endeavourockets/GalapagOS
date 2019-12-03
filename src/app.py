import os

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)

app.title = 'GalapagOS'
server = app.server

app.index_string = '''
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="msapplication-TileColor" content="#2d89ef">
    <meta name="theme-color" content="#4188c9">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="HandheldFriendly" content="True">
    <meta name="MobileOptimized" content="320">
    {%favicon%}
    <title>{%title%}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,300i,400,400i,500,500i,600,600i,700,700i&amp;subset=latin-ext">
    <!-- Dashboard Core -->
    <link href="./assets/css/dashboard.css" rel="stylesheet">
    <script src="./assets/js/dashboard.js"></script>
</head>

<body class="">
    <div class="page">
	<div class="flex-fill">
	<div class="header py-4" style="background:#142047">
	    <div class="container">
	      <div class="d-flex">
		<a class="header-brand" href="./index.html">
		  <img src="./assets/images/logo/endeavour.png" class="header-brand-img" alt="tabler logo">
		</a>
	      <div class="d-flex order-lg-2 ml-auto">
		<h1 style='color:#fff'>{%title%}</h1>
	      </div>
	      </div>
	    </div>
	</div>
	<div class="my-3 my-md-5">
          <div class="container">
	    {%app_entry%}
          </div>
	</div>
        </div>
        </div>
    </div>
    <footer>
	{%config%}
	{%scripts%}
	{%renderer%}
    </footer>
</body>
</html>
'''

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
