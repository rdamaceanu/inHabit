from flask import Flask, render_template

inHabit = Flask(__name__)

# Define routes
@inHabit.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    inHabit.run(debug=True)