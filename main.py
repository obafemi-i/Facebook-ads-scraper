from requests_html import HTMLSession
import pandas as pd
import os
import sys

session = HTMLSession()

output = 'new_output.csv'

shop_domain_file = 'shop_domain.csv'           # File that contains the shop domains to be scraped
scraped_urls_file = 'scraped_urls.txt'         # File to store scraped URLs

domains = []

# Load previously scraped URLs from the file
def get_scraped_urls():
    try:
        with open(scraped_urls_file, 'r') as file:
            scraped_urls = set(file.read().splitlines())
    except FileNotFoundError:
        scraped_urls = set()

    return scraped_urls


# get individual domain URLs from csv file
df = pd.read_csv(shop_domain_file)
for index, row in df.iterrows():
    domains.append(row.values[0])


def export_to_csv(ads: list):
    file_exists = os.path.isfile(output)

    output_df = pd.DataFrame(ads)

    if not file_exists:
        output_df.to_csv(output, index=False)  
    else:
        output_df.to_csv(output, mode='a', header=False, index=False)



def main():
    for domain in domains:
        # Check if the URL has already been scraped, if it has been scraped it will be skipped
        if domain in get_scraped_urls():
            print(f"Skipping {domain} as it has already been scraped.")
            continue

        try:
            url = f"https://web.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q={domain}&search_type=keyword_unordered&media_type=all"


            r = session.get(url=url)
            # r = session.get(url=url, proxies=proxies)

            r.html.render(sleep=2, keep_page=True)
            page = r.html.find('div.xdbano7', first=True).text

            try:
                result = page.split(' ')[0].split('~')[1]
            except IndexError:
                result = 0
            
            ads_list = []
            ads_dict = {'Domain': domain, 'Number of Results': result}
            ads_list.append(ads_dict)

            export_to_csv(ads_list)

            # Add the scraped URL to the set of scraped URLs
            get_scraped_urls().add(domain)

            # Save the scraped URLs to the file
            with open(scraped_urls_file, 'a') as file:
                file.write(domain + '\n')

            
            print(f'{domain} succesfully scraped, moving on...')
        
        except Exception as e:
            print(f"Error scraping {domain}: {e}")
            sys.exit()

    print('All done!')

if __name__ == '__main__':
    main()

