# ScoreSaber Curve and Reweight Tool

Tool to privately reweight scores on Beat Saber's unofficial ranking leaderboard: ScoreSaber

---

## How to use:

#### Open up `Star reweighter - full.py` in order to choose whether to reweight via player scores or leaderboard scores.
#### To edit the curve data, open `defines.py` in an IDE and edit the following values under ppCurve() -> x = percent value, y = score multiplier
#### To edit star ratings of ranked maps or give star ratings to unranked maps open up `ranked maps.txt` or create your own .txt file with the formatting listed inside the previously mentioned .txt
#### If you wish to edit the star to pp multiplier (the arbitrary number that makes pp values less linear the higher the star rating) you can do so under playerScoreGrab/leaderboardScoreGrab -> pp

## Plans:

Eventually I plan to update this to allow you to edit star ratings, give unranked maps a star rating, as well as implement some sort of per-map curve functionality

- ~~Edit ranked maps star rating~~
- ~~Give unranked maps a star rating~~
- Implement some sort of per-map curve functionality
- Allow you to edit pp curve & pp multiplier without having to physically open the python files
- Any other things I may think of or people may suggest

---

I think that's everything, I suck dick at readme's so if there's an issue dm me on discord: @potasium_ otherwise enjoy
