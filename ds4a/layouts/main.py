import dash_html_components as html
import dash_core_components as dcc
from ds4a.layouts.header import header
from ds4a.components.analytics import analitycs
from ds4a.layouts.tabs import tabs
from ds4a.layouts.inputs import layout_inputs



metrics = [
    {'label': 'Agency 1 Drivers', 'selected': 'true', 'model': 'drivers_model_a1'},
    {'label': 'Agency 1 Drivers - ALO', 'selected': 'true', 'model': 'drivers_model_a1_alo'},
    {'label': 'Agency 2 Drivers', 'selected': 'true', 'model': 'drivers_model_a2'},
    {'label': 'Agency 2 Drivers - ALO', 'selected': 'true', 'model': 'drivers_model_a2_alo'},

]

metrics2 = [
    {'label': 'Agency 1 Daily Itineraries', 'selected': 'true', 'model': 'itineraries_model_a1'},
    {'label': 'Agency 2 Daily Itineraries', 'selected': 'true', 'model': 'itineraries_model_a2'},
]

metrics3 = [
    {'label': 'A1 daily Drivers Prediction', 'selected': 'true', 'model': 'predict_daily_drivers_model_a1'},
    {'label': 'A1 daily Drivers ALO Prediction', 'selected': 'true', 'model': 'predict_daily_drivers_model_a1_alo'},
    {'label': 'A2 daily Drivers Prediction', 'selected': 'true', 'model': 'predict_daily_drivers_model_a2'},
    {'label': 'A2 daily Drivers ALO Prediction', 'selected': 'true', 'model': 'predict_daily_drivers_model_a2_alo'},

]

metrics4 = [
    {'label': 'A1 hourly Drivers Prediction', 'selected': 'true', 'model': 'predict_hourly_drivers_model_a1'},
    {'label': 'A2 hourly Drivers Prediction', 'selected': 'true', 'model': 'predict_hourly_drivers_model_a2'},    
]

metrics5 = [
    {'label': 'A1 hourly Drivers ALO Prediction', 'selected': 'true', 'model': 'predict_hourly_drivers_model_a1_alo'},
    {'label': 'A2 hourly Drivers ALO Prediction', 'selected': 'true', 'model': 'predict_hourly_drivers_model_a2_alo'},    
]


main_layout = html.Div(
    [
        html.Div(header, className=''),
        html.Div(
            [
                html.Div(
                    html.Div(
                        [
                            html.H1("Controls", className='title'),
                            layout_inputs
                        ],
                        className='controls',
                        id='controls'
                    ),
                    className="col-lg-3 col-12"
                ),
                html.Div(
                    [
                        html.Div([analitycs(metrics4)],className=""),
                        html.Div([analitycs(metrics5)],className=""),
                        html.Div([analitycs(metrics3)],className=""),
                        html.Div([analitycs(metrics)],className=""),
                        html.Div([analitycs(metrics2)],className=""),

                    ],
                    className="col-lg-9 col-12" 
                ),
            ],
            className="row"
        ),
#        html.Div(
#            html.Div(
#                tabs,
#                className="col-lg-9 col-12"
#            ),
#            className="row"
#        ),
    ],
    className="container-fluid"
)