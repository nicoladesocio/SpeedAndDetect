import cv2

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
		self.images.append(frame)
		self.frame_no = self.frame_no + 1
		cv2.imshow('frame',frame)
		cv2.waitKey(200)
		return