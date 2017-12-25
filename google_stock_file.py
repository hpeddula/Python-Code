import urllib.request

google_url="http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=8&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"
def download_url(url):
    response=urllib.request.urlopen(url)
    csv=response.read()
    
    csv_transform=str(csv)
    print(csv_transform)
    lines=csv_transform.split("\\n")
    dest_url = r'goog.csv'
    fw=open(dest_url,'w')
    for line in lines:
        fw.write("line\n")
    fw.close()

download_url(google_url)