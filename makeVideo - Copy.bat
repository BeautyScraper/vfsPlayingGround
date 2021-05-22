REM echo off
color a
set a="Yummy\*.jpg"
set b="video.mp4"
set c="..\ffmpeg"
set f=-c:v libx264 -pix_fmt yuv420p -r 30 -crf 20
set tmp="list.tmp"
for %%f in (%a%) do (@echo file 'file:%cd%\%%f' >> %tmp%)
%c% -y -f concat -safe 0 -i %tmp% %f% %b%
del /f /q list.tmp
