import pandas as pd
df = pd.read_excel("./12cases.xlsx")
data_path = "/labs/gevaertlab/data/breast_segmentation_qinmei/dataset/"
f=open("./20240122.txt","a")
for row in range(df.shape[0]):
	file_path = df.iloc[row][0]
	pid = df.iloc[row][1]
	f.write(data_path + str(pid) + "nii.gz\n")
