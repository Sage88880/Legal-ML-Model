import pdfplumber
import sys
import os

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' not found.")
        return None

    extracted_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    extracted_text += f"--- Page {i+1} ---\n"
                    extracted_text += page_text + "\n\n"
        return extracted_text
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_text.py <path_to_pdf>")
        sys.exit(1)
        
    pdf_file_path = sys.argv[1]
    print(f"Extracting text from: {pdf_file_path}")
    text = extract_text_from_pdf(pdf_file_path)
    
    if text:
        print("Extraction successful. First 500 characters:")
        print("-" * 40)
        print(text[:500])
        print("-" * 40)
        
        # Save to a text file in the same directory as the script
        output_name = os.path.splitext(os.path.basename(pdf_file_path))[0] + "_extracted.txt"
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", output_name)
        
        # Ensure data dir exists when saving
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Saved extracted text to: {output_path}")
