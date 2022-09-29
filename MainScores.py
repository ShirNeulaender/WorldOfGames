from flask import Flask, render_template
from Utils import BAD_RETURN_CODE
from Utils import SCORES_FILE_NAME

app = Flask(__name__, template_folder='templates')

if BAD_RETURN_CODE == -1:
    @app.route("/")
    def score_server():
        score_file = open(SCORES_FILE_NAME, "r")
        try:
            sum_score = int(score_file.read())
        except ValueError:
            sum_score = 0
        return render_template('scores_html.html', SCORE=sum_score)

else:
    @app.route("/")
    def score_server():
        return render_template("error_html.html", ERROR="Problem showing the result")

