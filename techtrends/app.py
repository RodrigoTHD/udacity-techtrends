import sqlite3

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
from logging.config import dictConfig

# logging configuration
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(levelname)s [%(asctime)s] %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

# Function to get a database connection.
# This function connects to database with the name `database.db`
db_connection_count = 0
def get_db_connection():    
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row    
    global db_connection_count
    db_connection_count = db_connection_count + 1
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()    
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()    
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):    
    post = get_post(post_id)
    if post is None:      
      app.logger.info('A non-existing article was accessed. post_id: "%s"', post_id)      
      return render_template('404.html'), 404
    else:
      app.logger.info('Article "%s" retrieved!', post['title'])      
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    app.logger.info('The "About Us" page is retrieved!')      
    return render_template('about.html')

# Define the post creation functionality
post_count = 0
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            global post_count
            post_count = post_count + 1

            app.logger.info('A new article was created. Title "%s"', title)
            return redirect(url_for('index'))

    return render_template('create.html')

# Define the healthz check endpoint
@app.route('/healthz')
def healthz():
    resp = jsonify({ "result": "OK - healthy" })
    resp.status_code = 200
    return resp

# Define the metrics endpoint
@app.route('/metrics')
def metrics():
    resp = jsonify({ "db_connection_count": db_connection_count, "post_count": post_count })
    resp.status_code = 200
    return resp    

# start the application on port 3111
if __name__ == "__main__":
   app.run(host='0.0.0.0', port='3111')
