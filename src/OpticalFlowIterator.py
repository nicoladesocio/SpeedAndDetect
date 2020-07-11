import cv2
import numpy as np

class OpticalFlowIterator():
	def __init__(self):
		self.images = []
		self.optical_flows = []
		self.mp4_path = ""
		self.video = None
		self.frame_no = 0

	def Import(self, mp4_path):
		self.mp4_path = mp4_path
		self.video = cv2.VideoCapture(mp4_path)
		ret, frame = self.video.read()
		# ignore the error for now
		self.images.append(frame)
		self.frame_no = self.frame_no + 1 
		return

	def ComputeNextOpticalFlow(self):
		self.video.set(1, self.frame_no)
		ret, frame = self.video.read()
		hsv = np.zeros_like(frame)
		hsv[...,1] = 255
		next = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		prvs = cv2.cvtColor(self.images[-1],cv2.COLOR_BGR2GRAY)
		flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
		mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
		hsv[...,0] = ang*180/np.pi/2
		hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
		rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
		self.images.append(frame)
		self.frame_no = self.frame_no + 1
		cv2.imwrite("./out/training_" + str(self.frame_no) + ".jpg", rgb)
		return