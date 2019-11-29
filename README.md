# MusicSplitter
Splits big audio stream into separate tracks with provided metadata.

### How to use
Easy peasy:
1. Have Python 3+ and ffmpeg installed (ffmpeg must be invokable from termial/cmd)
2. Open `tracks.txt`.
3. Edit the file to add information you need:
```
Arist
Album
Year
NameOfBigassFileYouWantToSplit.m4a
1:15:46 (Length of file)
00:00 Track 1 title
09:37 Track 2 title
16:14 Track 3 title
23:34 Track 4 title
29:22 Track 5 title
35:00 Track 6 title
44:05 Track 7 title
50:23 Track 8 title
56:47 Track 9 title
1:58:50 Track 10 title
1:05:05 Track 11 title
1:11:50 Track 12 title
```
4. Make sure the three files are in the same directory
5. Run the python script
