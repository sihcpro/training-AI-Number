#!/bin/bash
git add .
git status
echo "commit -m $1"
git commit -m "$1"
if [ $# = 2 ]
then
	echo "git push -u origin $2"
	git push -u origin $2
else
	echo "git push -u origin master"
	git push -u origin master
fi

exit