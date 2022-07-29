#!/bin/bash

cd $(pwd)

mkdir -p $HOME/robertaPrograms
#echo "echo  $(pwd)/devel/setup.bash" >| $HOME/robertaPrograms/getWorkspace.sh 

cp -v "launchRobertaScript.bash" $HOME/robertaPrograms

sed -i '4 a source '$(pwd)'/devel/setup.bash' $HOME/robertaPrograms/launchRobertaScript.bash 

chmod +x $(pwd)/src/roberta_robotino_translator/scripts/*
chmod +x $HOME/robertaPrograms/*

catkin_make
catkin_make
