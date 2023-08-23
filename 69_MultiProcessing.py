import multiprocessing
import requests

def downloadFile(url,filename):
    
    response = requests.get(url)
    
    with open(filename, "wb") as f:
      f.write(response.content)

if __name__ == "__main__":   
    url = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg"
    
    pros = []

    # Normal code
    # for i in range(5):
    #     downloadFile(url,f"File {i}")

    for i in range(5):
        p = multiprocessing.Process(target=downloadFile,args=[url,f"File {i}"])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
    
        

      
