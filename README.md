# TCG (Test Case Generation)

## Overview

TCG is a Streamlit application designed for generating test cases based on uploaded files or user-provided requirements. It utilizes a combination of language processing techniques and AI models to automate the test case generation process, saving time and effort for software engineers, business analysts, AI developers, and data analysts.

## Features

- **File Upload**: Users can upload files in various formats such as PDF, DOCX, or TXT, containing project requirements or summaries.
- **Requirements Input**: Alternatively, users can input their requirements directly into the application for test case generation.
- **AI-Powered Test Case Generation**: The application uses AI models, including OpenAI, to generate test cases based on the uploaded files or user-provided requirements.
- **Text Extraction**: Supports text extraction from PDFs, DOCX, TXT files, and images using OCR (Optical Character Recognition) techniques.
- **Dynamic Interface**: The Streamlit interface provides a user-friendly experience with real-time updates and interactive elements.

## Tech Stack

- **Streamlit:** Web application framework for data scientists
- **langchain:** Language processing library for text analysis and manipulation
- **PyPDF2:** PDF file manipulation library
- **docx:** Library for working with DOCX files
- **Pillow:** Python Imaging Library for image processing
- **pytesseract:** Python wrapper for Tesseract OCR engine

## Prerequisites

Before running the application, ensure you have Python installed on your system.

## Installation

To run the TCG application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/SIMRAN719/TCG.git
   cd tcg
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run main.py
   ```

## Dependencies

- **Streamlit**
- **langchain**
- **PyPDF2**
- **docx**
- **Pillow**
- **pytesseract**

## Contributing

Contributions to TCG are welcome! To contribute, please follow the guidelines in CONTRIBUTING.md.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
