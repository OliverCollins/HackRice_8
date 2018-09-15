from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def main():
	url = "https://www.lowincomehousing.us/nbhd/tx-houston-downtown"
	html = urlopen(url)

	soup = BeautifulSoup(html, 'xml')

	name = soup.find('div', attrs={'class': 'small-posts'})
	name_text = name.text

	return render_template('index.html', **locals())

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
