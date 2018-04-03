#from flask import Flask, render_template, request, redirect, url_for
#import numpy as np
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def sample():
	count = redis.incr('hits')
	return ' I have been seen {} times.\n'.format(count)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)