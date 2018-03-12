#!/usr/bin/env bash

version=$(python3 --version)

if [[ $version =~ .*3..* ]]
then
    python3 nowYouSeeMe.py
else
    echo "You need python 3.1, or later to run this game."
fi