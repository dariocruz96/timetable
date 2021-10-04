from flask import Flask, render_template

app = Flask('FullCalendar Demo')

events = [
    {
        'todo': 'Tutorial for Boris',
        'date': '2021-10-05',
    },
    {
        'todo': "Eat Hotpot",
        'date': '2021-10-05',
    }
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calendar')
def calendar():
    return render_template('/calendar.html',
                           events=events)
