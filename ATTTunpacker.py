import os
import sys

f1 = "Resource0.pak" # First PAK File
f2 = "Resource1.pak" # Second PAK File
folder1 = "PAK0" # PAK0 Folder
folder2 = "PAK1" # PAK1 Folder
os.mkdir(folder1) # Create Folder
os.mkdir(folder2) # Create Folder
repack1 = "FileData.rep" # For Repacking
repack2 = "FileData.rep" # For Repacking
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

        with open(os.path.join(folder1, repack1), "ab") as rep: # Creating the repack file
            rep.write(fileN) # Store the original 128 bytes
            rep.write(fileO) # Store the original File Offsets
            rep.write(fileS) # Store the original File Sizes

        beg.seek(fileB) # Seek fileB

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
        with open(os.path.join(folder2, nFile2), "wb") as fin: # For Final
            fin.write(fileByt2) # Write the file data

        with open(os.path.join(folder2, repack2), "ab") as rep2: # Creating the repack file
            rep2.write(fileN2) # Store the original 128 bytes
            rep2.write(fileO2) # Store the original File Offsets
            rep2.write(fileS2) # Store the original File Sizes

        mid.seek(fileB2) # Seek fileB2
    
print("FileData.rep was created, keep for repacking if you choose") # Info regarding the extra two files which are the repack files        
print("Extraction complete, you may go now.") # For completion
input() # For keeping the console open until the user closes it
