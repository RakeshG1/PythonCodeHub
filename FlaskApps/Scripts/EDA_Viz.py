# Import Libraries
import pandas as pd
import os
import base64
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 
from io import BytesIO
from flask import Flask, render_template, jsonify

# Flask API
app = Flask(__name__)

@app.route('/')
def Hello_World():
    return 'Hello World'

@app.route("/welcome_page")
def index():
    # You can pass data to the template here (optional)
    data = {"message": "Hello from Flask!"}
    return render_template("index.html", data=data)  # Pass data as a dictionary


@app.route('/plot_seaborn')
def plot_static():
    img = BytesIO()
    x = [1,2,3,4,5]
    y = [34,23,67,2,78]
    df = pd.DataFrame({"x":x, "y":y})
    #plt.plot(x,y)
    sns.lineplot(x=x, y=y, data=df, marker='o')
    plt.xlabel('X-Label')
    plt.ylabel('Y-Label')
    plt.title('Sample Scatter Plot')
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('plot[seaborn].html', plot_url=plot_url)

@app.route('/plot_d3js')
def plot_dynamic():
    # data = [
    #   { "x": 1, "y": 34 },
    #   { "x": 2, "y": 23 },
    #   { "x": 3, "y": 67 },
    #   { "x": 4, "y": 2 },
    #   { "x": 5, "y": 78 }
    # ]
    # return render_template('plot[d3js].html', chart_data=data)
    return render_template('plot[d3js].html')

@app.route('/stopServer', methods=['Get'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({"success": True, "message": "Server is shutting down..."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)