import os

f1 = "Resource0.pak" # First PAK File
f2 = "Resource1.pak" # Second PAK File
folder1 = "PAK0" # PAK0 Folder
folder2 = "PAK1" # PAK1 Folder
temp = b'\x00\x00\x00\x00'
repack1 = "FileData1.rep" # For Repacking
repack2 = "FileData2.rep" # For Repacking
pad = b'\x00\x00\x00\x00' # Used for temp sizes and temp offsets

def rem(file: str): # For removing existing files
    if os.path.isfile(file):
        os.remove(file)
        print(file, "is deleted.".format(file))

def unpack(pakf: str, undir: str, repfile: str): # For unpacking the PAK files
    with open(pakf, "rb") as pak: # The PAK files being read
        magic = pak.read(4)
        unk = pak.read(4)
        filecount = pak.read(4)
        for i in range(0, int.from_bytes(filecount, "little")): # Loop
            rawname = pak.read(128)
            filename = rawname.decode()
            filename = filename.replace('\0', '')
            print(filename, " File Number: ", i)
            fileoffset = int.from_bytes(pak.read(4), "little")
            filesize = int.from_bytes(pak.read(4), "little")
            likehere = pak.tell()
            pak.seek(fileoffset)
            filedata  = pak.read(filesize)
            with open(os.path.join(undir, filename), "wb") as end: # Unpacking the files from the PAK Archives
                      end.write(filedata)
            with open(repfile, "ab") as rep: # Creating the Repack files
                      rep.write(rawname)
                      rep.write(temp)
                      rep.write(temp)
            pak.seek(likehere)
                      
if __name__ == "__main__":
    os.makedirs(folder1, exist_ok=True) # Create Folder or skip
    rem(repack1) # Remove .rep file if it exists
    unpack(f1, folder1, repack1) # For unpacking the PAK file

    os.makedirs(folder2, exist_ok=True) # Create Folder or skip
    rem(repack2) # Remove .rep file if it exists
    unpack(f2, folder2, repack2) # For unpacking the PAK file
                      

print("FileData.rep was created, keep for repacking if you choose.") # Info regarding the extra two files which are the repack files        
print("Extraction complete, you may go now.") # For completion
input() # For keeping the console open until the user closes it
