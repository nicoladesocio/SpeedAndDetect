import OpticalFlowIterator as ofi


def main():
	optical_flows = ofi.OpticalFlowIterator()
	optical_flows.Import("../speedchallenge/data/test.mp4")
	print("hello world!")

if __name__ == "__main__":
	main()