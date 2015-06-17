#!/bin/bash
pyleus -c pyleus.conf build truck_topology.yaml
pyleus -c pyleus.conf submit truck_topology.jar
