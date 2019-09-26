#!/bin/bash
#simple program for climbing the directory
# source climb.sh
# Form: climb [amount of climb]

function climb { 
	local climbAmount i 
	climbNr=$1
	
	#setting the climb number to 1 if no parameter is set.
	if [[ -z $climbNr ]]; then
    	climbNr=1
	fi

	#looping through the number of climbs and jumping a directory up for each climb
    for (( i=0; i < climbNr; i++ )); do
        climbAmount+=../
    done

    #jumping to the new path/directory
    cd "$climbAmount"
}