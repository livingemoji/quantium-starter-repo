"""
Dash application to visualize Pink Morsel sales data over time.
Answers the question: Were sales higher before or after the price increase on Jan 15, 2021?
Includes region filtering and enhanced styling.
"""
import os
import pandas as pd
from dash import Dash, dcc, html, callback, Input, Output
import plotly.graph_objects as go

# Load and prepare data
df = pd.read_csv('data/processed_sales.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Create Dash app
app = Dash(__name__)

# Define custom CSS styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

def create_figure(selected_region):
    """Create line chart filtered by selected region."""
    if selected_region == 'all':
        # Group by date and calculate total daily sales
        chart_data = df.groupby('Date')['Sales'].sum().reset_index()
        title_suffix = 'All Regions'
    else:
        # Filter by region first, then group by date
        region_df = df[df['Region'] == selected_region]
        chart_data = region_df.groupby('Date')['Sales'].sum().reset_index()
        title_suffix = f'{selected_region.capitalize()} Region'
    
    chart_data = chart_data.sort_values('Date')
    chart_data['Sales'] = pd.to_numeric(chart_data['Sales'], errors='coerce')
    
    # Create the line chart
    fig = go.Figure()
    
    # Determine color based on region
    color_map = {
        'north': '#FF6B6B',
        'south': '#4ECDC4',
        'east': '#45B7D1',
        'west': '#FFA07A',
        'all': '#667EEA'
    }
    
    line_color = color_map.get(selected_region, '#667EEA')
    
    fig.add_trace(go.Scatter(
        x=chart_data['Date'],
        y=chart_data['Sales'],
        mode='lines',
        name='Daily Sales',
        line=dict(color=line_color, width=3),
        fill='tozeroy',
        fillcolor=f'rgba({int(line_color[1:3], 16)}, {int(line_color[3:5], 16)}, {int(line_color[5:7], 16)}, 0.15)',
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
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="red",
        borderwidth=2,
        font=dict(color="red", size=11, family='Arial')
    )
    
    # Update layout with titles and labels
    fig.update_layout(
        title={
            'text': f'Pink Morsel Sales - {title_suffix}',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': '#333'}
        },
        xaxis_title='Date',
        yaxis_title='Daily Sales ($)',
        hovermode='x unified',
        plot_bgcolor='rgba(250,250,250,0.9)',
        paper_bgcolor='white',
        font=dict(family='Segoe UI, sans-serif', size=12),
        margin=dict(l=80, r=80, t=100, b=80),
        height=600,
        showlegend=False
    )
    
    # Format y-axis as currency
    fig.update_yaxes(tickformat='$,.0f', gridcolor='rgba(200,200,200,0.2)')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(200,200,200,0.1)')
    
    return fig

# Create app layout
app.layout = html.Div([
    # Header
    html.Header([
        html.H1(' Pink Morsel Sales Dashboard', 
                 style={
                     'textAlign': 'center',
                     'marginBottom': 10,
                     'color': '#fff',
                     'fontSize': 36,
                     'fontWeight': 'bold',
                     'textShadow': '2px 2px 4px rgba(0,0,0,0.2)'
                 }),
        html.P('Analyzing sales impact of the price increase on January 15, 2021',
               style={
                   'textAlign': 'center',
                   'color': 'rgba(255,255,255,0.9)',
                   'fontSize': 16
               })
    ], style={
        'padding': '40px 20px',
        'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'borderBottom': '4px solid rgba(255,255,255,0.3)',
        'marginBottom': '30px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    }),
    
    # Main container
    html.Div([
        # Filter section
        html.Div([
            html.Label('Select Region:', 
                      style={
                          'display': 'block',
                          'marginBottom': '12px',
                          'fontSize': '16px',
                          'fontWeight': '600',
                          'color': '#333'
                      }),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': ' All Regions', 'value': 'all'},
                    {'label': ' North', 'value': 'north'},
                    {'label': ' South', 'value': 'south'},
                    {'label': ' East', 'value': 'east'},
                    {'label': ' West', 'value': 'west'}
                ],
                value='all',
                inline=True,
                style={'display': 'flex', 'gap': '25px'},
                labelStyle={
                    'display': 'inline-block',
                    'marginRight': '0px',
                    'cursor': 'pointer',
                    'userSelect': 'none'
                },
                inputClassName='region-radio'
            )
        ], style={
            'backgroundColor': '#f8f9fa',
            'padding': '20px',
            'borderRadius': '8px',
            'marginBottom': '25px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.05)',
            'border': '1px solid #e0e0e0'
        }),
        
        # Chart section
        html.Div([
            dcc.Graph(
                id='sales-chart',
                style={'margin': '0'},
                config={'responsive': True, 'displayModeBar': True}
            )
        ], style={
            'backgroundColor': 'white',
            'borderRadius': '8px',
            'padding': '20px',
            'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
            'marginBottom': '25px'
        }),
        
        # Info section
        html.Div([
            html.P(
                ' Tip: Hover over the chart to see exact sales values for each day. The red dashed line marks the price increase date.',
                style={
                    'color': '#555',
                    'fontSize': '14px',
                    'fontStyle': 'italic',
                    'margin': '0',
                    'padding': '12px',
                    'backgroundColor': '#e3f2fd',
                    'borderLeft': '4px solid #667eea',
                    'borderRadius': '4px'
                }
            )
        ])
    ], style={
        'maxWidth': '1200px',
        'margin': '0 auto',
        'padding': '0 20px'
    }),
    
    # Footer
    html.Footer([
        html.P(
            ' Data represents daily total sales of Pink Morsels. Analysis shows clear revenue impact from the price increase.',
            style={
                'textAlign': 'center',
                'color': '#fff',
                'fontSize': '14px',
                'marginBottom': '8px'
            }
        ),
        html.P(
            '© 2025 Soul Foods Analytics | Pink Morsel Sales Dashboard',
            style={
                'textAlign': 'center',
                'color': 'rgba(255,255,255,0.7)',
                'fontSize': '12px'
            }
        )
    ], style={
        'padding': '30px 20px',
        'textAlign': 'center',
        'background': 'linear-gradient(135deg, #764ba2 0%, #667eea 100%)',
        'marginTop': '40px',
        'borderTop': '4px solid rgba(255,255,255,0.3)'
    })
], style={
    'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
    'backgroundColor': '#f5f5f5',
    'minHeight': '100vh'
})

# Callback to update chart based on region selection
@callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    return create_figure(selected_region)

# Production server configuration
server = app.server

if __name__ == '__main__':
    # Get port from environment variable, default to 8080 for local development
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)
