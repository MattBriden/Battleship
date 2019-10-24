# Battleship
Simple Python Implementation of Battleship designed to test pre commit hooks and other Git repository features. This repository currently uses [Black](https://github.com/psf/black#version-control-integration) to check the format of all Python files attempted to be committed. If one of the proposed files does not pass Black's formatting check the commit will be disallowed until the code is formatted correctly.

### Example output when files need updated
```
git commit
black....................................................................Failed
hookid: black

Files were modified by this hook. Additional output:

reformatted battleship.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

### Example output when files are formatted correctly
```
git commit
black....................................................................Passed
[master 66324bf]
```

### Example output when Python files are unchanged
```
git commit
black................................................(no files to check)Skipped
[master 406c8a3]
```

### Run
Although this is predominantly for testing what can be done with a Git repository, the game can still be played. Simply run the below command:

```python battleship.py```

[Here](https://en.wikipedia.org/wiki/Battleship_(game)) are the rules to Battleship (this project may take some liberties.) Please note that when inputting the coordinates for a ship it must be in a Python list like so: 
```[(1,2),(2,2),(3,2)]```
