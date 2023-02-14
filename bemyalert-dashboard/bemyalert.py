import textwrap
import requests
import re
import time
import webbrowser
from bs4 import BeautifulSoup
from googlesearch import search
from tabulate import tabulate

websites = {
    "News": ["www.yahoo.com", "www.msn.com", "www.bing.com"],
    "Major News Channels": ["www.bbc.com", "www.cnn.com", "www.reuters.com"],
    "Top National and International News Outlets": ["www.nbcnews.com", "www.indiatimes.com", "www.nytimes.com"],
    "Business News": ["www.cnbc.com"],
    "Social Media": ["www.twitter.com", "www.facebook.com", "www.instagram.com", "www.reddit.com"],
    "Professional Networking and Job Hunting": ["www.linkedin.com"],
    "Financial Resources": [ "www.finance.yahoo.com", "www.forbes.com", "www.businessinsider.com"],
    "Stock Market Information and Analytics": ["www.marketwatch.com", "www.moneycontrol.com"],
    "Indian Financial Resources": ["www.economictimes.indiatimes.com", "www.sebi.gov.in", "www.bseindia.com"],
    "Investment Advice and Research": ["www.investopedia.com"],
    "Market Research and Insights": ["www.statista.com", "www.icra.in", "www.crisil.com"],
    "Indian Investment and Finance Resources": ["www.motilaloswal.com", "trendlyne.com"],
    "General Knowledge": ["www.wikipedia.org", "www.pewresearch.org"],
    "Data ML & Sources": ["www.kaggle.com", "doaj.org"],
}

def search_news(query, headers, websites):
    results = []
    for header in headers:
        for website in websites[header]:
            for i in search(query + " site:" + website, tld="com", num=5, stop=5, pause=2):
                try:
                    page = requests.get(i)
                    soup = BeautifulSoup(page.content, "html.parser")
                    title = soup.find("title").text
                except:
                    title = i

                wrapped_text = f'<a href="{i}" target="_blank">{title}</a>'

                results.append([header, website, wrapped_text])
    return results


while True:
    query = input("Enter your query: ")
    header_keys = list(websites.keys())
    print("Select headers:")
    for i, header in enumerate(header_keys):
        print(f"{i + 1}. {header}")
    selected_header_keys = [header_keys[int(x) - 1] for x in input("Enter your choices (separated by comma): ").split(",")]
    search_results = search_news(query, selected_header_keys, websites)
    if search_results:
     file_name = query + '_' + str(time.time()) + '.html'
     with open(file_name, "w", encoding="utf-8") as file:
        file.write("<html>\n<head>\n<title>" + query + "</title>\n")
        file.write("<style>\nbody {\nbackground-color: rgb(33, 6, 6);\n}\n")
        file.write("table {\nbackground-color: rgba(234, 234, 234, 0.832);\n")
        file.write("border-collapse: separate;\nborder-spacing: 1px;\n")
        file.write("margin: auto;\ndisplay: table;\nborder-radius: 15px;\n")
        file.write("box-shadow: 2px 2px 2px 1px rgba(0,0,0,0.3);\n}\n")
        file.write("th, td {\nborder-bottom: 1px solid #CCC;\npadding: 8px;\n")
        file.write("text-align: left;\n}\n")
        file.write("h1 {\ntext-align: center;\ncolor: #FFFFFF;\n}\n")
        file.write("</style>\n</head>\n<body>\n")
        file.write("<h1>Bemyalert Dashboard</h1>\n")
        file.write("<table>\n<tr>\n<th>Header</th>\n<th>Website</th>\n<th>Result</th>\n</tr>\n")
        for result in search_results:
            file.write("<tr>\n")
            file.write("<td>" + result[0] + "</td>\n")
            file.write("<td>" + result[1] + "</td>\n")
            file.write("<td>" + result[2] + "</td>\n")
            file.write("</tr>\n")
        file.write("</table>\n</body>\n</html>")

        webbrowser.open(file_name)
        print(f"Results stored in file '{file_name}' and opened in a web browser.")
    else:
        print("Found None")
        
    user_input = input("Press 'Enter' to close or 'r' to re-run the program: ")
    if user_input == "":
        break