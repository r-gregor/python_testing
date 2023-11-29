import tarfile

# gr_TRFJL = "targz-file.tar.gz"
gr_TRFJL = "bckpbin-en.current.tar.gz"
tar = tarfile.open(gr_TRFJL, "r:gz")
for tarinfo in tar:
	print(tarinfo.name, "is", tarinfo.size, "bytes in size and is ", end="")
	if tarinfo.isreg():
		print("a regular file.")
	elif tarinfo.isdir():
		print("a directory.")
	else:
		print("something else.")
tar.close()
