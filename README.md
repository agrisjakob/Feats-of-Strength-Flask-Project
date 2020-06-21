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
