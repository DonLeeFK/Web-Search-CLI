# Web Search CLI
This is a simple web search cli to allow you to have a more seamless experience of google oriented programming, 
## How to use
Simply download the code, modify `config.yaml` (if needed, skip if you are using mac) with path of your browser. Then alias `main.py` in your `.bashrc` or `zshrc` file. 
```
alias websearch="$PATH$/websearch-cli/main.py"
```
## Example
```
usage: Web Search CLI [query][options]

positional arguments:
  query

optional arguments:
  -h, --help            show this help message and exit
  -e ENGINE, --engine ENGINE
                        Specify search engine
  -b BROWSER, --browser BROWSER
                        Specify browser
  -v, --version         show program's version number and exit
  ```