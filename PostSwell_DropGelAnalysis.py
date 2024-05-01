import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

class ImgCircleAnalysis:
   
    def __init__(self, params, CircleImgFolder):
        self.dp = params[0]
        self.param1 = params[1]
        self.param2 = params[2]
        self.radMin = params[3]
        self.radMax = params[4]
        self.imgFolder = CircleImgFolder
        self.channel_height = params[5] #um
        self.radii_data = pd.DataFrame()
   
    def FindCircles(self, imgName):
        # Read image. 
        self.img = cv2.imread(self.imgFolder+'/'+imgName, cv2.IMREAD_COLOR)
        #print(self.img.shape) 
        self.pixel_um_ratio =  self.channel_height / self.img.shape[0] #um/pixel
        grey = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY) # Convert to grayscale. 
        blurred = cv2.blur(grey,(3,3))
        # Apply Hough transform on the grey image. 
        self.detected_circles = cv2.HoughCircles(blurred,  
                    cv2.HOUGH_GRADIENT, dp = self.dp, minDist=20, param1 = self.param1, 
                param2 = self.param2, minRadius = self.radMin, maxRadius = self.radMax) #tune min/max radius first 
        
        if self.detected_circles is None or self.detected_circles.shape[1] == 0:
            raise Exception("No Circles Found: Check parameters")

        self.radii_um = self.detected_circles[0,:,2] * 2 * self.pixel_um_ratio


    def SaveCircleImgs(self, imgName, CircleImgFolderPath):
        detected_circles_int = np.uint16(np.around(self.detected_circles)) 
        #print(detected_circles_int.shape)
        for pt in detected_circles_int[0, :]:  # Draw circles that are detected. 
            a, b, r = pt[0], pt[1], pt[2] 

            # Draw the circumference of the circle. 
            cv2.circle(self.img, (a, b), r, (0, 255, 0), 2)  
        cv2.imwrite(CircleImgFolderPath+'/'+imgName[:-4]+'_Circled.jpg',self.img)

    def SaveRawData(self,imgName, RawDataFolderPath):
        #saves the data from the circle detection to a file, in a column with 2 decimal precision
        np.savetxt(RawDataFolderPath+'/'+imgName[:-4]+'_Raw_Data.txt',np.transpose(self.radii_um),fmt='%1.2f') 
        #print(imgName[:-4])
        self.radii_data[imgName[:-4]] = pd.Series(self.radii_um)

    def write_final_data_and_hist(self, analyzed_folder_path):
        self.radii_data.to_csv(analyzed_folder_path+'/'+self.imgFolder+'_All_Raw_Data', index = False)
        binsInput = list(range(0,50))
        plt.hist(self.radii_data.to_numpy().ravel(),range= [0, 150] , bins=binsInput)
        plt.savefig(analyzed_folder_path+'/'+self.imgFolder+'_Histogram')

    def IndividualHistograms(self, imgName, HistogramFolder):
        binsInput = list(range(0,50))
        plt.hist(np.transpose(self.radii_um),range= [0, 150] , bins=binsInput)
        plt.savefig(HistogramFolder+'/'+imgName[:-4]+'_Histogram')
        plt.clf()

    def run(self):
        analyzed_folder_path = os.getcwd()+'/'+self.imgFolder+'Analyzed'
        if not os.path.exists(analyzed_folder_path):
           os.mkdir(analyzed_folder_path)
        pathCircImgs = analyzed_folder_path+'/CircledImgs'
        pathRawData = analyzed_folder_path+'/RawData'
        pathHistograms = analyzed_folder_path+'/Histograms'
        if not (os.path.exists(pathCircImgs)):  
            os.mkdir(pathCircImgs)
        if not (os.path.exists(pathRawData)):  
            os.mkdir(pathRawData) 
        if not (os.path.exists(pathHistograms)):  
            os.mkdir(pathHistograms)
        folderPath = os.getcwd()+'/'+self.imgFolder
        for filename in os.listdir(folderPath):
            if(filename[0] == '.'):
                continue
            #(filename)
            self.FindCircles(filename)
            self.SaveCircleImgs(filename,pathCircImgs)
            self.SaveRawData(filename,pathRawData)
            self.IndividualHistograms(filename,pathHistograms)
        self.write_final_data_and_hist(analyzed_folder_path)


