# src/main.py

from langgraph_system.langgraph_app import LangGraphApp

LANGCHAIN_TRACING_V2=True
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="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"
LANGCHAIN_PROJECT="ALIA-PAL"

def main():
    langgraph_app = LangGraphApp()
    student_id = 'student_123'  # Example student ID
    langgraph_app.run(student_id)

if __name__ == "__main__":
    main()
