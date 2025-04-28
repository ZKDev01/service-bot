import os
import streamlit as st 


def get_info_by_header(content,h) -> str:
  results = ""
  lines = content.splitlines()
  inside = False

  for line in lines:
    if line.startswith("#") and h in line.lower():
      inside = True
      continue
    if inside:
      if line.startswith("#"): break
      results += line + "\n"

  content = results.strip() if results else f"No {h} section found."
  return content



markdown_dir = "data/markdown"
markdown_files = [f for f in os.listdir(markdown_dir) if f.endswith(".md")]

selected_file = st.selectbox("Select a markdown file", markdown_files)

if st.button("Show Content"):
  file_path = os.path.join(markdown_dir, selected_file)
  with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
  
  with st.expander("Show Markdown Content"):
    st.markdown(content)
  
  content_abstract = get_info_by_header(content=content,h="abstract")
  content_references = get_info_by_header(content=content,h="references")
  st.markdown(f"""
  ## Abstract
  
  {content_abstract}
  
  ## References 
  
  {content_references}
  """)

