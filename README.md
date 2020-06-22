# Feats of Strength (FOS)

FOS is a Python web application, constructed using the Flask web framework. It allows you to provide tailor-made workout plans for a specific feat of strength, such as one-handed pushups. Users must register before using the app in order to generate workout plans suited to each user's ability. Users can store, edit and delete these workouts. The app comes with pre-made unit and integration tests, that can be used as a trigger for a continuous integration pipeline.
This app is ran on a Google Cloud Platform Ubuntu 18.04 virtual machine, using the Python-based HTTP web server Gunicorn.

The database is hosted on a GCP MySQL server.

## version 1.1:
Added workout rating functionality and related tests.


## Getting started with your own copy
To get a working copy of the project, simply pull down the repository and use the requirements.txt file (found in the root) to install the necessary python modules:

```bash
pip install -r requirements.txt
```

## Resources
[WebApp](http://35.242.145.187:5000/)

[Trello Board](https://trello.com/b/RqNvjEBM/feats-of-strength)


## Functionality
### Registration
You need to have a user account to use the app. The app uses a standard registration form with a username and password. The "How many pushups can you do?" question is used to determine the user's fitness level, which is then used to generate a workout that's appropriate to the user's current ability.

![Register](https://i.imgur.com/J2SBGok.png)

### Login
The app uses a standard login form, with the option to keep the user logged in if "Remember me" is ticked.
![Login](https://i.imgur.com/VnLvYg8.png)

### Workouts
This is the core page of the app, accessing it will automatically generate a user workout, if the user is new or if they have completed a previous workout. A workout consists of 3 sets with each set getting increasingly harder. A user's level (see registration) corresponds to an exercise in the database and determines the hardest type of exercise the user should do. This exercise is assigned as set 3, alongside two progressively easier exercises for set 1 and 2:
![Example Workout1](https://i.imgur.com/95XS2yY.png)

The user can then enter the number of reps they have completed for each set and submit the form to be redirected to their workout log.
#### Exceptions
If a user's level is below 3 their workouts will be generated differently:
Level 2 - This user's workout will consist of their hardest exercise as set 3, and two sets of the same (easier) exercise for sets 1 and 2.
Level 3 - This user's workout will consist of three sets of the same exercise, as they are not fit enough for the higher tier exercises.
#### Exercise table structure
The exercise table contains a list of exercises that get progressively harder, the higher their exercise id. This allows for an easy way to create skill-level tailored workouts.

### Workout log
This section contains all of the user's previously completed workouts (and their most recently generated unfinished workout).
The user has the option to either delete their latest workout by ticking the "Delete latest workout" box and pressing "Submit" or updating their most recent workout. 
![Log page](https://i.imgur.com/mOBWkp0.png)
Clicking on the "Update Latest Workout" link will redirect the user to a dynamic URL, set by the user's most recent workout id, within which the user can enter the corrected number of reps for their latest workout.

![Update page](https://i.imgur.com/95XS2yY.png)
#### Drawbacks
Note there are some drawbacks. Firstly, a user must delete their unfinished workout (if present) before attempting to edit their finished workouts. Secondly, a user can only edit their latest workout, meaning that they have to delete other workouts to get to a workout lower down on the page.

### Logout
Users can log out of their accounts by pressing the 'Logout' button, which is always located at the top right corner of the page.

![Logout](https://i.imgur.com/cTkhWcR.png)

### Workout Ratings (v1.1)
Users can rate their latest workout by following the "Review Latest Workout" link on the Workout Log Page. Users are then asked to give their latest workout a rating from 1-10. If a workout is given a rating, a message will show up on the home feed saying: "A user rated their workout as x/10 on date time". The same workout can not be rated twice.

## Architecture
### Database Structure
Please find below the progression of the app's entity relationship diagram from the conception of the idea through to implementation:

#### Initial ERD Concept
![Initial Idea](https://i.imgur.com/4WzIJQX.png)

#### ERD Progression (implementing a many-to-many relationship)
The initial ERD design was not fit for the intended many-to-many relationship between the workout and exercises tables. Whereas, this design solves those issues. 
![ERD Progression](https://i.imgur.com/LFmVKUl.png)

#### Final ERD (v1.0) 
This version of the ERD got rid of unnecessary columns and assigned the Exercises In Workouts table a PK, to get around errors during workout creation.
![Final ERD](https://i.imgur.com/EvltqW6.png)

#### Final ERD (v1.1)
This ERD was implemented in version 1.1, as a part of the workout ratings functionality.
![ERD 1.1](https://i.imgur.com/2TcCdBR.png)

#### ERD Functionality
Each user is assigned a workout id upon workout generation, a user can have many workout ids, but each workout id is unique to one user.
The app also models a many-to-many relationship between Workouts and Exercises using an association table. This allows for the generation of custom workouts, using a list of exercises found in the exercise table that are matched to a workout ID and each workout ID is assigned to one user.
##### v1.1
Each workout can now have one rating assigned to it and each rating must have a unique workout id.

## Continuous Integration
The web app uses Jenkins, as its CI server. Changes made to the master branch of this repository are automatically detected (using webhooks), triggering automated testing, which (if successful) triggers the restart of the application.

## Project Tracking
Project management was conducted using a Trello (kanban) board, with a MOSCOW system indicating the importance of each task. The board can be accessed [here](https://trello.com/b/RqNvjEBM/feats-of-strength).

## Risk Assessment
The final document can be found [here](https://drive.google.com/file/d/1-GfLXsC_jvMjW4AnRw3JfweoX_0BB4g0/view?usp=sharing).

### Initial Risk Assessment
Before any project work began, an initial risk assessment was conducted to identify any risks and potential mitigation strategies:
![Initial Risk Assessment](https://i.imgur.com/IPjqWBd.png)

### Reflection
After completion of the project, minor corrections and a reflection upon the initial risk assessment were conducted:
![Reflection](https://i.imgur.com/cPkhfnz.png)

## Testing
The app comes with unit tests (pytest) and integration tests (selenium), covering the main functions of the app. To run the tests on your copy, simply run pytest in the root of the application:

```bash
pytest
```

The unit tests cover registration, login, workout generation, workout deletion, workout update and workout review (v1.1) functionalities.
![coverage](https://i.imgur.com/qSfEUmT.png)
Alternatively, the latest test coverage report can be viewed [here](http://35.242.145.187:5000/coverage).
The integration tests currently cover registration, workout generation and workout updating functionalities.

### Testing Improvements
Further integration tests must be developed for the workout deletion and workout review (v1.1) functionalities.

## Overall Workflow
![Workflow](https://i.imgur.com/DUL0CbH.png)

## Potential Improvements
### Delete/update any workout functionality
Some work needs to be done so that a user can edit and/or delete any workout that they have completed from the log, without having to delete the previous workouts.

### User level-up system
User levels should increase once they've managed to do a certain numbers of reps on their hardest exercise. This can be implemented via matching the reps completed in a user's latest workout to the threshold column in the exercise table. Once a threshold is reached, the user's level increases by one. This would result in the user's next workout having harder exercises.

### Injury prevention page
The app needs an injury prevention page, which provides information for preventing, identifying and dealing with injuries.

### Home page community content
The home page could use some sort of hi-scores table or top 20 most recently finished workouts table, so that users can see others participating and progressing.

### Account page
The app needs a user account page, in which users could update or delete their user information. This would also include their date of birth, which currently exists on the database as a default entry for when the user registered.

### Workout Ratings (v1.1)
The workout ratings form needs a custom error validation function to prevent users from rating a workout outside of the 1-10 range. Furthermore, the ratings displayed on the home page could use some more information about the workouts, such as the exercise that the rated workout involved.
