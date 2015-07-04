#Author: Filmon
#This is a script to build toplogy prior submitting it to cluster
#!/bin/bash
$FILE="truck_topology_inbound.jar"
if [ -e $FILE ];
then
rm $FILE
fi
pyleus -c pyleus.conf build truck_topology_inbound.yaml
