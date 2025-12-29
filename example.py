"""
Example usage of the PDF to DOCX converter.
"""

from converter import PDFConverter, convert_pdf_to_docx
from pathlib import Path


def example_basic_conversion():
    """Example: Basic PDF to DOCX conversion."""
    print("Example 1: Basic conversion")
    print("-" * 50)
    
    # Using the convenience function
    try:
        result = convert_pdf_to_docx("sample.pdf")
        print(f"✓ Converted to: {result}")
    except FileNotFoundError:
        print("Note: sample.pdf not found. This is just an example.")
    print()


def example_custom_output():
    """Example: Convert with custom output path."""
    print("Example 2: Custom output path")
    print("-" * 50)
    
    converter = PDFConverter()
    try:
        result = converter.convert("input.pdf", "output/custom_name.docx")
        print(f"✓ Converted to: {result}")
    except FileNotFoundError:
        print("Note: input.pdf not found. This is just an example.")
    print()


def example_page_range():
    """Example: Convert specific page range."""
    print("Example 3: Convert specific pages")
    print("-" * 50)
    
    try:
        # Convert only pages 0-4 (first 5 pages)
        result = convert_pdf_to_docx("document.pdf", "pages_0_to_4.docx", start=0, end=5)
        print(f"✓ Converted pages 0-4 to: {result}")
    except FileNotFoundError:
        print("Note: document.pdf not found. This is just an example.")
    print()


def example_batch_conversion():
    """Example: Convert multiple PDF files."""
    print("Example 4: Batch conversion")
    print("-" * 50)
    
    converter = PDFConverter()
    pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
    
    try:
        results = converter.convert_batch(pdf_files, output_dir="converted_files")
        print(f"✓ Converted {len(results)} files")
    except Exception as e:
        print(f"Note: PDF files not found. This is just an example.")
    print()


if __name__ == "__main__":
    print("=" * 50)
    print("PDF to DOCX Converter - Usage Examples")
    print("=" * 50)
    print()
    
    example_basic_conversion()
    example_custom_output()
    example_page_range()
    example_batch_conversion()
    
    print("=" * 50)
    print("For CLI usage, run: python cli.py --help")
    print("=" * 50)
