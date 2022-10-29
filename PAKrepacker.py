import os
import sys

f1 = "Resource0.pak" # The bigger newly repacked archive
f2 = "Resource1.pak" # The smaller second new repacked archive
folder1 = "PAK0" # PAK0 Folder
folder2 = "PAK1" # PAK1 Folder
repack1 = "FileData1.rep" # For Resource0 Repacking
repack2 = "FileData2.rep" # For  Resource1 Repacking
f1info = b'\x47\x52\x45\x53\x64\x00\x00\x00\xB5\x1C\x00\x00' # Initial pak data for Resource0
f2info = b'\x47\x52\x45\x53\x64\x00\x00\x00\x35\x00\x00\x00' # Initial pak data for Resource1


if os.path.isfile(f2): # Check to see if the Archive file exists
  os.remove(f2) # Remove if it does
  print(f2, "deleted")
if os.path.isfile(f1): # Check to see if the Archive file exists
  os.remove(f1) # Remove if it does
  print(f1, "deleted")

with open(f2, "wb") as start: # Create the test archive
  start.write(f2info) # Write the starting data
  print("First PAK Archive created.")
  print("Now reading rep file.")
  
with open(repack2, "r+b") as pack1: # Begin repacking of the archive
  for i in range(0, 53): # for looping
    fileN = pack1.read(128) # File header
    nFile = fileN.decode()  # Decode to string
    fName = nFile.replace('\0', '') # Replace the nulls
    tempOff = pack1.read(4) # Read the temp offsets
    tempSize = pack1.read(4) # Read the temp size
    with open(f2, "ab") as beg1: # Pack Resource1.pak
      cSize = os.path.getsize(os.path.join(folder2, fName)) # Used to get the current file sizes to allow increased file sizes
      corSize = cSize.to_bytes(4, "little") # Convert to four bytes
      beg1.write(fileN) # Write the file headers
      beg1.write(tempOff) # Write the temp file offsets
      beg1.write(corSize) # Write the updated file sizes

print("Finishing PAK Archive Packing.")

with open(repack2, "rb") as rep1: # Finishing the first archive
  offsets = []
  for i in range(0, 53): # For looping
    fN = rep1.read(128) # Filenames
    nF = fN.decode() # Converting to string
    fOp = nF.replace('\0', '') # Replacing the nulls
    irrev = rep1.read(8) # Not needed now
    with open(os.path.join(folder2, fOp), "rb") as beg2: # For reading the file data
      fsize = os.path.getsize(os.path.join(folder2, fOp)) # Get current file size for reading.
      fdata = beg2.read(fsize) # Reading the file based on fsize
    with open(f2, "ab") as fin2: # Adding the file data
      tempOff = fin2.tell() # Set offsets
      oOff = tempOff.to_bytes(4, "little") # Convert to four bytes
      offsets.append(oOff) # Add the offsets to the list
      ffinal = fin2.write(fdata) # Write the file data
    with open(f2, "r+b") as corr: # Updating offsets
      corr.seek(12) # Advance to the needed offset
      for newOffsets in offsets: # Use the offsets from the list
        fileName = corr.read(128) # Read the filename headers
        offset = corr.write(newOffsets) # Write the correct offsets to the file data
        fileSize = corr.read(4) # Read the file size but not needed now
  offsets.clear()

print("First PAK Archive is Finished.")

print("Beginning next PAK Archive creation.")
print("The Second Archive will take longer to pack. please wait until the script is finished.")

with open(f1, "wb") as nstart: # Create the test archive
  nstart.write(f1info) # Write the starting data
  print("Second PAK Archive created.")
  print("Now reading rep file.")
with open(repack1, "r+b") as pack2: # Begin repacking of the archive
  for i in range(0, 7349): # For looping
    fileN = pack2.read(128) # File header
    nFile = fileN.decode()  # Decode to string
    fName = nFile.replace('\0', '') # Replace the nulls
    tempOff = pack2.read(4) # Read the temp offsets
    tempSize = pack2.read(4) # Read the temp size
    with open(f1, "ab") as nbeg: # Pack archive
      cSize = os.path.getsize(os.path.join(folder1, fName)) # Used to get the current file sizes to allow increased file sizes
      corSize = cSize.to_bytes(4, "little") # Convert to four bytes
      nbeg.write(fileN) # Write the file headers
      nbeg.write(tempOff) # Write the temp file offsets
      nbeg.write(corSize) # Write the updated file sizes

print("Finishing PAK Archive Packing.")

with open(repack1, "rb") as rep2: # Finishing the second archive
  offsetus = []
  for i in range(0, 7349): # For looping
    fN = rep2.read(128) # Filenames
    nF = fN.decode() # Converting to string
    fOp = nF.replace('\0', '') # Replacing the nulls
    irrev = rep2.read(8) # Not needed now
    with open(os.path.join(folder1, fOp), "rb") as nbeg2: # For reading the file data
      fsize = os.path.getsize(os.path.join(folder1, fOp)) # Get the current file size
      fdata = nbeg2.read(fsize) # Reading the file based on fsize
    with open(f1, "ab") as nfin: # Adding the file data
      tempOff = nfin.tell() # Set offsets
      oOff = tempOff.to_bytes(4, "little") # Convert to four bytes
      offsetus.append(oOff) # Add the offsets to the list
      ffinal = nfin.write(fdata) # Write the file data
    with open(f1, "r+b") as ncorr: # Updating offsets
      ncorr.seek(12) # Advance to the needed offset
      for newOffsets in offsetus: # Use the offsets from the list
        fileName = ncorr.read(128) # Read the filename headers
        offset = ncorr.write(newOffsets) # Write the correct offsets to the file data
        fileSize = ncorr.read(4) # Read the file size but not needed now
  offsetus.clear()
    
print("Second PAK Archive is Finished.")
input("Task completed, please keep the .rep files for any future repacking.")
