
import os
from jiandan_web import app

if __name__ == '__main__':
    if os.environ.get('PRODUCTION') != "PRODUCTION":
        app.run('0.0.0.0')
    else:
        app.run('0.0.0.0')

