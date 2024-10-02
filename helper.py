import time
from PIL import ImageGrab
from plyer import notification
import google.generativeai as genai

genai.configure(api_key='ENTER_YOUR_API_KEY')

def show_notification(message):
    notification.notify(
        title="Screenshot Captured",
        message=message,
        app_name="Snipping Tool",
        timeout=5  # Show notification for 5 seconds
    )

def clipboard_contains_image():
    try:
        img = ImageGrab.grabclipboard()
        if img is not None:
            return True
        return False
    except Exception as e:
        return False
    
def process_image(image):
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    temp_image_path = "temp_screenshot.jpg"
    image.save(temp_image_path)

    myfile = genai.upload_file(temp_image_path)

    model = genai.GenerativeModel("gemini-1.5-pro")
    result = model.generate_content(
        [myfile, "\n\n", "Solve the Question and only give the correct option as answer nothing else"]
    )
    
    return result.text

def monitor_clipboard():
    previous_clipboard_state = None
    
    while True:
        current_clipboard_image = ImageGrab.grabclipboard()
        
        if current_clipboard_image is not None and current_clipboard_image != previous_clipboard_state:
            previous_clipboard_state = current_clipboard_image
            
            result_text = process_image(current_clipboard_image)
            
            show_notification(result_text)
            
        time.sleep(1)
           
if __name__ == "__main__":
    print("Monitoring clipboard for screenshots...")
    monitor_clipboard()

