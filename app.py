from flask import Flask, url_for, render_template

app = Flask(__name__)

# provide links to the various pages
@app.route("/")
def landingPage():
  return render_template('home.html')

'''
AUTH ROUTES
'''
# login page
@app.route('/login')
def login():
    return render_template('login.html')

# logout page
@app.route('/logout')
def logout():
    return render_template('logout.html')


'''
STUDENT ROUTES
'''

# to see the progress of each unit and overall test performance for a student, also provide links to their tests
# for student it will automatically load their details
@app.route('/student-dashboard')
def progress():
    return render_template('student-dashboard.html')

# to see the progress of a sub topic
@app.route('/student-topic-progress')
def topicProgress():
    return render_template('student-topic-progress.html')

# to see the progress of a sub topic
@app.route('/student-sub-topic-progress')
def subTopicProgress():
    return render_template('student-sub-topic-progress.html')

'''
JOINT ROUTES
'''

# will need to have the <testID> within the link
# for a student or admin to setup a test and input marks
@app.route('/test-view')
def createTest():
    return render_template('test-view.html')
'''
ADMIN ROUTES
'''

  




  
if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)