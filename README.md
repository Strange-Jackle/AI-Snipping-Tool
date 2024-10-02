# Screenshot Monitor with AI Integration

This project monitors the clipboard for screenshots and uses Google's Generative AI to process the images and generate content. When a screenshot is detected, it is uploaded to the AI model, which then generates a response. A notification is displayed with the AI-generated content.

## Features

- Monitors clipboard for new screenshots.
- Converts and uploads screenshots to Google's Generative AI.
- Displays a notification with the AI-generated response.

## Requirements

- Python 3.x
- `Pillow` for image processing
- `plyer` for notifications
- `google-generativeai` for AI integration

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Strange-Jackle/AI-Snipping-Tool.git
    cd AI-Snipping-Tool
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure your Google Generative AI API key:
    ```python
    genai.configure(api_key='YOUR_API_KEY')
    ```

## Usage

1. Run the script:
    ```sh
    python helper.py
    ```

2. The script will start monitoring the clipboard for screenshots. When a screenshot is detected, it will be processed by the AI model, and a notification will be displayed with the generated content.

## Code Overview

- `show_notification(message)`: Displays a notification with the given message.
- `clipboard_contains_image()`: Checks if the clipboard contains an image.
- `process_image(image)`: Processes the image, uploads it to the AI model, and generates content.
- `monitor_clipboard()`: Monitors the clipboard for new screenshots and triggers the processing function.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Pillow](https://python-pillow.org/)
- [Plyer](https://plyer.readthedocs.io/en/latest/)
- [Google Generative AI](https://cloud.google.com/ai-platform)
