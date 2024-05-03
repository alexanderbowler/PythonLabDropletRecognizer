import PostSwell_DropGelAnalysis
import Screenshot_Capture
import os

dp = 1.5
minDist = 15 
param1 = 100
param2 = 30
minRadius = 20
maxRadius = 50
channel_height = 100 #um

params = [dp, param1, param2, minRadius, maxRadius, channel_height]

Test = PostSwell_DropGelAnalysis.ImgCircleAnalysis(params,"A1")
Test.run()
