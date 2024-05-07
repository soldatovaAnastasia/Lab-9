#Солдатова Анастасия Вариант №5
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Создание экземпляра Flask приложения
app = Flask('Feedback of customers')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Таблица отзывов
class Comments(db.Model):
    rate = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))

    def __repr__(self):
        return f'Comment: {self.text}, rate for {self.rate} stars.'

@app.route('/')
def main():
    comments = Comments.query.all()
    return render_template('index.html', comment_list=comments)


@app.route('/send', methods=['POST'])
def add_comment():
    data = request.json
    comment = Comments(**data)
    db.session.add(comment)
    db.session.commit()

    return 'OK'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)