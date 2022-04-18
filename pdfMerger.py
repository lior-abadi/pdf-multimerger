from createTitle import FolderHeader
import os
from pikepdf import Pdf
import pandas as pd


mainPath = r"./00ToMerge"               # Main path where the folders are located
singleCombOutput = r"./01EachCombined"  # Each case combined
createCover = True                 # Creates a cover for each folder showing its name.

cover = FolderHeader()
exportedList = []
imageFilesKey = "CI "

def merge_pdf(out_path: str, parent_folder: str):
    pdf = Pdf.new()
    for path, subdir, files in os.walk(parent_folder):
        for name in files:
            pathToFile = os.path.join(path, name)
            src = Pdf.open(pathToFile)
            pdf.pages.extend(src.pages)

    pdf.save(out_path)

    
print("Creating the covers and merging each case pdfs...")
for folder in os.listdir(mainPath):
        
    folderName = os.path.basename(folder)
    print(f"{folderName.upper()} being processed.")
    exportedList.append(folderName)
    
    dir = os.path.join(mainPath, folder)
    
    if createCover:
        cover.createHeader(folderName, dir)
        path, dirs, files = next(os.walk(dir))
        if (len(files) % 2 > 0):
            cover.addBlank(dir)
   
    folder = folder + "_comb.pdf"
    outputPath = os.path.join(singleCombOutput, folder)
    merge_pdf(outputPath, dir)
    
df = pd.DataFrame(exportedList)
df.to_csv(r"./02GlobalOutput/CombinedClientsList.csv")   
    
   
   
        
        


