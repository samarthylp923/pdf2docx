"""
Command-line interface for PDF to DOCX conversion.
"""

import sys
import argparse
from pathlib import Path
from converter import PDFConverter


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Convert PDF files to DOCX format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.pdf                      # Convert input.pdf to input.docx
  %(prog)s input.pdf -o output.docx       # Convert with custom output name
  %(prog)s input.pdf --start 0 --end 5    # Convert only pages 0-4
  %(prog)s file1.pdf file2.pdf -d output/ # Convert multiple files to output directory
        """
    )
    
    parser.add_argument(
        'pdf_files',
        nargs='+',
        help='PDF file(s) to convert'
    )
    
    parser.add_argument(
        '-o', '--output',
        dest='output',
        help='Output DOCX file path (only for single file conversion)'
    )
    
    parser.add_argument(
        '-d', '--output-dir',
        dest='output_dir',
        help='Output directory for converted files (for batch conversion)'
    )
    
    parser.add_argument(
        '--start',
        type=int,
        default=0,
        help='Starting page number (0-indexed, default: 0)'
    )
    
    parser.add_argument(
        '--end',
        type=int,
        default=None,
        help='Ending page number (exclusive, default: all pages)'
    )
    
    args = parser.parse_args()
    
    converter = PDFConverter()
    
    try:
        if len(args.pdf_files) == 1:
            # Single file conversion
            pdf_file = args.pdf_files[0]
            output_path = args.output
            
            if args.output_dir and not args.output:
                output_path = Path(args.output_dir) / Path(pdf_file).with_suffix('.docx').name
            
            print(f"Converting: {pdf_file}")
            result = converter.convert(pdf_file, output_path, args.start, args.end)
            print(f"✓ Success! Created: {result}")
            return 0
            
        else:
            # Batch conversion
            if args.output:
                print("Warning: --output is ignored for batch conversion. Use --output-dir instead.")
            
            print(f"Converting {len(args.pdf_files)} files...")
            results = converter.convert_batch(args.pdf_files, args.output_dir)
            print(f"\n✓ Completed: {len(results)}/{len(args.pdf_files)} files converted successfully")
            return 0
            
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
