import argparse
from dash import Dash

from pages.layout import create_app_layout


def arg_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(description='Initialize the Dash app')

    parser.add_argument('--port', '-p',
                        help='Port number for the Dash app',
                        default=8050, )
    parser.add_argument('--host', '-H',
                        help='Host for the Dash app',
                        default='0.0.0.0')
    parser.add_argument('--no-debug', '-n',
                        help='Debug mode for the Dash app',
                        action='store_false', )  # store_false sets it to be True by default

    return parser


def main():

    args = arg_parser().parse_args()

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = create_app_layout()

    # port = random.randint(7000, 8000)
    port = args.port
    app.run_server(host=args.host, debug=args.no_debug, port=port)


if __name__ == '__main__':
    main()
