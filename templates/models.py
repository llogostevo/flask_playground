from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(255), unique=True, nullable=False)
    lastname = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin', 'student', 'teacher'), nullable=False)

class Teacher(db.Model):
    __tablename__ = 'teacher'
    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(255), nullable=False)
    course_board = db.Column(db.String(255), nullable=False)
    course_level = db.Column(db.String(255), nullable=False)

class Unit(db.Model):
    __tablename__ = 'unit'
    unit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unit_number = db.Column(db.String(255), nullable=False)
    unit_name = db.Column(db.String(255), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))

class Topic(db.Model):
    __tablename__ = 'topic'
    topic_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    topic_name = db.Column(db.String(255), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.unit_id'))

class Subtopic(db.Model):
    __tablename__ = 'subtopic'
    subtopic_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subtopic_name = db.Column(db.String(255), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.topic_id'))

class Completion(db.Model):
    __tablename__ = 'completion'
    completion_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    subtopic_id = db.Column(db.Integer, db.ForeignKey('subtopic.subtopic_id'))
    completion_status = db.Column(db.String(20), nullable=False)
    last_studied = db.Column(db.Date)

class Assessment(db.Model):
    __tablename__ = 'assessment'
    assessment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assessment_type = db.Column(db.String(20))
    assessment_name = db.Column(db.String(20))

class AssessmentPaper(db.Model):
    __tablename__ = 'assessment_paper'
    paper_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paper_name = db.Column(db.String(20))
    paper_date = db.Column(db.Date)
    subtopic_id = db.Column(db.Integer, db.ForeignKey('subtopic.subtopic_id'))
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment.assessment_id'))

class PaperQuestion(db.Model):
    paper_question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('assessment_paper.paper_id'))
    question_number = db.Column(db.String(20))
    subtopic_id = db.Column(db.Integer, db.ForeignKey('subtopic.subtopic_id'))
    max_mark = db.Column(db.Integer)

class QuestionAttempt(db.Model):
    __tablename__ = 'question_attempt'
    question_attempt_id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer)
    include_in_results = db.Column(db.Boolean)
    assessor_type = db.Column(db.String(20))
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))

class Teaching(db.Model):
    __tablename__ = 'teaching'
    teaching_id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'), nullable=False)
    subtopic_id = db.Column(db.Integer, db.ForeignKey('subtopic.subtopic_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    dateTaught = db.Column(db.Date)

class Class(db.Model):
    __tablename__ = 'class'
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(255), nullable=False)
    course_completion_date = db.Column(db.Date)

class Enrolment(db.Model):
    __tablename__ = 'enrolment'
    enrolment_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.class_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)

