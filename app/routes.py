
from flask import render_template, redirect, url_for, request
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from app.models import Users, Workout, Exercises, ExercisesInWorkout
from app.forms import RegistrationForm, LoginForm, WorkoutForm
from datetime import datetime

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', title= 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.level.data < 1:
            setLevel = 1
        elif form.level.data <5:
            setLevel = 2
        else:
            setLevel = 3
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(username=form.username.data, password= hash_pw, level= setLevel)
        
        
        
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('workout'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember= form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('workout'))
    return render_template('login.html', title = 'Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/workout', methods=['GET','POST'])
@login_required
def workout():
    Workout.create(Workout)
    workouts = Workout.query.filter_by(userid= current_user.userid).all()
    userLevel = Users.query.filter_by(userid = current_user.userid).first().level
    exercises = Exercises.query.all()
    for workout in workouts:
        if workout.userid == current_user.userid:
            for exercise in exercises:
                if exercise.exerciseid <= userLevel:
                    workout.work.append(exercise)
                    db.session.commit()
    form = WorkoutForm()
    return render_template('workout.html', title= 'Workout', posts=userLevel)

