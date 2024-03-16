# Twokinds scraper

This is a pthon script that scrapes the website https://twokinds.keenspot.com.

It downloads the comic into the `comic` directory (by default).

## How to use

Download all the requirements

```
pip3 install -r requirements.txt
```

Edit main.py to set which pages you want to scrape:

```python
start_page = 1
end_page = 1228
```

And edit the download path if you want:

```python
download_path = "comic/" # Do not forget the last "/"
```

Run the main script

```
python3 main.py
```

## Compatibility

Works on MacOS (tested)

Works on Linux, though packages need to be installed through your distro's package manager. For example on Fedora:
```
sudo dnf install python3-beautifulsoup4
sudo dnf install python3-lxml
sudo dnf install python3-certifi
```

Never tested on Windows