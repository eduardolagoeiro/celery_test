import os
from celery import Celery
from flask import Flask
from flask_celery import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = os.environ.get('CELERY_BROKER_URL')
app.config['CELERY_RESULT_BACKEND'] = os.environ.get('CELERY_RESULT_BACKEND')

celery = make_celery(app)

@app.route('/')
def hello_world():
  return 'hello world'

@app.route('/process/<string>')
def process(string):
  reverse.delay(string)
  return 'I sent an async request!'

@celery.task(name='celery_example.reverse')
def reverse(string):
  return string[::-1]

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)