#declare the dataset list
dataset = [2, 3, 4, 1, 2, 5]

#find the mean of dataset
sm=0
for i in range(len(dataset)):
   sm+=dataset[i]
   mean = sm/len(dataset)

#calculating population standard deviation of the dataset
deviation_sum = 0
for i in range(len(dataset)):
   deviation_sum+=(dataset[i]- mean)**2
   psd = math.sqrt((deviation_sum)/len(dataset))

#calculating sample standard deviation of the dataset
ssd = math.sqrt((deviation_sum)/len(dataset) - 1)

#display output
print("Population standard deviation of the dataset is", psd)
print("Sample standard deviation of the dataset is", ssd)
