# Battleship
Simple Python Implementation of Battleship designed to test pre commit hooks and other Git repository features. This repository currently uses [Black](https://github.com/psf/black#version-control-integration) to check the format of Python files before a commit and will disallow the commit if the code is not formatted correctly.
### Run
Although this is prediominatly for testing what can be done with a Git repository, the game can still be played. Simply run the below command:

```python battelship.py```

Here are the rules to Battleship (this project may take some liberties.) Please note that when inputting the coordinates for a ship it must be in a Python list like so: 
```[(1,2),(2,2),(3,2)]```
