# Import all libraries needed for the tutorial
from pandas import DataFrame, read_csv
import pandas as pd


#read the csv file 
#Link to download national names: https://www.kaggle.com/kaggle/us-baby-names
#Use the file path to your CSV
df = pd.read_csv('NationalNames.csv', names =['ID','Names','year','gender','count'])


#print 'list of names: '
#print df#['Names']#[:30]
#print '^^ number of total names ^^'
isMale = df['gender']=='M'
isLength = df['Names'].str.len() == 5;
isPopular = df['count'] > 20
isRecent = (df['year'] > 1890)&(df['year'] < 2010 )
df = df[isMale&isLength&isPopular&isRecent]
print df

del df['ID']
del df['year']
del df['gender']
del df['count']

uniqueNames = df['Names'].unique()


df = pd.DataFrame(data = uniqueNames, columns = ['Names'])
df = df

print df


#after filtering it is small enough that you should be able to open it in excel
df.to_csv('filtered_names.csv',index=False,header=False) #create a new csv with filtered data if you want to
exit('exited after exporting filtered csv')

count = 0 #counts number of grids are found

for item, frame in df['Names'].iteritems():
    if pd.notnull(frame):
    	name1 = frame.upper()
    	for item, frame2 in df['Names'].iteritems():
    		if pd.notnull(frame2):
    			name2 = frame2.upper()
    			if (name2[0] == name1[1])&(name2!=name1):
    				for item, frame3 in df['Names'].iteritems():
    					if pd.notnull(frame3):
    						name3 = frame3.upper()
    						isNotRepeat = (name3!=name1)&(name3!=name2);
    						if (name3[0] == name1[2])&(name3[1]==name2[2])&isNotRepeat:
    							for item, frame4 in df['Names'].iteritems():
    								if pd.notnull(frame4):
    									name4 = frame4.upper()
    									isNotRepeat = (name4!=name1)&(name4!=name2)&(name4!=name3);
    									if (name4[0] == name1[3])&(name4[1]==name2[3])&(name4[2]==name3[3])&isNotRepeat:
    										for item, frame5 in df['Names'].iteritems():
    											if pd.notnull(frame5):
    												name5 = frame5.upper()
    												isNotRepeat = (name5!=name1)&(name5!=name2)&(name5!=name3)&(name5!=name4);
    												if (name5[0] == name1[4])&(name5[1]==name2[4])&(name5[2]==name3[4])&(name5[3]==name4[4])&isNotRepeat:
    													count=count+1
    													print 'Grid Number: ' + str(count)
    													print 'Name 1: ' + name1
    													print 'Name 2: ' + name2
    													print 'Name 3: ' + name3
    													print 'Name 4: ' + name4
    													print 'Name 5: ' + name5
    													print '  '


    			
    	