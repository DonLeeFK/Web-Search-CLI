# Web Search CLI
This is a simple web search cli to allow you to have a more seamless experience of google oriented programming by launching search engine directly from you command line. 
## How to use
Simply download the code, modify `config.yaml` (if needed, skip if you are using mac) with path of your browser. Then alias `main.py` in your `.bashrc` or `zshrc` file. 
```
alias websearch="$PATH$/websearch-cli/main.py"
```
## Example
```
-h, --help            show this help message and exit
  -e ENGINE, --engine ENGINE
                        specify search engine
  -b BROWSER, --browser BROWSER
                        specify browser
  -v, --version         show program's version number and exit
  -n NUMBER, --number NUMBER
                        max number of search results in console mode
  -c, --console         display search results at terminal instead of opening
                        browser
  ```

You can either open a new browser tap or output the top n results to terminal.

  ```
  websearch 時代革命 -c       
1. 時代革命(紀錄片) - 维基百科，自由的百科全书 :  https://zh.wikipedia.org/wiki/%E6%99%82%E4%BB%A3%E9%9D%A9%E5%91%BD_(%E7%B4%80%E9%8C%84%E7%89%87)
2. 时代革命(纪录片) - 维基百科，自由的百科全书 :  https://zh.wikipedia.org/zh-cn/%E6%99%82%E4%BB%A3%E9%9D%A9%E5%91%BD_(%E7%B4%80%E9%8C%84%E7%89%87)
3. 映画『時代革命』公式サイト :  https://jidaikakumei.com/
4. 時代革命- 電影線上看 - friDay影音 :  https://video.friday.tw/movie/detail/88892
5. Revolution of Our Times 時代革命 - Facebook :  https://www.facebook.com/RevolutionofOurTimes/
6. 時代革命台灣專頁 - Facebook :  https://www.facebook.com/RevolutionofOurTimesTW/
7. 時代革命Revolution of Our Times - Yahoo奇摩電影戲劇 :  https://movies.yahoo.com.tw/movieinfo_main.html/id=12424
8. 作者-《時代革命》團隊 - 博客來網路書店 :  https://search.books.com.tw/search/query/key/%E3%80%8A%E6%99%82%E4%BB%A3%E9%9D%A9%E5%91%BD%E3%80%8B%E5%9C%98%E9%9A%8A/adv_author/1/
9. 時代革命台灣專頁(@root_twig) • Instagram photos and videos :  https://www.instagram.com/root_twig/
  ```