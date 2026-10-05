# Legal ML Model

A university machine learning project for working with legal documents. The project is in an early stage: right now it covers the first step of the pipeline, which is extracting plain text from PDF files so it can be used for later preprocessing and model training.

## Project structure

```
Legal-ML-Model/
├── extract_text.py   # Extracts text from a PDF into data/
├── data/
│   ├── raw/          # Put source PDFs here
│   └── *_extracted.txt  # Text output from extract_text.py
└── venv/             # Local Python virtual environment (not part of the source)
```

## Requirements

- Python 3.10 or newer
- [pdfplumber](https://github.com/jsvine/pdfplumber), which installs `pdfminer.six`, `pypdfium2` and `Pillow` as dependencies

## Setup

Create and activate a virtual environment, then install the dependency.

**Windows (PowerShell)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pdfplumber
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
pip install pdfplumber
```

If a `venv/` folder already exists, you only need to activate it.

## Usage

Pass the path to a PDF:

```bash
python extract_text.py data/raw/example.pdf
```

The script:

1. Reads each page of the PDF with `pdfplumber`.
2. Prints the first 500 characters so you can check the result.
3. Saves the full text to `data/<pdf-name>_extracted.txt`, with a `--- Page N ---` header before each page.

The output always goes to the `data/` folder next to the script, no matter which directory you run it from. If a file with the same name already exists, it is overwritten.

### Example output file

```
--- Page 1 ---
<text of page 1>

--- Page 2 ---
<text of page 2>
```

## Limitations

- Only PDFs with a text layer are supported. Scanned PDFs (images of pages) produce no text, because there is no OCR step.
- Pages with no extractable text are skipped and get no page header.
- Complex layouts such as multi-column pages and tables may come out in an unexpected reading order.

## Next steps

Planned work for the rest of the pipeline:

- Batch extraction for every PDF in `data/raw/`
- Text cleaning and preprocessing (removing headers, footers and page numbers)
- Building a labelled dataset of legal documents
- Training and evaluating a model
