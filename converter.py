"""
PDF to DOCX Converter Module

This module provides functionality to convert PDF files to DOCX format.
"""

import os
from pathlib import Path
from typing import Union, Optional
from pdf2docx import Converter


class PDFConverter:
    """A class to handle PDF to DOCX conversion."""
    
    def __init__(self):
        """Initialize the PDF converter."""
        pass
    
    def convert(
        self,
        pdf_path: Union[str, Path],
        docx_path: Optional[Union[str, Path]] = None,
        start: int = 0,
        end: Optional[int] = None
    ) -> str:
        """
        Convert a PDF file to DOCX format.
        
        Args:
            pdf_path: Path to the input PDF file
            docx_path: Path to the output DOCX file (optional, defaults to same name with .docx extension)
            start: Starting page number (0-indexed, default: 0)
            end: Ending page number (exclusive, default: None means all pages)
            
        Returns:
            str: Path to the generated DOCX file
            
        Raises:
            FileNotFoundError: If the input PDF file doesn't exist
            ValueError: If the input file is not a PDF
        """
        # Convert to Path objects
        pdf_path = Path(pdf_path)
        
        # Validate input file
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        if pdf_path.suffix.lower() != '.pdf':
            raise ValueError(f"Input file must be a PDF, got: {pdf_path.suffix}")
        
        # Determine output path
        if docx_path is None:
            docx_path = pdf_path.with_suffix('.docx')
        else:
            docx_path = Path(docx_path)
        
        # Ensure output directory exists
        docx_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Perform conversion
        cv = Converter(str(pdf_path))
        cv.convert(str(docx_path), start=start, end=end)
        cv.close()
        
        return str(docx_path)
    
    def convert_batch(
        self,
        pdf_files: list[Union[str, Path]],
        output_dir: Optional[Union[str, Path]] = None
    ) -> list[str]:
        """
        Convert multiple PDF files to DOCX format.
        
        Args:
            pdf_files: List of paths to input PDF files
            output_dir: Directory for output DOCX files (optional)
            
        Returns:
            list[str]: List of paths to the generated DOCX files
        """
        converted_files = []
        
        for pdf_file in pdf_files:
            pdf_path = Path(pdf_file)
            
            if output_dir:
                output_path = Path(output_dir) / pdf_path.with_suffix('.docx').name
            else:
                output_path = None
            
            try:
                result = self.convert(pdf_path, output_path)
                converted_files.append(result)
                print(f"✓ Converted: {pdf_file} -> {result}")
            except Exception as e:
                print(f"✗ Failed to convert {pdf_file}: {e}")
        
        return converted_files


def convert_pdf_to_docx(
    pdf_path: Union[str, Path],
    docx_path: Optional[Union[str, Path]] = None,
    start: int = 0,
    end: Optional[int] = None
) -> str:
    """
    Convenience function to convert a PDF file to DOCX format.
    
    Args:
        pdf_path: Path to the input PDF file
        docx_path: Path to the output DOCX file (optional)
        start: Starting page number (0-indexed, default: 0)
        end: Ending page number (exclusive, default: None means all pages)
        
    Returns:
        str: Path to the generated DOCX file
    """
    converter = PDFConverter()
    return converter.convert(pdf_path, docx_path, start, end)
