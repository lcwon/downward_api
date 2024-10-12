<<<<<<< HEAD
=======
import os
>>>>>>> 67093ec (Save app.py)
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/')
def hello():
    return 'Hello Flask World'
    
if __name__ == '__main__':
    app.run()
    
=======
# 환경 변수에서 값 가져오기, 없으면 기본값을 사용
podname = os.environ.get('POD_NAME', 'Unknown Pod')
nodename = os.environ.get('NODE_NAME', 'Unknown Node')
namespace = os.environ.get('POD_NAMESPACE', 'Unknown Namespace')

@app.route("/")
def index():
    return f"Container EDU | POD Working : {podname} | nodename : {nodename} | namespace : {namespace}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

>>>>>>> 67093ec (Save app.py)
