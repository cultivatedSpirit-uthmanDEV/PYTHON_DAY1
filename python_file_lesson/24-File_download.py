from urllib import request

goog_url = 'https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv'

def download_worldbank_data(csv_url):
  response = request.urlopen(csv_url)
  csv = response.read()
  csv_str = str(csv)
  lines = csv_str.split("\\n")
  dest_url = r'goog.csv'
  fx = open(dest_url, "w")
  for line in lines:
      fx.write(lines + "\n")
  fx.close()


download_worldbank_data(goog_url)