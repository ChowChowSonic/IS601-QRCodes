"""Main function and driver code"""
import sys
import os
import qrcode
import time
from dotenv import load_dotenv
import logging.config
load_dotenv()

def main(data: [str]):
	"""Main function and driver code"""
	try: 
		dir = os.getenv("QR_DIR", "./qr-codes")
		logging.basicConfig(
			level=logging.DEBUG,
			format='%(asctime)s - %(levelname)s - %(message)s',
			handlers=[
            logging.StreamHandler(sys.stdout),
			logging.FileHandler('app.log', mode="a"),
        	], 
    	)
		# Ensure that the handlers are properly configured
		logging.info("Application started successfully")
		os.makedirs(dir, exist_ok=True)
		code = qrcode.QRCode(version=3, box_size=10, border=1)
		code.add_data(data[1])
		code.make()
		img = code.make_image(fill_color="BLACK", back_color="WHITE")
		logging.info("Successfully created image")
		now=time.time()
		img.save(dir+"/"+str(now)+".png", "png")
		logging.info(f"Successfully saved image to {dir+"/"+str(now)+".png"}")
	except OSError:
		logging.error(f"Failed to create directory {dir}")
	except IndexError: 
		logging.error("Please provide a url as the first argument when running this program")

if __name__ == "__main__":
	main(sys.argv) #pragma: no cov 
