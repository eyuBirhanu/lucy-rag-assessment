import fitz  # PyMuPDF
import os

def extract_and_chunk_pdf(file_path, chunk_size=800, overlap=150):
    """
    Reads a PDF, extracts text page by page, and splits it into overlapping chunks.
    Maintains the page number for citations later.
    """
    doc = fitz.open(file_path)
    chunks =[]
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text").strip()
        
        if not text:
            continue
            
        # Sliding window chunking
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]
            
            # Clean up the text slightly (remove excessive newlines)
            chunk_text = " ".join(chunk_text.split())
            
            chunks.append({
                "page": page_num + 1,  # 1-indexed for humans
                "text": chunk_text
            })
            
            start += (chunk_size - overlap)
            
    doc.close()
    return chunks