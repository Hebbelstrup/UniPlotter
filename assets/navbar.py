import dash_bootstrap_components as dbc

def create_navbar():

    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                children=[
                    dbc.DropdownMenuItem("home", href='/home'),
                    dbc.DropdownMenuItem('analystics', href='/analytics'),
                    dbc.DropdownMenuItem('CD', href='/cd'),
                    dbc.DropdownMenuItem('Files', href='/files')
                ],
            ),
        ],
        brand="UniPlotter", # set the left side text of navbar
        brand_href="/home",
        sticky="top",
        color='dark',
        dark=True,

        )
    return navbar