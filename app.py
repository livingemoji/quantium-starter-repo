"""
Dash application to visualize Pink Morsel sales data over time.
Answers the question: Were sales higher before or after the price increase on Jan 15, 2021?
"""
import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go

# Load and prepare data
df = pd.read_csv('data/processed_sales.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Group by date and calculate total daily sales
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()
daily_sales = daily_sales.sort_values('Date')

# Convert Sales to numeric
daily_sales['Sales'] = pd.to_numeric(daily_sales['Sales'], errors='coerce')

# Create Dash app
app = Dash(__name__)

# Create the line chart
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=daily_sales['Date'],
    y=daily_sales['Sales'],
    mode='lines',
    name='Daily Total Sales',
    line=dict(color='#1f77b4', width=2),
    hovertemplate='<b>Date:</b> %{x|%Y-%m-%d}<br><b>Sales:</b> $%{y:,.2f}<extra></extra>'
))

# Add a vertical line at the price increase date (Jan 15, 2021)
price_increase_date = pd.to_datetime('2021-01-15')
fig.add_shape(
    type="line",
    x0=price_increase_date, x1=price_increase_date,
    y0=0, y1=1,
    yref="paper",
    line=dict(color="red", width=2, dash="dash"),
)

fig.add_annotation(
    x=price_increase_date,
    text="Price Increase<br>Jan 15, 2021",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="red",
    ax=40,
    ay=-40,
    bgcolor="rgba(255,255,255,0.8)",
    bordercolor="red",
    borderwidth=1,
    font=dict(color="red", size=11)
)

# Update layout with titles and labels
fig.update_layout(
    title={
        'text': 'Pink Morsel Sales Over Time',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 28}
    },
    xaxis_title='Date',
    yaxis_title='Daily Total Sales ($)',
    hovermode='x unified',
    plot_bgcolor='rgba(240,240,240,0.5)',
    paper_bgcolor='white',
    font=dict(family='Arial, sans-serif', size=12),
    margin=dict(l=80, r=80, t=100, b=80),
    height=600
)

# Format y-axis as currency
fig.update_yaxes(tickformat='$,.0f')

# Create app layout
app.layout = html.Div([
    html.Header([
        html.H1('Pink Morsel Sales Analysis', 
                 style={'textAlign': 'center', 'marginBottom': 10, 'color': '#333'}),
        html.P('Visualizing the impact of the price increase on January 15, 2021',
               style={'textAlign': 'center', 'color': '#666', 'fontSize': 16})
    ], style={'padding': '30px 20px', 'backgroundColor': '#f8f9fa', 'borderBottom': '1px solid #dee2e6'}),
    
    html.Div([
        dcc.Graph(figure=fig, style={'margin': '20px 0'})
    ], style={'padding': '20px', 'maxWidth': '1200px', 'margin': '0 auto'}),
    
    html.Footer([
        html.P('Data represents daily total sales of Pink Morsels across all regions.',
               style={'textAlign': 'center', 'color': '#999', 'fontSize': 12, 'marginTop': 20})
    ], style={'padding': '20px', 'textAlign': 'center', 'borderTop': '1px solid #dee2e6', 'backgroundColor': '#f8f9fa'})
], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#fff'})

if __name__ == '__main__':
    print("Starting Dash app on http://127.0.0.1:8050/")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True)
