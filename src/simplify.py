import logging
from io import BytesIO
from PIL import Image
from ollama import generate
from typing import Optional, Union, List
# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_image_to_bytes(
    image_file: Union[str, bytes], format: str = "JPEG"
) -> Optional[bytes]:
    try:
        with Image.open(image_file) as img:
            with BytesIO() as buffer:
                img.save(buffer, format=format)
                return buffer.getvalue()
    except Exception as e:
        logging.error(f"An error occurred while converting the image: {e}")
        return None


def call_llm(prompt: str, image_bytes: bytes, model: str, ) -> Optional[List[dict]]:
    try:
        return generate(model=model, prompt=prompt, images=[image_bytes], stream=True)
    except Exception as e:
        logging.error(f"An error occurred while generating response: {e}")
        return None


def post_process_response(responses: Optional[List[dict]]) -> str:
    if responses is None:
        logging.warning("No responses received from the model.")
        return ""

    full_response = ""
    for response in responses:
        response_text = response.get("response", "")
        print(response_text, end="", flush=True)
        full_response += response_text
    return full_response


def main():
    # provide inputs
    prompt = "what is the change? summarize in few lines."
    input_image = r"data\combined.jpeg"
    # preprocess inputs
    image_bytes = convert_image_to_bytes(input_image)
    # call llm
    llm_response = call_llm(prompt, image_bytes, model="llama3.2-vision")
    # post proces response
    response = post_process_response(llm_response)
    # save response
    # print('*'*30)
    # print(response)
    # print('*'*30)
    

if __name__ == "__main__":
    main()