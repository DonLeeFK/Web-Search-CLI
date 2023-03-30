import webbrowser
import argparse
import yaml
import pathlib
import requests
from bs4 import BeautifulSoup


cur_path = pathlib.Path(__file__).parent.resolve()
try:
    with open(str(cur_path)+'/config.yaml') as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    print("missing config file")

urls = config['urls']

parser = argparse.ArgumentParser(prog='Web Search CLI', usage='%(prog)s [query][options]')
parser.add_argument('query', nargs='+')
parser.add_argument('-e', '--engine', default='google', help="specify search engine")
parser.add_argument('-b', '--browser', default='safari', help="specify browser")
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0 by DonLeeFK')
parser.add_argument('-n', '--number', default=20, help="max number of search results in console mode")
parser.add_argument('-c', '--console', action='store_true', help="display search results at terminal instead of opening browser")
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

def search_console():
    query = ' '.join(args.query)
    num = args.number
    engine = args.engine.lower()
    if engine in urls.keys():
        url = urls[engine]
    else:
        print(f"{args.engine} not supported, revert back to Google")
        url = urls['google']
        engine = 'google'
        
    q_url = f"{url}{query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    search_results = []
    if engine == 'google':
        num = args.number+5
        q_url += f"&num={num}"
        res = requests.get(q_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        for i, item in enumerate(soup.select(".tF2Cxc")):
            if i == args.number:
                #print("break")
                break
            link = item.select_one(".yuRUbf a")["href"]
            title = item.select_one(".yuRUbf a h3").text
            search_results.append((title, link))
    if engine == 'bing':
        num = args.number+5
        q_url += f"&count={num}"
        res = requests.get(q_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        #print(soup)
        print(soup.select(".b_algo"))
        for i, item in enumerate(soup.select(".b_algo")):
            if i == args.number:
                break
            link = item.select_one("a")["href"]
            title = item.select_one("h2")
            search_results.append((title, link))
    if engine == 'duckduckgo':#fyi duckduckgo do not support num of results
        q_url = f"https://duckduckgo.com/html/?q={query}&kl=us-en"
        res = requests.get(q_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        for i, item in enumerate(soup.select(".result__title")):
            if i == args.number:
                break
            link = item.select_one("a")["href"]
            title = item.select_one("a").text
            search_results.append((title, link))
    
    if engine == 'baidu':
        num = args.number+5
        q_url = f"https://www.baidu.com/s?wd={query}&rn={num}"
        res = requests.get(q_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        #print(q_url)
        for item in soup.select(".t a"):
            link = item.select_one["href"]
            title = item.text
            search_results.append((title, link))
        

    return search_results




if __name__ == "__main__":
    if args.console:
        search_results = search_console()
        for i, result in enumerate(search_results):
            print(f"{i+1}. {result[0]} :  {result[1]}")
    else:
        webbrowser.get(config['apps'][args.browser.lower()]).open(query_url())
