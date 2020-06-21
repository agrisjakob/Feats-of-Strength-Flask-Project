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
