__author__ = 'student'
from flask import  Flask
from  flask import  render_template

app = Flask(__name__)

count = 0
@app.route('/<string:Name>',methods=['GET'])
def index(Name):

    global count
    count += 1
    return render_template('index.html',ame=Name, cnt=count)

if __name__=='__main__':
    app.run(port= 8076,debug= True)
