from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

connection_string = 'mongodb+srv://febrii:febrii0@cluster0.ms3cgyr.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(connection_string)
db = client.dbfebrii

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    # sample_receive = request.args.get('sample_give')
    # print(sample_receive)
    articles = list(db.diary.find({}, {'_id': False}))
    return jsonify({'articles': articles})

@app.route('/diary', methods=['POST'])
def save_diary():
    # sample_receive = request.form.get('sample_give')
    # print(sample_receive)
    title_reveive = request.form.get('title_give')
    content_receive = request.form.get('content_give')
    
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    file = request.files['file_give']
    extention = file.filename.split('.')[-1]
    filename = f'static/post-{mytime}.{extention}'
    file.save(filename)

    profile = request.files['profile_give']
    extention = profile.filename.split('.')[-1]
    profilename = f'static/profile-{mytime}.{extention}'
    profile.save(profilename)

    doc = {
        'file': filename,
        'profile': profilename,
        'title': title_reveive,
        'content': content_receive
    }
    db.diary.insert_one(doc)
    return jsonify({'message': 'data was saved!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)