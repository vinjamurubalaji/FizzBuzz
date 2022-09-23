

import csv

input_file = csv.DictReader(open("Trails.csv"))
Activecount = 0;
LightsCount = 0;
WalkaBikecount=0
TrailsAfter2000 = []
Trailstouple = ()
for row in input_file:
    try:
        age= int(row["INST_YEAR"])
        if(age > 2000 and row["TRAIL_NAME"] != 'UNKNOWN NAME'):
            TrailsAfter2000 . append(row["TRAIL_NAME"])
        if (row['STATUS']=='ACTIVE' and row["TRAIL_NAME"] != 'UNKNOWN NAME' and age != 0):
            Activecount+=1
        if (row['LIGHT']=='Yes' and row["TRAIL_NAME"] != 'UNKNOWN NAME' and age != 0):
            LightsCount+=1
        if (row['WALKING']=='Yes' and row['BIKING']=='Yes' and row["TRAIL_NAME"] != 'UNKNOWN NAME' and age != 0 and row['LIGHT']=='Yes'):
            WalkaBikecount+=1
            Trailstouple = Trailstouple + (row["TRAIL_NAME"],row["CONDITION"],row['LIGHT'],row['STATUS'],row['WALKING'],row['BIKING'])
    except:
        continue
print('trails that are Active :',Activecount)
print(tuple(set(TrailsAfter2000)))
print('Trails with Lights :',LightsCount)
print('Trails with Walking and Biking: ',WalkaBikecount)
print('touple is :',tuple(set(Trailstouple)) )
