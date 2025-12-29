"""
Create a simple test PDF file for testing the converter.

Note: This script requires reportlab to be installed.
Install with: pip install reportlab
"""

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False


def create_test_pdf(filename="test_sample.pdf"):
    """Create a simple test PDF file."""
    if not REPORTLAB_AVAILABLE:
        raise ImportError(
            "reportlab is required to create test PDFs. "
            "Install with: pip install reportlab"
        )
    
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
    if not REPORTLAB_AVAILABLE:
        print("Note: reportlab is not installed. Skipping test PDF creation.")
        print("Install with: pip install reportlab")
    else:
        try:
            create_test_pdf()
        except Exception as e:
            print(f"Error creating test PDF: {e}")
