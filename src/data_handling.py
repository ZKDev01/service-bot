from typing import Any
import aspose.pdf as ap 
import aspose.pydrawing as drawing
from docling.document_converter import DocumentConverter

def convert_to_markdown(source:str,path_to_export:str) -> bool:
  converter = DocumentConverter()
  result = converter.convert(source=source)
  with open(path_to_export,'w',encoding='utf-8') as file:
    file.write(result.document.export_to_markdown())
  return True
  
def extract_image(source:str) -> None:
  document = ap.Document(source)
  counter = 1
  img_name = "image_{counter}.jpg"
  for page in document.pages:
    for image in page.resources.images:
      with open(img_name.format(counter=counter), "wb") as img_file:
        image.save(img_file, drawing.imaging.ImageFormat.jpeg)
        counter += 1

