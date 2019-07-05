from flask import Flask, render_template, url_for, request
from web_scraping import *

app = Flask(__name__)
df = pd.read_csv("%s/data/Job_search.csv" % main_path())

@app.route("/")
def main():
    return render_template('main.html')
@app.route("/", methods=['POST'])
def main_post():
    job_name = request.form['text']
    df = pd.read_csv("%s/data/Job_search.csv" % main_path(), index_col= None)
    df = df[df['Job_Name'].str.contains(job_name)]
    return render_template('job_list.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
@app.route("/job", methods=('POST','GET'))
def data():
    return render_template('job_list.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
