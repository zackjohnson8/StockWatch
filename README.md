<a name="readme-top"></a>
## About The Project
StockWatch is a web scraping analyzer which trades stocks based on public sentiment, or I hope it will be soon. The 
technology being used is docker to run a database container, PostgreSQL database to store data, TDAmeritrade API to 
handle automated trading, and Flask to run the web server (Will probably remove in the future as this 
application becomes more personal single use. Previously it was being built as a back-end to a front-end application, 
that is no longer the case).

## Getting Started
### Configuration
Modify the configuration files listed below. The information changed in these files should not be commited and are 
sensitive. Note: until a better solution is implemented, follow this links implementation of --assume-unchanged 
https://stackoverflow.com/questions/18276951/how-do-i-stop-git-from-tracking-any-changes-to-a-file-from-this-commit-forward
* ```./src/stock_watch/startup_config.yml``` - This file contains the configuration for TDAmeritrade API
* ```./src/stock_watch/data_scraper/configs/praw.ini``` - This file contains the configuration for Reddit API

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any 
contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also 
simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

    Fork the Project
    Create your Feature Branch (git checkout -b [name_of_your_new_branch])
    Commit your Changes (git commit -m 'Add some awesome feature')
    Push to the Branch (git push origin [name_of_your_new_branch])
    Open a Pull Request

## License
Distributed under the MIT License. See the `LICENSE` file for more information.

## Contact
Zachary Johnson - @zackjohnson8 - zackjohnson8@gmail.com
