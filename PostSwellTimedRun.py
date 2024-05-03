import PostSwell_DropGelAnalysis
import Screenshot_Capture
import os
import time

dp = 1.5
minDist = 15 
param1 = 100
param2 = 30
minRadius = 20
maxRadius = 50
channel_height = 100 #um

params = [dp, param1, param2, minRadius, maxRadius, channel_height]

cur_img_folder = "Current_Run"

droplet_analyzer = PostSwell_DropGelAnalysis.ImgCircleAnalysis(params,cur_img_folder)
if not os.path.exists(os.path.join(os.getcwd(), cur_img_folder)):
    os.mkdir(os.path.join(os.getcwd(), cur_img_folder))


for i in range(2):
    Scrnshot = Screenshot_Capture.ScrnShot(os.getcwd()+'/'+cur_img_folder)
    Scrnshot.takeScreenshot()
    droplet_analyzer.run()
    time.sleep(5)
    file_list = os.listdir(os.path.join(os.getcwd(), cur_img_folder))
    for file in file_list:
        os.remove(os.path.join(os.getcwd(), cur_img_folder, file))
    






