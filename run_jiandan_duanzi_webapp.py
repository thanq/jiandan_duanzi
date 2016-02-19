
import os
from jiandan_web import app

if __name__ == '__main__':
    if os.environ.get('PRODUCTION') != "PRODUCTION":
        app.run()
    else:
        app.run('0.0.0.0', port=80)

