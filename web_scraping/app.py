from flask import Flask, render_template, url_for, request
from web_scraping.scraping import *

app = Flask(__name__)
df = pd.read_csv("%s/data/Job_search.csv" % main_path())

@app.route("/")
def main():
    return render_template('main.html')
@app.route("/", methods=['POST'])
def main_post():
    job_name = request.form['text']
    job_name = job_name.lower()
    df = pd.read_csv("%s/data/Job_search.csv" % main_path(), index_col=None)
    df['Job_Name'] = df['Job_Name'].str.lower()
    df = df[df['Job_Name'].str.contains(job_name)]
    return render_template('job_list.html',  tables=[df.to_html(classes='table table-striped table-hover', index=False)])


if __name__ == '__main__':
    app.run(debug=True)
