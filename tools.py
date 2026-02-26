## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader

## Creating custom pdf reader tool
class FinancialDocumentTool():
    @staticmethod
    def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file
        """
        
        loader = PyPDFLoader(file_path=path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content
            
            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report

## Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    def analyze_investment_tool(financial_document_data):
        """Analyze financial data for investment opportunities"""
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        processed_data = ' '.join(processed_data.split())
                
        return processed_data

## Creating Risk Assessment Tool
class RiskTool:
    @staticmethod
    def create_risk_assessment_tool(financial_document_data):        
        """Create risk assessment based on financial data"""
        return financial_document_data