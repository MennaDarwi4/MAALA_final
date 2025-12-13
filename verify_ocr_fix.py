
import os
from PIL import Image
from agents.ocr_agent.core import OCRAgent
from dotenv import load_dotenv

# Load env for API key
load_dotenv()

def create_dummy_image(path):
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    img.save(path)
    return path

def test_ocr():
    print("Testing OCR Agent...")
    img_path = "test_image.png"
    create_dummy_image(img_path)
    
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            print("Skipping test: GROQ_API_KEY not found in .env")
            return
            
        agent = OCRAgent(api_key)
        # print(f"Agent initialized with model: {agent.llm.model_name}")
        
        result = agent.extract_text(img_path)
        result = agent.extract_text(img_path)
        with open("verify_output.txt", "w") as f:
            f.write(f"OCR Result: {result}\n")
        print("Success: Check verify_output.txt")
        
    except Exception as e:
        print(f"Failed with error: {e}")
    finally:
        if os.path.exists(img_path):
            os.remove(img_path)

if __name__ == "__main__":
    test_ocr()
