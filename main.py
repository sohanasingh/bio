import urllib.request as urlreq
from dash import Dash, html
import dash_bio as dashbio

app = Dash(__name__)

data = ('lobster.fasta') #.read().decode('utf-8')

app.layout = html.Div([
    dashbio.AlignmentChart(
        id='alignment-viewer',
        data=data
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)