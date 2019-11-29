import subprocess


# reads tracks.txt file and passes each line into lineList
lineList = list()
with open('tracks.txt') as f:
  for line in f:
    lineList.append(line.rstrip("\n\r"))


artist = lineList[0]
album = lineList[1]
year = lineList[2]
inputFile = lineList[3]
audioLength = lineList[4]

# deleting the top 5 lines, leaving only the tracklist
del lineList[0] 
del lineList[0]
del lineList[0]
del lineList[0]
del lineList[0]



for number, line in enumerate(lineList, start=1):
  lineSplit = line.split(" ", 1)
  title = lineSplit[1]
  trackNumber = number
  fileName = str(number) + " - " + title + ".m4a" # m4a because i had trouble with ffmpeg and other formats
  timeFrom = lineSplit[0]                         # fuck it it works well enough
  if number<len(lineList):
    timeTo = (lineList[number]).split(" ", 1)[0]
  else:
    timeTo = audioLength # couldn't figure out how to get length of audio file easily
  
  # this shit's just lazy fuck it
  titleString = "title=" + title
  albumString = "album=" + album
  dateString = "date=" + str(year)
  artistString = "artist=" + artist
  trackString = "track=" + str(trackNumber)
  
  subprocess.run(["ffmpeg", "-i", inputFile, "-ss", timeFrom, "-to", timeTo, "-metadata", titleString, "-metadata", albumString, "-metadata", dateString, "-metadata", artistString, "-metadata", trackString, "-c", "copy", fileName])
  
  
