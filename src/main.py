import OpticalFlowIterator as ofi

def main():
	optical_flows = ofi.OpticalFlowIterator()
	optical_flows.Import("../speedchallenge/data/train.mp4")
	for i in range(0,500):
		optical_flows.ComputeNextOpticalFlow()
	print("hello world!")

if __name__ == "__main__":
	main()