from googlesearch import search
from tabulate import tabulate

websites = {
    "News": ["www.yahoo.com", "www.bbc.com", "www.cnn.com", "www.reuters.com", "www.nbcnews.com", "www.indiatimes.com", "www.msn.com", "www.nytimes.com", "www.cnbc.com", "www.india.com", "timesofindia.indiatimes.com", "www.theguardian.com" ],
    "Social Media": ["www.twitter.com", "www.facebook.com", "www.instagram.com", "www.linkedin.com", "www.reddit.com", "www.pinterest.com"],
    "Finance": [ "www.finance.yahoo.com", "www.forbes.com", "www.businessinsider.com", "www.screener.in"],
    "Stock Market": ["www.nasdaq.com", "www.nyse.com", "www.marketwatch.com", "www.economictimes.indiatimes.com", "www.sebi.gov.in", "www.bseindia.com", "www.nseindia.com", "www.bloomberg.com", "in.tradingview.com", "www.investing.com"],
    "Research Reports": ["www.wikipedia.org", "www.investopedia.com", "doaj.org", "www.statista.com", "www.kaggle.com", "www.pewresearch.org", "www.icra.in", "www.crisil.com", "www.motilaloswal.com", "trendlyne.com", "www.mckinsey.com", "www.bain.com", "www.ibef.org", "www.ey.com", "kpmg.com"],
}

def search_news(query, headers, websites):
    results = []
    for header in headers:
        for website in websites[header]:
            for i in search(query + " site:" + website, tld="com", num=5, stop=5, pause=2):
                results.append([header, website, i])
    return results

while True:
    query = input("Enter your query: ")
    header_keys = list(websites.keys())
    print("Select headers:")
    for i, header in enumerate(header_keys):
        print(f"{i + 1}. {header}")
    selected_header_keys = [header_keys[int(x) - 1] for x in input("Enter your choices (separated by comma): ").split(',')]
    search_results = search_news(query, selected_header_keys, websites)
    if search_results:
        print("Results:")
        print(tabulate(search_results, headers=['Header', 'Website', 'Result']))
    else:
        print("Found None")
        

rerun = input("Press 'Enter' to close or 'r' to re-run the program: ")
if rerun.lower() == 'r':
    search_news(query, selected_header_keys, websites)
