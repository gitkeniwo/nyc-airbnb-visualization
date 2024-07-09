from app import app

import argparse

dash_app = app
server = dash_app.server


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Initialize the Dash app')
    parser.add_argument('--port', '-p',
                        help='Port number for the Dash app',
                        default=8050,)
    parser.add_argument('--host', '-H',
                        help='Host for the Dash app',
                        default='0.0.0.0')
    parser.add_argument('--no-debug', '-n',
                        help='Debug mode for the Dash app',
                        action='store_false',)  # store_false sets it to be True by default

    args = parser.parse_args()

    # port = random.randint(7000, 8000)
    port = args.port
    dash_app.run_server(host=args.host, debug=args.no_debug, port=port)