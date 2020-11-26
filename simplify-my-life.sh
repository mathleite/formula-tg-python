#!/bin/bash

GREEN_COLOR='\033[0;32m'
NO_COLOR='\033[0m'

printf "${GREEN_COLOR}Running Mypy linter!\n"
echo $(mypy src/ test/)

printf '\nRunning Tests!'
echo $(python -m unittest)
printf "\n${NO_COLOR}Bye!\n"
