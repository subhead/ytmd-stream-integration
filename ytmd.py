#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import configparser
from time import sleep
from datetime import datetime

class ytmd:

	def __init__(self):
		config = configparser.ConfigParser()
		config.read(os.path.join(os.getcwd(), 'config.ini'))
		self.ytmdApiUrl = config.get('app', 'ytmdApiUrl').strip("'")
		self.outputPattern = config.get('app', 'outputPattern').strip("'")
		self.timePattern = config.get('app', 'timePattern').strip("'")
		self.coverWidth = config.get('app', 'coverWidth').strip("'")
		self.coverHeight = config.get('app', 'coverHeight').strip("'")
		self.titleFilePath = config.get('app', 'titleFilePath').strip("'")
		self.authorFilePath = config.get('app', 'authorFilePath').strip("'")
		self.albumFilePath = config.get('app', 'albumFilePath').strip("'")
		self.historyFilePath = config.get('app', 'historyFilePath').strip("'")
		self.coverFilePath = config.get('app', 'coverFilePath').strip("'")
		self.pollInterval = int(config.get('app', 'pollInterval').strip("'"))
		self.saveHistory = config.get('app', 'saveHistory').strip("'")		
		self.lastPlayedTrack = {'author': '', 'title': '', 'album': '', 'cover': ''}

	def currentTrack(self):
		r = requests.get(self.ytmdApiUrl, verify=False).json()
		self.currentPlayedTrack = {
			'author': r['track']['author'],
			'title': r['track']['title'],
			'album': r['track']['album'],
			'cover': r['track']['cover'],
			'timePlayed': datetime.now().strftime(self.timePattern)
		}

		self.hasTrackChanged()

		return self.currentPlayedTrack


	def hasTrackChanged(self):
		if not self.lastPlayedTrack['title'] == self.currentPlayedTrack['title']:
			self.lastPlayedTrack = {
				'author': self.currentPlayedTrack['author'],
				'title': self.currentPlayedTrack['title'],
				'album': self.currentPlayedTrack['album'],
				'cover': self.currentPlayedTrack['cover'],
				'timePlayed': self.currentPlayedTrack['timePlayed'],
				'hasChanged': True
			}


	def downloadCover(self, coverUrl):
		c = requests.get(coverUrl, allow_redirects=True)
		
		with open(os.path.join(os.getcwd(), self.coverFilePath), 'wb') as coverFile:
			coverFile.write(c.content)


	def writeTrackToFile(self, file, currentTrack):
		with open(os.path.join(os.getcwd(), self.titleFilePath), 'w+') as currentTitleFile:
			currentTitleFile.write(self.currentPlayedTrack['title']+'\n')
		with open(os.path.join(os.getcwd(), self.authorFilePath), 'w+') as currentAuthorFile:
			currentAuthorFile.write(self.currentPlayedTrack['author']+'\n')
		with open(os.path.join(os.getcwd(), self.albumFilePath), 'w+') as currentAlbumFile:
			currentAlbumFile.write(self.currentPlayedTrack['album']+'\n')

		if self.saveHistory:
			with open(os.path.join(os.getcwd(), self.historyFilePath), 'a+') as historyFile:
				if not self.lastPlayedTrack['author']: self.lastPlayedTrack['author'] = 'unknown'
				if not self.lastPlayedTrack['title']: self.lastPlayedTrack['title'] = 'unknown'
				if not self.lastPlayedTrack['album']: self.lastPlayedTrack['album'] = 'unknown'
				historyFile.write(f"[{self.lastPlayedTrack['timePlayed']}] {self.lastPlayedTrack['author']} - {self.lastPlayedTrack['title']} - {self.lastPlayedTrack['album']} \n")


	def run(self):
		track = ytm.currentTrack()

		if self.lastPlayedTrack['hasChanged']:
			self.lastPlayedTrack['hasChanged'] = False
			ytm.writeTrackToFile(self.titleFilePath ,track)
			ytm.downloadCover(self.currentPlayedTrack['cover'])
			print(f"[{self.lastPlayedTrack['timePlayed']}] {self.lastPlayedTrack['author']} {self.lastPlayedTrack['title']} {self.lastPlayedTrack['album']} \r")
		
		sleep(self.pollInterval)



if __name__ == '__main__':
	ytm = ytmd()
	while True:	
		ytm.run()
	