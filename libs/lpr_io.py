# encoding=utf-8
# Created by wz on 18-6-11.
import json

JSON_EXT = '.json'


class LPRWriter:
    def __init__(self, foldername, filename, imgSize, databaseSrc='Unknown', localImgPath=None):
        self.foldername = foldername
        self.filename = filename
        self.databaseSrc = databaseSrc
        self.imgSize = imgSize
        self.boxlist = []
        self.localImgPath = localImgPath
        self.verified = False

    def addBndBox(self, box, label, difficult):
        box = list(map(lambda x: list(x), box))
        self.boxlist.append({'label': label, 'difficult': difficult, 'box': box})

    def save(self, targetFile):
        with open(targetFile, 'w') as f:
            json.dump({'foldername': self.foldername, 'filename': self.filename, 'imgsize': self.imgSize,
                       'localimgpath': self.localImgPath, 'verified': self.verified, 'boxlist': self.boxlist}, f)


class LPRReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.shapes = None
        self.verified = None
        self.read()

    def read(self):
        self.shapes = []
        with open(self.filepath, 'r') as f:
            obj = json.load(f)
            boxlist = obj['boxlist']
            for box in boxlist:
                self.shapes.append(
                    (box['label'], list(map(lambda x: tuple(x), box['box'])), None, None, box['difficult']))
            self.verified = obj['verified']

    def getShapes(self):
        return self.shapes
