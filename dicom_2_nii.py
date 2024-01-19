import dicom2nifti
import pandas as pd
import os
import os.path as osp
import shutil
df = pd.read_excel("./9case_20240118.xlsx")
nii_path = "/scratch/groups/ogevaert/HER2BreastCancer/nii_for_segment"
for row in range(df.shape[0]):
	file_path = df.iloc[row][0]
	pid = df.iloc[row][1]
	shorted_path_list = file_path.split("/")[:-1]
	original_file_path = "/".join(shorted_path_list)
	pid_dir = osp.join(nii_path, str(pid))
	print(original_file_path)
	print(pid)
	print(pid_dir)
	if not osp.exists(pid_dir):
		os.mkdir(pid_dir)
	dicom2nifti.convert_directory(original_file_path, pid_dir, compression=True)
	print("nii created")
	new_file_name = osp.join(nii_path, str(pid)+".nii.gz")
	for file in os.listdir(pid_dir):
		print("moving file %s" %(file))
		shutil.move(osp.join(pid_dir, file), new_file_name)
	os.rmdir(pid_dir)
