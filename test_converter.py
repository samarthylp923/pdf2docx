"""
Test script to verify the PDF to DOCX conversion functionality.
"""

import os
import sys
from pathlib import Path
from converter import PDFConverter, convert_pdf_to_docx
from create_test_pdf import create_test_pdf


def test_basic_conversion():
    """Test basic PDF to DOCX conversion."""
    print("Test 1: Basic conversion")
    print("-" * 50)
    
    try:
        # Create a test PDF first
        test_pdf = "test_basic.pdf"
        create_test_pdf(test_pdf)
        
        # Convert it
        result = convert_pdf_to_docx(test_pdf)
        
        # Verify output exists
        if Path(result).exists():
            print(f"✓ Success: Conversion created {result}")
            # Clean up
            os.remove(test_pdf)
            os.remove(result)
            return True
        else:
            print(f"✗ Failed: Output file not created")
            return False
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False


def test_custom_output():
    """Test conversion with custom output path."""
    print("\nTest 2: Custom output path")
    print("-" * 50)
    
    try:
        test_pdf = "test_custom.pdf"
        output_docx = "custom_output.docx"
        create_test_pdf(test_pdf)
        
        result = convert_pdf_to_docx(test_pdf, output_docx)
        
        if Path(result).exists() and result == output_docx:
            print(f"✓ Success: Custom output created at {result}")
            os.remove(test_pdf)
            os.remove(result)
            return True
        else:
            print(f"✗ Failed: Custom output not created")
            return False
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False


def test_file_not_found():
    """Test error handling for non-existent file."""
    print("\nTest 3: Error handling - File not found")
    print("-" * 50)
    
    try:
        convert_pdf_to_docx("nonexistent.pdf")
        print("✗ Failed: Should have raised FileNotFoundError")
        return False
    except FileNotFoundError as e:
        print(f"✓ Success: Correctly raised FileNotFoundError")
        return True
    except Exception as e:
        print(f"✗ Failed: Unexpected error: {e}")
        return False


def test_invalid_file_type():
    """Test error handling for invalid file type."""
    print("\nTest 4: Error handling - Invalid file type")
    print("-" * 50)
    
    try:
        # Create a text file
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write("This is not a PDF")
        
        convert_pdf_to_docx(test_file)
        print("✗ Failed: Should have raised ValueError")
        os.remove(test_file)
        return False
    except ValueError as e:
        print(f"✓ Success: Correctly raised ValueError")
        os.remove(test_file)
        return True
    except Exception as e:
        print(f"✗ Failed: Unexpected error: {e}")
        try:
            os.remove(test_file)
        except (FileNotFoundError, OSError):
            pass
        return False


def run_all_tests():
    """Run all tests."""
    print("=" * 50)
    print("PDF to DOCX Converter - Test Suite")
    print("=" * 50)
    print()
    
    tests = [
        test_basic_conversion,
        test_custom_output,
        test_file_not_found,
        test_invalid_file_type,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    print("=" * 50)
    
    return all(results)


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
