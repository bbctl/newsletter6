import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Kim's Corner"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
                                            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
                                            Facilisis sed odio morbi quis commodo odio. Ac turpis egestas integer\
                                            eget aliquet nibh praesent tristique. Quam vulputate dignissim suspendisse \
                                            in est ante in nibh mauris. Volutpat sed cras ornare arcu dui vivamus arcu.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Operations Highlights"], className="subtitle"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Employee Engagement Index"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        [
                                                            "Highlighting the results:"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                    "EEI scores saw year over-year boosts from 62% to 69% in engagement and 53% to 77% in participation. \
                                                    Notable improvements: 13% in the belief that your job offers development opportunities, 12% in your \
                                                    manager communicates their expectations and, 10% in regularly receiving performance feedback."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Several areas we are focused on improving:"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    • The rationale behind business decisions is clear to me (50%) \
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    • Lumen makes it easy for me to deliver the desired customer experience (59%) \
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    • My job offers development opportunities (56%) \
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["We're Listening:"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    My leadership team and I continue our commitment to you as we head towards 2021, \
                                                    seeking to identify opportunities and take action to make further improvements in \
                                                    all areas."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    
                                                ],
                                                className="nine columns",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        style={"margin-bottom": "35px"},
                        className="row",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Happy Thanksgiving!"], className="subtitle"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["From Our Team"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        [
                                                            "If Lumen was a pie, then we are all the ingredients to making it Amazing!"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.Br([]),
                                                    html.Br([]),
                                                    html.P(
                                                        [
                                                            "Thanksgiving is a time to remember that “now is no time to think of what you do not have. Think of what you can do with what there is.” – Ernest Hemingway"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["'No Bake' Pumpkin Cheesecake"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "We've included a recipe from one of our team members below....."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Img(src='https://i.ibb.co/TBzt0Sm/Picture1.jpg')

                                                ],
                                                className="nine columns",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Ingredients"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_fund_facts)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Instructions"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_price_perf)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
