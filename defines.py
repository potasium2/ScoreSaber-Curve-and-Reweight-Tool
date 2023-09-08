import math
import requests
import json
import numpy as np
import matplotlib.pyplot as plt

# define curve so it can be called later when needed
def ppCurve():
    global x, y
    x = np.array([2, 1, 0.999, 0.9975, 0.995, 0.9925, 0.99, 0.9875, 0.985, 0.9825, 0.98, 0.9775, 0.975, 0.9725, 0.97, 0.965, 0.96, 0.955, 0.95, 0.94, 0.93, 0.92, 0.91, 0.9, 0.875, 0.85, 0.825, 0.8, 
                0.75, 0.7, 0.65, 0.6, 0.5, 0.4, 0.25, 0.1, 0][::-1])
    y = np.array([1000, 9, 7, 4.9871, 3.4482, 2.9713, 2.4056, 2.102, 1.853, 1.69, 1.535, 1.435, 1.37, 1.32, 1.27, 1.2, 1.13, 1.06, 1, 0.94, 0.905, 0.86, 0.84, 0.805, 0.765, 0.725, 0.695, 0.65, 
                0.59, 0.5, 0.4, 0.25, 0.18, 0.1, 0.01, 0.001, 0][::-1])

def playerScoreGrab(player, sort, page, endPage):
    
    maps = {}
    
    clearPScores = open(f"{player}.txt", "w")
    clearPScores.write("")
    
    while page <= endPage: # how many pages you want to look through
        scoresCheck = requests.get(f"https://scoresaber.com/api/player/{player}/scores?sort={sort}&page={page}")
        scores = scoresCheck.json()
        for i in scores["playerScores"]: # checks under "playerScores" in the scoresCheck request thanks to scoresabers special formatting
            baseScore = i["score"] ["baseScore"]
            songName = i["leaderboard"] ["songName"]
            maxScore = i["leaderboard"] ["maxScore"]
            mapper = i["leaderboard"] ["levelAuthorName"]
            difficulty = i["leaderboard"] ["difficulty"] ["difficulty"]
            sr = i["leaderboard"] ["stars"]
            
            if difficulty == 9:
                diffLabel = "ExpertPlus"
            elif difficulty == 7:
                diffLabel = "Expert"
            elif difficulty == 5:
                diffLabel = "Hard"
            elif difficulty == 3:
                diffLabel = "Normal"
            elif difficulty == 1:
                diffLabel = "Easy"
            
            percent = baseScore/maxScore
                
            if sr == 0: # checks to see if the map is ranked
                continue
            elif max == 0: # checks to see if the map data is even available, just a fail safe incase you go above the # of played ranked maps
                continue
                
            ppCurve() # get pp curve
            pp = (round(np.interp(percent, x, y) * (sr * 42.11353187445), 2)) # apply pp curve
                
            maps[f"{songName} {diffLabel} mapped by {mapper}"] = {"star rating": sr, "percent": round(percent * 100, 2), "pp": round(pp, 2)} # saves the maps to a list which can be sorted later via black magic
        
        print(f"current page: {page}")
        page += 1
        
    # maps get sorted here
    maps = sorted(maps.items(), key=lambda x: x[1]["pp"], reverse=True)
    maps = dict(maps)
    export = open(f"{player}.txt", "a", encoding="utf-8")
    for name, data in maps.items():
        export.write(f"{name}, {data['star rating']}, {data['percent']}, {data['pp']}\n")
    
def leaderboardScoreGrab(leaderboardId, page, endPage):
    
    players = {}
    
    leaderboardMaxScore = requests.get(f"https://scoresaber.com/api/leaderboard/by-id/{leaderboardId}/info") # get all general map info
    maxScore = leaderboardMaxScore.json()
    songName = maxScore["songName"]
    artist = maxScore["songAuthorName"]
    mapper = maxScore["levelAuthorName"]
    max = maxScore["maxScore"]
    sr = maxScore["stars"]
    
    clearLScores = open(f"{songName} by {artist} mapped by {mapper}.txt", "w")
    clearLScores.write("")
    
    while page <= endPage: # how many pages you want to look through
        leaderboardScores = requests.get(f"https://scoresaber.com/api/leaderboard/by-id/{leaderboardId}/scores?page={page}")
        scores = leaderboardScores.json()
        for i in scores["scores"]: # checks under "leaderboardScores" in the scores request thanks to scoresabers special formatting
            playerName = i["leaderboardPlayerInfo"] ["name"]
            base = i["baseScore"]
            modifier = i["modifiers"]
            
            if max == 0: # checks if map is up on beatsaver
                continue
            
            percent = base/max
            
            ppCurve() # get pp curve
            pp = (round(np.interp(percent, x, y) * (sr * 42.11353187445), 2)) # apply pp curve
            
            players[playerName] = {"star rating": sr, "percent": round(percent * 100, 2), "pp": round(pp, 2)} # saves the maps to a list which can be sorted later via black magic
        
        print(f"current page: {page}")
        page += 1
        
    # maps get sorted here
    players = sorted(players.items(), key=lambda x: x[1]["pp"], reverse=True)
    players = dict(players)
    export = open(f"{songName} by {artist} mapped by {mapper}.txt", "a", encoding="utf-8")
    for name, data in players.items():
        export.write(f"{name}, {data['star rating']}, {data['percent']}, {data['pp']}\n")