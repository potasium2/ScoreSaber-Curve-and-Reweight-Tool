import math
import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from defines import playerScoreGrab, playerScoreGrabCustomStars, leaderboardScoreGrab, leaderboardScoreGrabCustomStars

print("It is advised you read 'read me.txt' before continuing.\nIf you know what you are doing then you may ignore this message.\n")
print("\nWould you like to reweight player scores or a leaderboard?\n(1 for player scores, 2 for a leaderboard)")
reweight = int(input())

print("\nWould you like to input custom star ratings, yes or no? (1 or 2)")
customSR = int(input())

if customSR == 1:
    if reweight == 1:
        print("\nPlease enter a scoresaber player ID:")
        playerId = str(input())
        print("\nWould you rather sort by top scores or recent scores? (please type \"top\" or \"recent\" (all lower case))")
        sort = str(input())
        print("\nPlease enter the page number you would like to start on:")
        startPage = int(input())
        print("\nPlease enter the page number you would like to end on.\nIt is advised you do not enter a page number greater than the number of pages a player has:")
        endPage = int(input())
        print("\nPlease enter the name of your custom ratings txt (i;e if its 'ranked maps.txt' just enter 'ranked maps')")
        rankedMaps = str(input())
        print("Running score recalculation.")
        playerScoreGrabCustomStars(playerId, sort, startPage, endPage, rankedMaps)
        print("Recalculation complete, press enter to close.")
        input()
    if reweight == 2:
        print("\nPlease enter a scoresaber leaderboard ID:")
        leaderboardId = str(input())
        print("\nPlease enter the page number you would like to start on:")
        startPage = int(input())
        print("\nPlease enter the page number you would like to end on.\nIt is advised you do not enter a page number greater than the max number of pages a leaderboard has:")
        endPage = int(input())
        print("\nPlease enter the custom star rating you would like to use for the map:")
        sr = float(input())
        print("Running score recalculation.")
        leaderboardScoreGrabCustomStars(leaderboardId, startPage, endPage, sr)
        print("Recalculation complete, press enter to close.")
        input()
    else:
        print("You did not input a proper number, please reopen and try again.")
        input()
elif customSR == 2:
    if reweight == 1:
        print("\nPlease enter a scoresaber player ID:")
        playerId = str(input())
        print("\nPlease enter the page number you would like to start on:")
        startPage = int(input())
        print("\nPlease enter the page number you would like to end on.\nIt is advised you do not enter a page number greater than the number of ranked pages a player has:")
        endPage = int(input())
        print("Running score recalculation.")
        playerScoreGrab(playerId, "top", startPage, endPage)
        print("Recalculation complete, press enter to close.")
        input()
    elif reweight == 2:
        print("\nPlease enter a scoresaber leaderboard ID:")
        leaderboardId = str(input())
        print("\nPlease enter the page number you would like to start on:")
        startPage = int(input())
        print("\nPlease enter the page number you would like to end on.\nIt is advised you do not enter a page number greater than the max number of pages a leaderboard has:")
        endPage = int(input())
        print("Running score recalculation.")
        leaderboardScoreGrab(leaderboardId, startPage, endPage)
        print("Recalculation complete, press enter to close.")
        input()
    else:
        print("You did not input a proper number, please reopen and try again.")
        input()
else:
    print("You did not input a proper number, please reopen and try again.")
    input()