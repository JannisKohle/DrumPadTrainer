import os
import json


def getIndex(el, ls): # would return from 0 to len(ls)-1 <- normal index
    index = -1
    for i in ls:
        index += 1
        if i == el:
            return index

    return "element not found"

def createEx(name, rythm, replay, startBPM, bars):
    if name in listEx():
        return "AlreadyExistsError"

    if rythm not in [[4, 4], [2, 4], [8, 8], [4, 8], [16, 16], [8, 16], [3, 4], [6, 8], [12, 16]]:
        return "WrongRythmError"

    if startBPM < 15 or startBPM > 240:
        return "WrongBPMError"

    if replay > 128:
        return "WrongReplayError"

    for bar in bars:
        if len(bar) != rythm[0]:
            return f"WrongBarLenghtError({bar})"

        for note in bar:
            if type(note[0]) != dict:
                return f"WrongNoteError({bar}/{getIndex(note, bar)})"

    toWrite = {"name": name, "rythm": rythm, "replay": replay, "startBPM": startBPM, "bars": bars}

    os.chdir("data/exercises/")
    os.system(f"touch {name}.json")
    with open(f"{name}.json", "r+") as f:
        json.dump(toWrite, f)
        

def delEx(name):
    pass

def publishEx(name):
    pass

def unpublishEx(name):
    pass

def listEx():
    pass
