from src.app import app

__author__ = 'andres'

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])

