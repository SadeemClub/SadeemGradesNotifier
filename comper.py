import filecmp 
  
# Path of first file 
file1 = "/media/sahar/years/paython/learn/file1.txt"
  
# Path of second file 
file2 = "/media/sahar/years/paython/learn/file2.txt"
   
# Compare the os.stat() 
# signature i.e the metadata 
# of both files  
comp = filecmp.cmp(file1, file2) 
  
# Print the result of comparison 
print(comp) 
  
# Compare the 
# contents of both files 
comp = filecmp.cmp(file1, file2, shallow = False) 
  
# Print the result of comparison 
print(comp) 
