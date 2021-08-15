from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    doc = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive,
    }

    db.bookreview.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '저장 완료'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.bookreview.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'all_reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)