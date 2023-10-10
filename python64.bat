@setlocal
@set PYTHONVER=Python310
@set PYTHONHOME=%USERPROFILE%\AppData\Local\Programs\Python\%PYTHONVER%
@set PATH=%PYTHONHOME%\Scripts;%PATH%
@"%PYTHONHOME%\python.exe" %*
