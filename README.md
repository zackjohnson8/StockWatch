<a name="readme-top"></a>
## About The Project
Using the TDAmeritrade API, this program affords the capability to retrieve data from the stock market. It stores 
data in a dockerized PostgreSQL. For communication with the front-end, the Flask microframework is used.  As of now, 
this program does not contain its own GUI to display the information, it is meant to be used with a separate front-end.

## Getting Started
To run this program, you will need to have a TDAmeritrade developer account with a refresh token, client ID, and 
redirect URI. Use the <a href='https://developer.tdameritrade.com/content/getting-started'>TDAmeritrade Getting Started</a> to get this information</br>

Update the startup_config.yml file with your TDAmeritrade information. The program will not run without this 
information.

## Roadmap
- [x] Add TDAmeritrade API
- [x] Add Docker PostgreSQL container
- [x] Add logic to store data in PostgreSQL database
- [x] Add a flask service
- [ ] Add the logic for communicating with outside sources

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
