#!/bin/bash
git add .
git status
git commit -m "$1"
if [ $# = 2 ]
then
	git push -u origin $2
else
	git push -u origin master
fi

exit