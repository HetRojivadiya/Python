import requests
import argparse

def download_file(url, filename):
   if filename is None:
          filename = "het.jpg"
   
   response = requests.get(url)
   with open(filename, "wb") as f:
      f.write(response.content)
      
parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of the File Download")
parser.add_argument("Output", nargs='?', help="by which name do you want to download the file", default=None)

args = parser.parse_args()
download_file(args.url, args.Output)
print("File downloaded successfully.")

#write in terminal:
# & C:/Users/hetro/AppData/Local/Programs/Python/Python311/python.exe c:/Users/hetro/OneDrive/Desktop/Python/57_CommandLine_Utilities.py https://imagej.net/images/AuPbSn40.jpg