# Web Search CLI
This is a simple web search cli to allow you to have a more seamless experience of google oriented programming by launching search engine directly from you command line. 
## How to use
Simply download the code, modify `config.yaml` (if needed, skip if you are using mac) with path of your browser. Then alias `main.py` in your `.bashrc` or `.zshrc` file. 
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

```
                                                                             __                                                ______                                          _____                    
                        ____                                               __  \_    ______                                 ___     |\                                        _    |\_                  
                       _    \__                                     ____   _    |\__      |\_                            __           \                       __       ____   |\     |                  
                       |\      \_   ____                          __   |\__|            __                           ___           ___|                    __   \     _   |\   |     |\                 
                        |\      | __                             __                __                            ___            __                        _     |\    |    |\__|      |                 
                   ___   |\       _     _|                      __      ___    __   |   ___                            ___     _  \______                 |\    _    _|             __|                 
                  _  |\___       _     _                       __     __  |\       _|      \                             |     |\__     |                  |\___|   _              _                    
                 _|       \    | |     |\___                  __      _    |\   _          |                  ___________|              |                                     |    |\   __              
                 _        |    |_|\         \__              __     _ |\    |\   \         |                _                           |\               ____       ____    |_|      \  _               
                 |\__    _|                                _      _    |\  __    | |      _                 |                   __        \___         _     \_   __   |               _                
          _____         _             _____                     __      |  _     | |       \                |\_   _            _ |            \_      _      _   __ \__|    ___      __                 
         _    |\____                      |  |              ___    _    |\       |_|    __ |                  |\  |     _      |_|             |\     |\    _   __          _ |        \__              
         |\_          __               __  \ |\                  _     __           \_    _|                     _|    _                ____    |\     |\__    __          _|_|           \___          
           |\       __ |      __       _   |_ |\              __      _             _ \   _             ____  _        |\_  ____       _    \__ _|           __   _  |             ___        \         
            |\     _  _|    _  |      _|    |  |\      ______         |    ___      |_|   |\           _   |__     ___     _ _ | |     |       _       _____       \_    ___       _ |\       |         
             |\___  \_     _| _|    __      |   |\    _               |    _               |           |\        __  |           |     |              _                _   |       |   \______          
                  \__     __  _     _      _|    |    |\__            |    |\_   _ \       |\___        |\      __  _|     ______|    _               |               _   _|   ____|                    
                 __     __    |     |  _____     |\       \____       |\___    __  |            \___     |\   __    _     _      |    |               |\        __  __       _                          
         _______       __     |      _            |                           _   _    ____         \__   |\__      |\    |\    _|    |                |\    __   _             _______                 
        _            __       |\                  |              |           _   _   __   |\                         |\               |                  \___          |\             |\                
         \_         __         |\_               _|              |\_   ______        _     |\__________               |\   _______    |                                  \_     _______                 
          |\___    __             \______________                   \__     |\_     _|                                  \_       |\___|                                   |\___                         
               \__                                                             \___                                                                                                                     
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                ____                                   ___                              
                                 ____                                                                                          _    \____                             _   \__                           
                                _    \_                                                                                         \       |\                            |      \_                         
                                |     |\                                _____                                     _ \_____      |\        \_                          |       |                         
                                |      |                                     \__      ______                      |      |\_____            \_                       _|                                 
                 _____           \     |\                               __      \     _     \_                    |                    ____                         __         __                       
             ___      \_         |       \____                           |       \   _|\     |\_            ______                  \_     \__                    __     ____    \__                    
            _      _   |\  ______|           |                           |\      |      \___   |                         | |       __                            __    _            \_                  
           _|    _      |_            __     |\_                    ___   |\     |\         \__|            __     ____   _|   ___  |\                          __        ___  \      \__               
            |     \_     |  _        _   |\_    \_                __   \_  |      |\__   _                   |\___    |\__    _ _    |\_                      __        _      |\__      \____          
            |            | _    |     \_    \__ _                __     |   \                                        __   \   |_|       \_                   __            ___    |\_         \_____    
           _               |\_      __    _ _                   __     _   _|            _____                     __    _|\                               __       ______      __  |              |    
           |      __            ___  |  _   |\___              __    _    _           __                         __        |             _               ___     _        \___    \_|          ____|    
          _     _  |     __   _     _|\ |\      |\           __       \__           __         __               __     |   |      _______              __           ______      _      _ \____          
          |     |\_|    _ |   |\__            __            __       _              _         _ |\              _      |\__|     _  _   |\_____    ____          __      |\_   _ \    _                 
                        | |       \____     _             __                ___     |\        |  |               \____  _  |     |\_|\        |                    \     _ |   |_|   _                  
         __             | |       _    \   _            _                __   |\     |\       |  |\                  | _|\_|                   \   _________       |    _| |          \                 
        _         __    | |\____  |\   |   |                   __      _       |\     |\      |   |\       __________              ___________              \    |_    __ _          _|                 
       _|      __  |\_  |      |    _| |   |          \___   __ |     _         |\     |\_    |    |      _             __       _            \_            |\_       __  |     ______                  
        |\____        \_       |\___   |   |              \_   _      |          |\      |\   |    |      |\       ____   \     _                             |\_____     |    _                        
                                      _    |                   |\_    |           |\       \__|     \      |\_____         \    |                                         |    |                        
                              ___     |    |                     |\  _             |\_             _                       |     \                                        |    |                        
                           |     \____|    |                      |\_|                \_           |                      _      |                                        |    |                        
                            \__             \                                           \___      _|                      |      |                                        |    |                        
                               \__         _                                                \____                         |\     |                                        |   _|                        
                                  \________                                                                                |\_  _|                                        |\  _                         
                                                                                                                              \__                                          |\_|                         
                                                                                                                                                                                                        
                                                                                                                                                                                                                        
```