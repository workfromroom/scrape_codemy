import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape')
def scrape_codemy():
    html_doc = requests.get("https://codemy.com/")
    soup = BeautifulSoup(html_doc.text,"html.parser")
    images = soup.findAll(attrs={"class":"info-content"})
    return render_template('index.html',images=images)

if __name__ == '__main__':
    app.run(debug=True)