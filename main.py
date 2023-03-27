import webbrowser
import argparse
import yaml



try:
    with open('config.yaml') as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    print("missing config file")

urls = config['urls']

parser = argparse.ArgumentParser(prog='Web Search From CLI', usage='%(prog)s [query][options]')
parser.add_argument('query', nargs='+')
parser.add_argument('-e', '--engine', default='google', help="Specify search engine")
parser.add_argument('-b', '--browser', default='safari', help="Specify browser")
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0 by DonLeeFK')
args = parser.parse_args()


def query_url():
    query = ' '.join(args.query)
    if args.engine.lower() in urls.keys():
        url = urls[args.engine.lower()]
    else:
        print(f"{args.engine} not supported, revert back to Google")
        url = urls['google']
    q_url = url+query
    return q_url




if __name__ == "__main__":
    webbrowser.get(config['apps'][args.browser.lower()]).open(query_url())
