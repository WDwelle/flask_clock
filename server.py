from flask import Flask, render_template, session
from datetime import datetime, date

app = Flask(__name__)
app.secret_key="noooo anakin"

@app.route('/')
def time():
    today = date.today()
    now = datetime.now().time()
    current_datetime = datetime.now()

    session['today'] = str(today.strftime('%m-%d-%Y'))
    session['now'] = str(now)
    session['current_datetime'] = str(current_datetime)

    print(today.strftime('%m-%d-%Y'))
    print(now)

    return render_template('index.html',today = session['today'], now = session['now'] )


if __name__=="__main__":
    app.run(debug=True)