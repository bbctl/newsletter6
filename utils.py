import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("lumen_logo_dark.jpg"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("InsideLink", id="learn-more-button"),
                        href="https://centurylink.sharepoint.com",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Newsletter")],
                        className="seven columns main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "U.S. 2021 Holiday Calendar",
                href="https://centurylinkenterprise.us.newsweaver.com/centurylinkhumanresources.16yj0vo8jm/x4hs10nc4zthrtishrij6e/external?email=true&a=6&p=4405827&t=680337",
                className="tab first",
            ),
            dcc.Link(
                "COVID-19 Resources",
                href="https://centurylinkenterprise.us.newsweaver.com/centurylinkhumanresources.2f5cdlil3r/j2fewl5v158hrtishrij6e/external?email=true&a=5&p=4318228&t=1402038",
                className="tab",
            ),
            dcc.Link(
                "Internal Jobs",
                href="https://internaljobs.centurylink.com/?locale=en_US",
                className="tab",
            ),
            dcc.Link(
                "Flu Shot Program",
                href="https://centurylink.sharepoint.com/sites/ILHR/SitePages/Wellness-US-Prevention.aspx#flu-shot-program",
                className="tab",
            ),
            dcc.Link(
                "HealthVUE App",
                href="https://centurylink.sharepoint.com/SitePages/HealthVUE-Launch.aspx",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
