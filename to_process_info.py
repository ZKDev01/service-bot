import os
from src.data_handling import convert_to_markdown


def process_pdfs_to_markdown(source_dir: str, output_dir: str) -> None:
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  for filename in os.listdir(source_dir):
    if filename.endswith(".pdf"):
      source_path = os.path.join(source_dir, filename)
      output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.md")
      try:
        convert_to_markdown(source=source_path, path_to_export=output_path)
        print(f"Converted {filename} to Markdown.")
      except Exception as e:
        print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
  source_directory = "data\\documents"
  output_directory = "data\\markdown"
  process_pdfs_to_markdown(source_directory, output_directory)

