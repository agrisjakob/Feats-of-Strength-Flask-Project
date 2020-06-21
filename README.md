# Feats of Strength (FOS)

FOS is a Python web application, constructed using the Flask web framework. It allows you to provide tailor-made workout plans for a specific feat of strength, like one-handed pushups. Users must register before using the app in order to generate workout plans suited to each user's ability. Users can store, edit and delete these workouts. The app comes with pre-made unit and integration tests, that can be used as a trigger for a continuous integration pipeline.

## Getting started with your own copy
To get a working copy of the project, simply pull down the repository and use the requirements.txt file (found in the root) to install the necessary python modules:

```bash
pip install -r requirements.txt
```

## Resources
[WebApp](http://http://35.242.145.187:5000/)
[Trello Board](https://trello.com/b/RqNvjEBM/feats-of-strength)

## Architecture
### Database Structure
Please find below the progression of the app's entity relationship diagram from the conception of the idea through to implementation:

#### Initial ERD Concept
![Initial Idea](https://i.imgur.com/4WzIJQX.png)

#### ERD Progression (implementing a many-to-many relationship)
The initial ERD design was not fit for the intended many-to-many relationship between the workout and exercises tables. Whereas, this design solves those issues. 
![ERD Progression](https://i.imgur.com/LFmVKUl.png)

#### Final ERD (currently implemented)
This version of the ERD got rid of unnecessary columns and assigned the Exercises In Workouts table a PK, to get around errors during workout creation.
![Final ERD](https://i.imgur.com/EvltqW6.png)

#### ERD Functionality
The app models a many-to-many relationship between Workouts and Exercises using an association table. This allows for the generation of custom workouts, using a list of exercises found in the exercise table that are matched to a workout ID and each workout ID is assigned to one user.

## Project Tracking
Project management was conducted using a Trello (kanban) board, with a MOSCOW system indicating the importance of each task. The board can be accessed [here](https://trello.com/b/RqNvjEBM/feats-of-strength)

## Risk Assessment
The final document can be found [here](https://drive.google.com/file/d/1-GfLXsC_jvMjW4AnRw3JfweoX_0BB4g0/view?usp=sharing)

### Initial Risk Assessment
Before any project work began, an initial risk assessment was conducted to identify any risks and potential mitigation strategies:
![Initial Risk Assessment](https://i.imgur.com/IPjqWBd.png)

### Reflection
After completion of the project, minor corrections and a reflection upon the initial risk assessment were conducted:
![Reflection](https://i.imgur.com/cPkhfnz.png)

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
