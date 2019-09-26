#!/bin/bash
#simple program for tracking time of a task
#chmod a+x track.sh
#Form: ./track [argument]
#Flags: {-start [label] (start), -stop (stop), -status (status)}

option=$1; shift;
label=$1;
LOGFILE="./track.txt" #for logging all the tasks
TIMEFILE="./time.txt" #for keeping track of the time spent on each task
lastWord=$(awk '{w=$1} END{print w}' $LOGFILE)

case "$option" in
	start)
		if [ "$lastWord" = "" ]; then
			startDate=$(date);
			fixedStart=$(date +%s)
			taskNr=$(grep -c -o "LABEL" $LOGFILE) #setting the task number
			echo "START $startDate" >> $LOGFILE
			echo "LABEL this is task $taskNr: $label" >> $LOGFILE
			echo -n "$fixedStart " >> $TIMEFILE
 		else
			echo "A task is already running."
		fi
		;;

	stop)
		if [ "$lastWord" = "LABEL" ]; then
			endDate=$(date);
			fixedEnd=$(date +%s)
			echo "END $endDate" >> $LOGFILE
			echo "" >> $LOGFILE
			echo "$fixedEnd" >> $TIMEFILE
		else 
			echo "No active task to stop."
		fi
		;;

	status)
		if [ "$lastWord" = "LABEL" ]; then
			taskNr=$(grep -c -o "LABEL" $LOGFILE) #setting the current tracking number, the last in this case
			label=$(awk '{w=$6} END{print w}' $LOGFILE) #setting the current task 
			echo "Currently tracking task $taskNr: $label"
		else 
			echo "No active task beeing tracked."
		fi
		;;

	log)
		if [ "$lastWord" = "" ]; then
			declare -i taskNr=0
			while IFS=: read -r line
			do
				#taskNr=$(grep -c -o "LABEL" $LOGFILE)
				taskNr+=1
				start=$(echo $line | awk '{printf $1}')
				end=$(echo $line | awk '{printf $2}')

				#finding time difference
				DIFFSEC=$(( $end - $start ))

				#converting back to something meaningful
				let S=${DIFFSEC}%60
				let MM=${DIFFSEC}/60 # Total number of minutes
	  			let M=${MM}%60
	  			let H=${MM}/60
				timestamp=$(printf "%02d:%02d:%02d" $H $M $S)

				echo "Task $taskNr: $timestamp"
			done <"$TIMEFILE"
		else
			echo "Task is still running, stop to see log."
		fi
		;;
	*)
		echo "$0: invalid option $option"; exit ;
esac