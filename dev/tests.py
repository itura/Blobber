#just testing how things look
import blob_
import game
import traceback

def test1():
	blob_list = []
	for i in range(10):
		new_blob = blob_.Blob("DEV", float(i)*1.23456, float(i)*3.52345, float(i+1)*10.0, (i*12.5,i*6.5,i*2.8))
		blob_list.append(new_blob)
	print blob_list
	print "\n"

	blob_str = game.blobsToString(blob_list)
	print blob_str
	print "\n\n"
	blob_list = game.blobsFromString(blob_str)
	print blob_list

if __name__ == "__main__":
	try:
		test1()
	except Exception, err:
		print(traceback.format_exc())
	raw_input()