# Chatbot

To create a virtual environment and install the requirements from the `requirements.txt` file, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Create a virtual environment:
    - For Windows:
      ```
      python -m venv venv
      ```
    - For macOS and Linux:
      ```
      python3 -m venv venv
      ```
4. Activate the virtual environment:
    - For Windows:
      ```
      venv\Scripts\activate
      ```
    - For macOS and Linux:
      ```
      source venv/bin/activate
      ```
5. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

Now you have successfully created a virtual environment and installed the required packages from the `requirements.txt` file.

To access the data present in the `data/` folder, you can use the following code:

```python
import os

data_folder = os.path.join(os.getcwd(), 'data')
# Use the data_folder variable to access the data files
```

Make sure that the `data/` folder is located in the same directory as your script or notebook.
