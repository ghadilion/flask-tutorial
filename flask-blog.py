from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Kiran Srinivasan',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '01 January 2023'
    },
    {
        'author': 'ABC',
        'title': 'Blog post 1',
        'content': 'Second post content',
        'date_posted': '02 January 2023'
    }
]

@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)