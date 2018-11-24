from flask import Flask
import os
app = Flask(__name__, static_url_path='')

@app.route("/")
def root():
    return app.send_static_file('./webpage.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)