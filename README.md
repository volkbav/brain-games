### Hexlet tests and linter status:
[![Actions Status](https://github.com/volkbav/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/volkbav/python-project-49/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/c8fb98ab26e34c3f9592/maintainability)](https://codeclimate.com/github/volkbav/python-project-49/maintainability)

# Intro
I present a set of mind games "brain-games"

# Demo
## brain-even
[![asciicast](https://asciinema.org/a/ih1dfdYA9lQWdSaRw5RFRv6N7.svg)](https://asciinema.org/a/ih1dfdYA9lQWdSaRw5RFRv6N7)

## brain-calc
[![asciicast](https://asciinema.org/a/XMKYDz7WHhfEqZkINOosXQFsl.svg)](https://asciinema.org/a/XMKYDz7WHhfEqZkINOosXQFsl)

## brain-gcd
[![asciicast](https://asciinema.org/a/dibJr6I8zcZWuoFyTYojH2p37.svg)](https://asciinema.org/a/dibJr6I8zcZWuoFyTYojH2p37)

## brain-progression
[![asciicast](https://asciinema.org/a/k4mAacnyVu56yQxGh1ZYAQjs1.svg)](https://asciinema.org/a/k4mAacnyVu56yQxGh1ZYAQjs1)

# Installation
You will need:
1. install uv package manager.
You can find how to install uv here: https://github.com/Hexlet/ru-instructions/blob/main/uv.md
2. install git 
3. clone repository
```
git clone git@github.com:volkbav/python-project-49.git
```
3. sync packeges
```
make install
```
4. install games
```
make package-install
```

# How to play
to start the game, you need to run the command: `make <game name>`

where `<game name>` - name of games. It's can be:<br/>
`brain-games` - greetig player<br/>
`brain-even` - generate random number and ask user if it is even<br/>
`brain-calc` - generate two numbers and ask calculate<br/>
`brain-gcd` - generate two numbers and ask find greatest common divisor