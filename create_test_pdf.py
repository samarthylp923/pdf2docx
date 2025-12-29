"""
Create a simple test PDF file for testing the converter.
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def create_test_pdf(filename="test_sample.pdf"):
    """Create a simple test PDF file."""
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Add title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(1 * inch, height - 1 * inch, "Test PDF Document")
    
    # Add some content
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.5 * inch, "This is a test PDF file for the pdf2docx converter.")
    c.drawString(1 * inch, height - 2 * inch, "It contains sample text to demonstrate the conversion functionality.")
    
    # Add a section
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 3 * inch, "Features:")
    
    c.setFont("Helvetica", 12)
    c.drawString(1.5 * inch, height - 3.5 * inch, "• Convert PDF files to DOCX format")
    c.drawString(1.5 * inch, height - 4 * inch, "• Support for page range selection")
    c.drawString(1.5 * inch, height - 4.5 * inch, "• Batch conversion capability")
    c.drawString(1.5 * inch, height - 5 * inch, "• Easy to use command-line interface")
    
    # Add page number
    c.setFont("Helvetica", 10)
    c.drawString(width / 2, 0.5 * inch, "Page 1")
    
    # Save the PDF
    c.showPage()
    c.save()
    print(f"✓ Created test PDF: {filename}")


if __name__ == "__main__":
    try:
        create_test_pdf()
    except ImportError:
        print("Note: reportlab is not installed. Skipping test PDF creation.")
        print("Install with: pip install reportlab")
