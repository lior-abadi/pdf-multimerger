from createTitle import FolderHeader
import os
from pikepdf import Pdf

output = r"./02GlobalOutput"
title = "Output1.pdf"
eachCasePath = r"./01EachCombined"  # Each case combined
createCover = False                 # Creates a cover for each folder showing its name.

cover = FolderHeader()

def merge_pdf(out_path: str, parent_folder: str):
    pdf = Pdf.new()
    for path, subdir, files in os.walk(parent_folder):
        for name in files:
            print(f"Merging {name}")
            pathToFile = os.path.join(path, name)
            src = Pdf.open(pathToFile)
            pdf.pages.extend(src.pages)

    pdf.save(out_path)
    

dir = os.path.join(eachCasePath)

outputMergePath = os.path.join(output, title)
merge_pdf(outputMergePath, dir)
    
    
   
   
        
        


