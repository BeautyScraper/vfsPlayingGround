REM set ffmpeg="D:\Developed\Automation\Batch\ffmpeg.exe"
REM ffmpeg -i  -r 1/1 filename%03d.jpg
set eDir=Yummy
cd %eDir%
ren *.jpg Out*
cd ..

REM MD %eDir%
REM ffmpeg -i "valentina-nappi_002.gif" -r 1/1  "%eDir%/out-%%03d.jpg"
REM ffmpeg  -pattern_type glob -i "%eDir%/*.jpg" -c:v libx264 -pix_fmt yuv420p output.mp4
..\ffmpeg -r 20 -f image2 -i "%eDir%/Out-%%04d.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p Humped.mp4