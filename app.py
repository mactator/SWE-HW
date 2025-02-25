from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Course Finder App')

@app.route('/api/health')
def health_check():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)