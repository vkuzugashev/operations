from flask import Flask, render_template
from models import Artist, Album, Song, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///operation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
def show_user(user_id):
    if request.method == 'POST':
        return 'POST'
    else:
        #return f'GET Это профиль пользователя ID {user_id}'
        return render_template('test.html')


@app.route('/songs')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)    

if __name__ == '__main__':
    app.run(debug=True)
