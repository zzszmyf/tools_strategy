import os
import sys

label = "bad_good"

schema_list = []
schema_index = {}
schema_line = ""
fea_label_count = {}

with open(sys.argv[1]) as f:
    schema_line = f.readline()
    schema_list = schema_line.strip().split(",")
    
for index, schema_value in enumerate(schema_list):
    schema_index[schema_value] = index

with open(sys.argv[2]) as f:
    for line in f.readlines():
        if line == schema_line:
            continue
        ins_lst = line.strip().split(",")
        for index, ins_fea in enumerate(ins_lst):
            key = ",".join([schema_list[index],ins_lst[schema_index[label]], ins_fea])
            fea_label_count[key] = fea_label_count.get(key, 0) + 1

for key in fea_label_count:
    print ("%s\t%d" % (key, fea_label_count[key]))
