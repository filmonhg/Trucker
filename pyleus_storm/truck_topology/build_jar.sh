#Author: Filmon
#This is a script to build topology prior submitting it to cluster
#!/bin/bash
$FILE="truck_topology.jar"
if [ -e $FILE ];
then
rm $FILE
fi
pyleus -c pyleus.conf build truck_topology.yaml
