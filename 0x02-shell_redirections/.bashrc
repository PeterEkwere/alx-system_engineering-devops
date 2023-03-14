#This is a command to automatically create a sha-bang file
newprogramfile () {
	if [-e $l]
	then 
		echo "this file already exist"
	else
		echo "#!/bin/bash" > $l
		echo "this was created by $USER" >> $l
		vim $l
	fi

}
