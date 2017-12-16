import argparse

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument ("number")
	
	args = parser.parse_args()
	print args
	if ( args.number == "silent"):
		print "Noise"

	