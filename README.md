<h1>Reniec Consult App in Python</h1>

<p>1. Clone the repo</p>

```
https://github.com/BryanGrados/python-reniec-consult-app.git
```

<p>2. Download python dependencies if you don't have it: </p>

```
pip install pyinstaller
pip install requests
pip -m install --upgrade
```

<p>3. Create the .exe</p>

```
pyinstaller --windowed --onefile --icon=./reniec.ico reniec.py
```
<p color="darkred">Warning: If you wanna change the .ico file before change the .ico name and path</p>

<p>4. Enjoy! You can find your .exe in </p>

```
..\build\app.exe
```
