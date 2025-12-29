# pdf2docx
PDF to DOCX converter

A simple and efficient Python tool to convert PDF files to DOCX (Microsoft Word) format.

## Features

- Convert single or multiple PDF files to DOCX format
- Support for page range selection
- Batch conversion capability
- Command-line interface for easy usage
- Python API for programmatic access

## Installation

### Using pip (after setup)

```bash
pip install -r requirements.txt
pip install -e .
```

### Manual installation

```bash
pip install pdf2docx>=0.5.6 python-docx>=0.8.11 PyMuPDF>=1.23.0
```

## Usage

### Command Line Interface

Convert a single PDF file:
```bash
python cli.py input.pdf
```

Convert with custom output name:
```bash
python cli.py input.pdf -o output.docx
```

Convert specific page range (pages 0-4):
```bash
python cli.py input.pdf --start 0 --end 5
```

Convert multiple files:
```bash
python cli.py file1.pdf file2.pdf file3.pdf -d output_directory/
```

### Python API

Basic conversion:
```python
from converter import convert_pdf_to_docx

# Convert PDF to DOCX
result = convert_pdf_to_docx("input.pdf")
print(f"Converted to: {result}")
```

Advanced usage with page range:
```python
from converter import PDFConverter

converter = PDFConverter()

# Convert specific pages (0-4)
result = converter.convert(
    "input.pdf",
    "output.docx",
    start=0,
    end=5
)
```

Batch conversion:
```python
from converter import PDFConverter

converter = PDFConverter()
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
results = converter.convert_batch(pdf_files, output_dir="converted/")
```

## Requirements

- Python 3.7+
- pdf2docx>=0.5.6
- python-docx>=0.8.11
- PyMuPDF>=1.23.0

## Examples

See `example.py` for more detailed usage examples.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
