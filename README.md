# Ascension-to-the-Throne
Unpacker and Repacker for Ascension To The Throne in Python. It supports unpacking of the game's archives and repacking them as well so user mods should work. I have modified the original TGA files and repacked the archives. The game loads the changes. To extract the files just double click the script. You will need Python 3 installed and have the scripts in the same directory as Resource0.pak and Resource1.pak. It will extract the files in the archives to two separate folders. The Folders are "PAK0" and "PAK1". Each folder will have the pak files set for it so Resource1.pak should go into PAK1 folder. I suggest having spare storage for the files to be extracted. Resource1.pak has 53 files in it and Resource0.pak has 7,349 files in it. When they are extracted you will find two files created that are not from the game. They are "FileData1.rep" and "FileData2.rep". They are custom files I created to be used with repacking. Repacking with these scripts requires those two .rep files in the same directory as the python scripts. I suggest keeping backups of the original pak files in case the user accidentally alters the archive incorrectly. The folders are separated because there are two separate archives. There are several kinds of files in each archive but not all of them are easily editable. The lua files are not normal ones since they have a magic of LuaQ which means you may need unluac for them but a lot of files are straightforward. The Repacker is made to support increased File Sizes. You do not need to worry about the file size changing.
They can become smaller, larger, or remain the same. The important part is
that if you modify the files they need to retain the original structure not the original size. The Unpacker and Repacker will extract and
repack correctly so long as you modify the extracted files correctly. That means if the file is compressed and you decompress it you need to
compress it back correctly. If a binary file receives a modification make sure it is done properly. File size is pretty much irrelevant with these scripts
as long as the mods you make do not alter the structure. 

The archive formats for the PAK files go like this:

Initial 12 bytes:

Magic 4

Unk 4

File Count 4

File Metadata 136 bytes each:

File Header is 136 bytes but only the filename and the last 8 bytes seem to be used.

It may be extra padding but the filenames need to stay the same.

Filename/Padding 128 bytes

Offset to File Data 4

File Size 4.

This was made by myself, LethoTC or on Discord I go by TheIllusiveFlowerTC.
A big thanks to the Lord(Christian) for blessing me with success and my mentor Medstar for helping as well.
