# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:32:07 2017

@author: PBallant
"""

import pandas as pd

espn = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')
espn = espn[0]
espn.columns = ['RK','PLAYER','TEAM','GP','G','A','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','PP-G','PP-A','SH-G','SH-A'];
espn = espn.loc[2:,:]
espn = espn.loc[espn['PLAYER'] != 'PLAYER',:]
espn = espn.loc[espn['PLAYER'] != 'PP',:]
espn = espn.drop('RK',axis = 1)
espn.reset_index(inplace = True, drop = True)