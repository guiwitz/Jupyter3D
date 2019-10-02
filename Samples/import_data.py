import requests

myfile = requests.get('https://www.dropbox.com/s/c81t4rjqtdufowz/training_groundtruth.tif?dl=1', allow_redirects=True)
open('training_groundtruth.tif', 'wb').write(myfile.content)

myfile = requests.get('https://www.dropbox.com/s/rjkpujq2js6lvu7/training.tif?dl=1', allow_redirects=True)
open('training.tif', 'wb').write(myfile.content)