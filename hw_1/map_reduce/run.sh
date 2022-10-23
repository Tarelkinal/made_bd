#!/bin/bash

hdfs dfs -rm -r /hw1/mapred.out

mapred streaming \
	-input /hw1/price.csv \
	-output /hw1/mapred.out \
	-mapper "/usr/bin/python3 var_mapper.py" \
	-reducer "/usr/bin/python3 var_reducer.py" \
	-file var_mapper.py \
	-file var_reducer.py

