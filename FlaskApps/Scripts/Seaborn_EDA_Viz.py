# Import Libraries
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

@app.route('/plot')
def plot():
    img = BytesIO()
    y = [1,2,3,4,5]
    x = [34,23,67,2,78]
    plt.plot(x,y)
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('plot.html', plot_url=plot_url)

@app.route('/stopServer', methods=['Get'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({"success": True, "message": "Server is shutting down..."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)