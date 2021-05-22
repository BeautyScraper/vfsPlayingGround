REM set ffmpeg="D:\Developed\Automation\Batch\ffmpeg.exe"
REM ffmpeg -i  -r 1/1 filename%03d.jpg
REM set eDir=Brittanya Razavi BuCFLgEg0EH
REM set eDir=%1
REM MD "%eDir%"
REM ffmpeg -i "valentina-nappi_002.gif" -r 1/1  "%eDir%/out-%%03d.jpg"
REM ffmpeg -i "%eDir%.mp4"  -vsync 0 "%eDir%/out-%%03d.jpg"
REM xcopy frames.bat ".\%eDir%\"
REM cd "%eDir%"
REM start "" cmd /k frames.bat
python ExtractFramesDoAll.py