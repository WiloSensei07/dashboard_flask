from flask import Flask, render_template
from plot import df, get_scatter_plot, get_bar_plot, get_spider_plot

# launch a new flask instance
app = Flask(__name__)


@app.route('/')
def world():
    return "<h1>Hello world!</h1>" \
           "<li><a href='/bonjour'> Welcome.</a></li>" \
           "<li><a href='/index'> Index site.</a></li>" \
           "<li><a href='/hi/<name>'> Wilo.</a></li>" \
           "<li><a href='/dataframe'> Dataframe.</a></li>" \
           "<li><a href='/dashboard'> Dashboard.</a></li>"


@app.route('/bonjour')
def bonjour():
    return "<h1>Bonjour tout le monde!</h1>" \
           "<a href='/'> Retour.</a>"


@app.route('/hi/<name>')
def hi(name):
    return f"<h1>Hi {name} ! </h1>" \
           "<a href='/'> Retour.</a>"


@app.route('/dataframe')
def get_data_frame_html():
    return render_template("dataframe.html", table = df.head(100).to_html(col_space=50, justify="center"))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashborad_html():
    fig_scatter = get_scatter_plot()
    fig_bar = get_bar_plot()
    fig_spider = get_spider_plot(df)
    return render_template("dashboard.html", fig_scatter = fig_scatter, fig_bar = fig_bar, fig_spider = fig_spider)

if __name__ == "__main__":
    app.run(debug=False)