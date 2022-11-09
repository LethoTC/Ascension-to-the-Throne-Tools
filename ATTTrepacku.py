import os

f1 = "Resource0.pak" # The bigger newly repacked archive
f2 = "Resource1.pak" # The smaller second new repacked archive
folder1 = "PAK0" # PAK0 Folder
folder2 = "PAK1" # PAK1 Folder
repack1 = "FileData1.rep" # For Resource0 Repacking
repack2 = "FileData2.rep" # For  Resource1 Repacking
f1info = b'\x47\x52\x45\x53\x64\x00\x00\x00\xB5\x1C\x00\x00' # Initial pak data for Resource0
f2info = b'\x47\x52\x45\x53\x64\x00\x00\x00\x35\x00\x00\x00' # Initial pak data for Resource1

def rem(file: str): # Remove existing files
  if os.path.isfile(file):
    os.remove(file)
    print(file, " is deleted.")
    print("Beginning Task.")
    
def initarchive(filepath:str, initialinfo): # Starting the new PAK files
  with open(filepath, "wb") as start:
    start.write(initialinfo)
    
def packer(repfile: str, pakfile: str, existfolder: str, loopu: int): # Packing the new PAK files
  print("Reading rep file".format(repfile))
  with open(repfile, "r+b") as pack: # Read .rep file
    for i in range(0, loopu): # Loop
      filen = pack.read(128)
      newf = filen.decode()
      newf = newf.replace('\0', '')
      tempoff = pack.read(4)
      tempsize = pack.read(4)
      with open(pakfile, "ab") as mid: # Writing the headers
        csize = os.path.getsize(os.path.join(existfolder, newf)) # Get the current size for allowing increased file sizes
        corsize = csize.to_bytes(4, "little")
        mid.write(filen)
        mid.write(tempoff)
        mid.write(corsize)
  print("Finishing PAK Archive creation.")
  with open(repfile, "rb") as rep: # Read .rep file packing the files
    offsetu = [] # Storing updated offsets
    for i in range(0, loopu): # Loop
      filen = rep.read(128)
      fop = filen.decode()
      fop = fop.replace('\0', '')
      irrev = rep.read(8)
      with open(os.path.join(existfolder, fop), "rb") as alm: # Read the file data
        fsize = os.path.getsize(os.path.join(existfolder, fop))
        fdata = alm.read(fsize)
      with open(pakfile, "ab") as fin: # Get the current offsets to support increased file sizes and write the file data
        tempoff = fin.tell()
        coff = tempoff.to_bytes(4, "little")
        offsetu.append(coff)
        ffinal = fin.write(fdata)
      with open(pakfile, "r+b") as corr: # Correct the existing offsets for file data
        corr.seek(12)
        for newoff in offsetu:
          filename = corr.read(128)
          offset = corr.write(newoff)
          filesize = corr.read(4)
  offsetu.clear()
  print("Archive Packing is done.")
if __name__ == "__main__":
  print("Beginning first PAK Archive Creation.")
  rem(f2) # Remove existing PAK file
  initarchive(f2, f2info) # Create the PAK file
  packer(repack2, f2, folder2, 53) # Pack the PAK file

  print("Beginning second PAK Archive Creation.")
  print("The Second Archive will take longer to pack. please wait until the script is finished.")

  rem(f1) # Remove existing PAK file
  initarchive(f1, f1info) # Create the PAK file
  packer(repack1, f1, folder1, 7349) # Pack the PAK file
input("Task completed, please keep the .rep files for any future repacking.")
