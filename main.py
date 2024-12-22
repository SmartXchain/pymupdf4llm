"""
    This package converts the pages of a PDF to text in Markdown format using PyMuPDF. Standard text and tables are detected, brought in the right reading sequence and then together converted to GitHub-compatible Markdown text.
"""
import pymupdf4llm

md_text = pymupdf4llm.to_markdown("AMS2406.pdf")

print(md_text)

"""
    Markdown text store as a UTF8-encoded file
"""
import pathlib

pathlib.Path("output.md").write_bytes(md_text.encode())
print("Markdown saved to output.md")

"""
    Extract only specific pages
"""
md_text_pages = pymupdf4llm.to_markdown("AMS2406.pdf", pages=[0])
print(md_text_pages)

"""
    Image Extraction
"""

md_text_images = pymupdf4llm.to_markdown(
    doc="Figure1.pdf",
    page_chunks=True,
    write_images=True,
    image_path="images",
    image_format="png",
    dpi=300
)

"""
    Chunking data and extracting it with metadata, toc_items, tables, images, graphics, text
"""

md_text_chunks = pymupdf4llm.to_markdown(
    doc="AMS2406.pdf",
    pages=[0,1],
    page_chunks=True
)
print(md_text_chunks[1])

"""
    Table Extraction - lacks details
"""
md_text_tables = pymupdf4llm.to_markdown(
    doc="AMS2406.pdf"
)
print (md_text_tables)

"""
    Detailed word-by-word extraction
"""

md_text_words = pymupdf4llm.to_markdown(
    doc="AMS2406.pdf",
    pages=[0,1],
    page_chunks=True,
    write_images=True,
    image_path="images",
    image_format="png",
    dpi=300,
    extract_words=True
)
print(md_text_words[0]['words'][:20])

"""
    Extracting Data as LLamaIndex Documents
"""
llama_reader = pymupdf4llm.LlamaMarkdownReader()
llama_docs = llama_reader.load_data("AMS2406.pdf")
print(f"Number of LlamaIndex documents: {len(llama_docs)}")
print(f"Content of first document: {llama_docs[0].text[:500]}")