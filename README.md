# ytmd-stream-integration
Helper utility for integrating [YouTube Music Desktop App](https://ytmdesktop.app/) into all popular streaming applications like [Open Broadcaster Software (OBS)](https://obsproject.com/), [Streamlabs OBS](https://streamlabs.com/) or [XSplit](https://www.split.com/).

This utility fetches the current playing song from the remote API of [YouTube Music Desktop App](https://ytmdesktop.app/) and output the informations into various text file. THese text files can be processed by [Open Broadcaster Software (OBS)](https://obsproject.com/), [Streamlabs OBS](https://streamlabs.com/) or [XSplit](https://www.split.com/).


# Features
- Easy setup
- Automatically fetches the YouTUbe Music Desktop App API for song informations
- Stores the song informations in plain text files
- Download the album cover art and stores them locally
- Saves the song history of all played songs
- Cross platform compatible (Windows, Linux, Mac)


# Requirements
- Python 3.8, pip (Not needed if running the prebuild windows binary)
- YouTube Music Desktop App installed
- Activated remote control API inside of Youtube Music Desktop App 


# Installation

## Windows
- You can download a pre compiled binary release here
- Unpack the zip file
- Change into the newly created directory
- Check configuration config.txt and make changes if needed
- Double click the ytmd.exe

OR

- Clone this repo
- cd into this repo
- pip install -r requirements.txt
- Check the configuration file config.txt and make changes if needed
- python ytmd.py

(optional) Compiling a windows executable
- Install PyInstaller
- python -m PyInstaller --clean --onefile --add-data="config.ini;." --icon="ytmd.ico" ytmd.py
- Your binary is stored under the dist directory

## Linux / Mac
- Clone this repo
- cd into this repo
- pip install -r requirements.txt
- Check the configuration file config.txt and make changes if needed
- python ytmd.py



