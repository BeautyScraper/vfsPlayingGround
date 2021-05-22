REM echo off
color a
set a="Yummy\*.jpg"
set b="video.mp4"
set c="D:\Developed\VFS\RandyVideo\ffmpeg.exe"
set f=-c:v libx264 -pix_fmt yuv420p -r 30 -crf 20
set tmp="list.tmp"
%c% -y -f concat -safe 0 -i %tmp% %f% %b%
del /f /q list.tmp
