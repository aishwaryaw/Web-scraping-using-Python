import os
import requests
import datetime
from requests_html import HTML
import pandas as pd
import sys

abs_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(abs_path)

def url_to_text(url,file_year=None, save=False):

    r = requests.get(url)
    if r.status_code == 200:
         html_text = r.text
    
    if save:
        if file_year == None:
            today = datetime.datetime.now()
            file_year = today.year

        filename= os.path.join(BASE_DIR,f"html-text{file_year}.html")
        with open(filename, "w") as f:
            f.write(r.text)

    return html_text


def parse_and_extract(url, name="2020"):
    html_text = url_to_text(url=url)
    if html_text == None:
        return False

    r_html = HTML(html= html_text)
    r_table = r_html.find(".imdb-scroll-table")
    # print(r_table)
    #[<Element 'div' id='table' class=('a-section', 'imdb-scroll-table', 'mojo-gutter')>]

    if len(r_table) == 0:
        return False
    header_names = []
    table_data = []
    parsed_table = r_table[0]
    table_rows = parsed_table.find("tr")
    #print(table_row)
    header_row = table_rows[0]
    header_data = header_row.find("th")
    header_names = [x.text for x in header_data]
    
    for row in table_rows[1:]:
        cols = row.find("td")
        row_data = []
        #table_row_data = {}

        for i,col in enumerate(cols):
            header = header_names[i]
            row_data.append(col.text) # each row data forms a separate list

        table_data.append(row_data) # this is the list of all individual rows lists
    
    df = pd.DataFrame(table_data , columns= header_names)
    path = os.path.join(BASE_DIR,'data')
    os.makedirs(path, exist_ok=True)
    filename = os.path.join(path, f"{name}.csv")
    df.to_csv(filename,index=False)
    return True
    

def render(start_year=None, years_ago=0):

    if start_year == None:
        today = datetime.datetime.now()
        start_year = today.year

    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4 
    # if years_ago == 0:
    #     years_ago = 10
    url = f"https://www.boxofficemojo.com/year/world/{start_year}/"

    for year in range(0,years_ago+1):
        
    
        finished = parse_and_extract(url.format(year=start_year), name=start_year)
        if finished:
            print(f"{start_year} finished")

        else:
            print(f"{start_year} not finished")

        start_year= start_year-1


# if __name__ == "__main__":

#     try:
#         start = int(sys.argv[1])
#     except:
#         start = None
#     try:
#         count = int(sys.argv[2])
#     except:
#         count= 0
    
#     render(start_year=start, years_ago=count)
    

             

        
   












# if __name__ == "__main__":
#     url_to_text("https://www.boxofficemojo.com/year/world/2020/")

