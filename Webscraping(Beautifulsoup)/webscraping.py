from bs4 import BeautifulSoup
import requests
import urllib.request
import xlsxwriter


#Create a new Excel
workbook = xlsxwriter.Workbook("Anime.xlsx")
worksheet = workbook.add_worksheet()


req = requests.get("https://4anime.to/")
soup = BeautifulSoup(req.content,"html.parser")
#print(soup.title)
images = []
i = 1
for img in soup.findAll("div",{"id": "aroundimage"}):
    #images.append(img.find('img').get('src'))
    fullpath =  f"https://4anime.to{img.find('img').get('src')}"    
     
    path = f"{img.find('img').get('src')}"
    firstpos = path.rfind("/")
    lastpost = len(path)
    destination = f"images/{path[firstpos+1:lastpost]}"

    opener = urllib.request.build_opener()
    opener.addheaders =  [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(fullpath, destination )  

    worksheet.write_url(f"A{i}",destination) # Image information
    worksheet.insert_image(f"B{i}",destination,{'x_scale': 0.5,'y_scale': 0.5})
    i += 1
#print(images)    
workbook.close()
