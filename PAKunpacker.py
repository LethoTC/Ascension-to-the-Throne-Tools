import os

f1 = "Resource0.pak" # First PAK File
f2 = "Resource1.pak" # Second PAK File
folder1 = "PAK0" # PAK0 Folder
folder2 = "PAK1" # PAK1 Folder

    
os.makedirs(folder1, exist_ok=True) # Create Folder or skip
os.makedirs(folder2, exist_ok=True) # Create Folder or skip
repack1 = "FileData1.rep" # For Repacking
repack2 = "FileData2.rep" # For Repacking
pad = b'\x00\x00\x00\x00' # Used for temp sizes and temp offsets

if os.path.isfile(repack1): # Check to see if the repack.rep file exists
    os.remove(repack1) # If it does delete it
    print(repack1, 'deleted') # Print the result
if os.path.isfile(repack2): # Check to see if the repack.rep file exists
    os.remove(repack2) # If it does delete it
    print(repack2, 'deleted') # Print the result
        
with open(f1, "rb") as beg: # For Beginning
    magic = beg.read(4) # GRES is the magic
    unk = beg.read(4) # Not sure of the following bytes
    fileC = beg.read(4) # File Count
    for i in range(0, int.from_bytes(fileC, "little")): # The loop
        fileN = beg.read(128) # For reading and other usages
        fileD = fileN.decode() # Decode fileN
        nFile = fileD.replace('\0', '') # Removing nulls
        print(nFile) # Print the filenames
        fileO = beg.read(4) # File Offsets
        fileS = beg.read(4) # File Sizes
        fileB = beg.tell()  # Current Position   
        beg.seek(int.from_bytes(fileO, "little"), os.SEEK_SET) # Seek the offset
        fileByt = beg.read(int.from_bytes(fileS, "little")) # Read the bytes by the file size
        with open(os.path.join(folder1, nFile), "wb") as end: # For End
            end.write(fileByt) # Write the file data
        with open(repack1, "ab") as rep: # Creating the repack file
            rep.write(fileN) # Store the original 128 bytes
            rep.write(pad) # Write the temp pad for repacking later
            rep.write(pad) # Write the temp pad to be replaced by repacking files with current sizes later
        beg.seek(fileB) # Seek fileB
    print("First PAK File done.")

with open(f2, "rb") as mid: # For Second PAK File    
    magic2 = mid.read(4) # GRES is the magic
    unk2 = mid.read(4) # Not sure of the following bytes
    fileC2 = mid.read(4) # File Count
    for j in range(0, int.from_bytes(fileC2, "little")): # The Loop
        fileN2 = mid.read(128) # For reading and other usages
        fileD2 = fileN2.decode() # Decode fileN
        nFile2 = fileD2.replace('\0', '') # Removing nulls
        print(nFile2) # Print the filenames
        fileO2 = mid.read(4) # File Offsets
        fileS2 = mid.read(4) # File Sizes
        fileB2 = mid.tell()  # Current Position   
        mid.seek(int.from_bytes(fileO2, "little"), os.SEEK_SET) # Seek the offset
        fileByt2 = mid.read(int.from_bytes(fileS2, "little")) # Read the bytes by the file size
        with open(os.path.join(folder2, nFile2), "wb") as fin: # For End
            fin.write(fileByt2) # Write the file data
        with open(repack2, "ab") as rep2: # Creating the repack file
            rep2.write(fileN2) # Store the original 128 bytes
            rep2.write(pad) # Write the temp pad for repacking with updated data later
            rep2.write(pad) # Write temp pad for repacking with updated data later          
        mid.seek(fileB2) # Seek fileB2
    print("Second PAK File done.")
    
print("FileData.rep was created, keep for repacking if you choose.") # Info regarding the extra two files which are the repack files        
print("Extraction complete, you may go now.") # For completion
input() # For keeping the console open until the user closes it
