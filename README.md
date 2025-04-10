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
[![asciicast](https://asciinema.org/a/zBPjAiicPsFc6r6bcIJMc5Y64.svg)](https://asciinema.org/a/zBPjAiicPsFc6r6bcIJMc5Y64)

## brain-prime
[![asciicast](https://asciinema.org/a/9prcHFh5TqSSSpVAF6zO8PIbv.svg)](https://asciinema.org/a/9prcHFh5TqSSSpVAF6zO8PIbv)

# Installation
You will need:
1. install uv package manager.
You can find how to install uv here (russian): https://github.com/Hexlet/ru-instructions/blob/main/uv.md
or here (english): https://docs.astral.sh/uv/#getting-started
2. install git 
3. clone repository
4. sync packeges
```
make install
```
5. install games
```
make package-install
```

# How to play
to start the game, you need to run the command: `make <game name>`

where `<game name>` - name of games. It's can be:<br/>
`brain-calc` - generate two numbers and ask calculate<br/>
`brain-even` - generate random number and ask user if it is even<br/>
`brain-games` - greetig player<br/>
`brain-gcd` - generate two numbers and ask find greatest common divisor<br/>
`brain-prime` - generate random number and ask if it is prime<br/>
`brain-progression` - generate progression and ask find missing number<br/>
