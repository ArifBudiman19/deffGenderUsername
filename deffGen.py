import re
import numpy as np

from util import load_dataset, save_dataset1D

dataArray = load_dataset('./dataset/name.data')
dataTrainArray = load_dataset('./dataset/test.gender.nolabel.data')
dataResult = np.copy(dataTrainArray)

i = 0
for dataTrain in dataTrainArray:
	name = dataTrain[0]
	#gender++ if male
	#gender-- if female
	gender = 0
	
	d1Name = re.findall('[A-Z][^A-Z]*', name)
	for d2Name in d1Name:
		dName = re.findall('[a-zA-Z]+', d2Name)
		
		for d in dName:
			for data in dataArray:
				if(len(data[0]) >= 3):
					if(data[0].lower() == d.lower()):
						if(data[1] == 'F'):
							gender -= 1
						else:
							gender += 1
	
	if(gender == 0):
		for d2Name in d1Name:
			dName = re.findall('[a-zA-Z]+', d2Name)
			
			for d in dName:
				for data in dataArray:
					if(len(data[0]) >= 3):
						if(d.lower() in data[0].lower()):
							if(data[1] == 'F'):
								gender -= 1
							else:
								gender += 1
						elif(data[0].lower() in d.lower()):
							if(data[1] == 'F'):
								gender -= 1
							else:
								gender += 1
		
	if gender > 0:
		dataResult[i][0] = 'M'	
	elif gender < 0:
		dataResult[i][0] = 'F'
	else:
		dataResult[i][0] = 'U'
	i += 1
	
for data in dataResult:
	print data[0]
