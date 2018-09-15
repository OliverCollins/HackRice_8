# Imports for flask and beautiful soup
from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)

# Base route
@app.route("/")
def main():

	# Grab the website and open it as html
	url = "https://www.lowincomehousing.us/nbhd/tx-houston-downtown"
	html = urlopen(url)

	# Load content from website
	soup = BeautifulSoup(html, 'html.parser')

	# Look specifically for available homes
	name = soup.find('div', attrs={'class': 'small-posts'})
	page_html = name.text.split()

	house_pic, phone_number, postal_code = [], [], []

	# Grab the urls for the pictures of available houses
	for x in range(len(page_html)):

		# Grab pictures of available housing
		if page_html[x][-8:] == '"photo":':

			# Just grab the URL for picture of house
			house_pic.append(page_html[x+1][1:-16])

		if page_html[x][9:18] == 'telephone':

			# Grab the phone numbers
			phone_number.append(page_html[x+1][0:8])

		# Second way they print telephone numbers
		elif page_html[x][-17:-8] == 'telephone':

			# Grab the phone numbers
			phone_number.append(page_html[x+1][0:8])

		if page_html[x][-12:-2] == 'postalCode':

			# Grab the postal code
			postal_code.append(page_html[x+1][1:6])

	# Render html file and pass in contents from scrapped website
	return render_template('index.html', **locals())

# Run server
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
