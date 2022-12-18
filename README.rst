.. image:: https://codecov.io/gh/zackjohnson8/StockWatch/branch/master/graph/badge.svg?token=ZAOUINTOA8
 :target: https://codecov.io/gh/zackjohnson8/StockWatch

=================
About The Project
=================

**StockWatch** is a web scraping analyzer which trades stocks based on public sentiment, or I hope it will be soon.

**Storage**: A local docker PostgreSQL database. By dockerizing the database, it is easy to spin up
a new instance for testing purposes, and it is easy to scale the database to handle more storage.

**Stock Broker**: Currently TDAmeritrade's API is being used as a placeholder until further development is planned.
I chose to use this API because it's what I use for my own personal trading. That being said, finding a more robust API
and solution is a priority for the future. Having a way of trading with real money and simulated money is a priority for
future testing.

**Data Scraping**: Using website API if available, otherwise using 'some future web scraping library' to scrape the
data from the website. These should be easy to add and remove in instances of website/API changes.

**Message Bus**: Is used to handle the data flow between the various components of the application. This allows for
easy scaling, and testing of the application.

**Analyzer**: (Future plans) A way of analyzing the and making decisions based on the data retrieved from scrapers.

Minimum viable product will be a data scraping from as many sources as possible. Functional manual trading capabilities
for both real and simulated money.

===============
Getting Started
===============

Configuration
=============

Modify the configuration files listed below. The information changed in these files should not be commited and are 
sensitive. Note: until a better solution is implemented, follow this `solution`_ of --assume-unchanged

.. _solution: https://stackoverflow.com/questions/18276951/how-do-i-stop-git-from-tracking-any-changes-to-a-file-from-this-commit-forward

    * ./src/stock_watch/startup_config.yml - This file contains the configuration for TDAmeritrade API
    * ./src/stock_watch/data_scraper/configs/praw.ini - This file contains the configuration for Reddit API

(Not sure how to get the TDAmeritrade API and Reddit API values? Follow the links below)
    * https://developer.tdameritrade.com/content/getting-started
    * https://github.com/reddit-archive/reddit/wiki/API

Running
=======
Fork and clone your project to a local directory of your choosing.

Setup your virtual environment
------------------------------

Open the newly cloned /StockWatch directory in your terminal and run the following commands::

    $ python3 -m venv venv
    $ source venv/bin/activate


Install dependencies
--------------------

Download the dependecies from the requirements.txt file::

    $ pip install -r requirements.txt


Run the application
-------------------

To run the application, run the following command::

    $ python3 -m src.stock_watch


============
Contributing
============
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any 
contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also 
simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!::

    Fork the Project
    Create your Feature Branch (git checkout -b [name_of_your_new_branch])
    Commit your Changes (git commit -m 'Add some awesome feature')
    Push to the Branch (git push origin [name_of_your_new_branch])
    Open a Pull Request

=======
License
=======
Distributed under the MIT License. See the `LICENSE` file for more information.

=======
Contact
=======
Zachary Johnson - @zackjohnson8 - zackjohnson8@gmail.com
