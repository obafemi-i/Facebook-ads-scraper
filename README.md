### Facebook Ads Scraper

Install dependencies before running the sccript, to install dependecies run the command below in the terminal
`pip install -r requirements.txt`


The scraped results are saved in a "output.csv" file. If you wish to change the name of the file, go to line number 7, the output variable in the main.py file and change the value. Like this;
        output = 'output.csv' ,    change to,    output = 'anything-you-want.csv'


The shop_domain_file variable's value in the main.py is the name of the file that contains the shop domains to be scraped, change the value accordingly.


When the main.py script is run for the first time, a "scraped_urls.txt" file is created. This file saves the scraped domains. 
If the script needs to be stopped and restarted, the already scraped domains will not be scraped again.


To start the script, in the terminal run  `python main.py`

Happy scraping!