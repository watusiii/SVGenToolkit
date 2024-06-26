# Project Guide: Creating and Viewing SVG Art with Metadata

Welcome to your project guide! This guide will walk you through the process of generating SVG art, creating corresponding metadata files, and viewing the SVG images in a web browser. In this example project the included script generates Picoblots!

## Prerequisites

1. **Download and Install Python:**
   Ensure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).

2. **Download and Install Visual Studio Code:**
   Download and install Visual Studio Code (VS Code) from [code.visualstudio.com](https://code.visualstudio.com/).

## Step 1: Prepare Your Project Folder

1. **Create a Main Folder:**
   Create a main folder on your computer and name it `SVG_Project` (or any name you prefer).

2. **Save All Required Files in the Main Folder:**
   - Place the following files inside the `SVG_Project` folder:
     - `generate_svg.py`
     - `generate_metadata.py`
     - `index.html`

3. **Folder Structure:**
   Your `SVG_Project` folder should look like this:
   ```
   SVG_Project/
   ├── generate_svg.py
   ├── generate_metadata.py
   └── index.html
   ```

## Step 2: Generate SVG Art

### Files Required:
- `generate_svg.py`

### Instructions:

1. **Open Visual Studio Code:**
   Open Visual Studio Code.

2. **Open the Project Folder:**
   - Go to `File` > `Open Folder...`.
   - Select the `SVG_Project` folder and open it.

3. **Open the Terminal:**
   - Open the terminal in VS Code by pressing `Ctrl + ~` or by going to `View` > `Terminal`.

4. **Run the SVG Generation Script:**
   - Ensure you are in the `SVG_Project` directory in the terminal.
   - Run the script by typing:
     ```sh
     python generate_svg.py
     ```

   This script will generate 333 SVG files in a folder called `images`.

## Step 3: Create Metadata Files

### Files Required:
- `generate_metadata.py`

### Instructions:

1. **Ensure the Terminal is Open:**
   - Make sure the terminal in VS Code is open and you are in the `SVG_Project` directory.

2. **Run the Metadata Generation Script:**
   - Run the script by typing:
     ```sh
     python generate_metadata.py
     ```

   This script will create 333 JSON metadata files in a folder called `metadata`.

## Step 4: Viewing the SVG Art

### Files Required:
- `index.html`

### Instructions:

1. **Open the `index.html` File:**
   - Ensure `index.html` is in the `SVG_Project` directory.
   - Open the `index.html` file in Visual Studio Code.

2. **Open the HTML File in a Browser:**
   - You can open the `index.html` file in a web browser by right-clicking on the file in VS Code and selecting `Open with Live Server` (if you have the Live Server extension installed) or by dragging the file into your browser.

3. **What You'll See:**
   - A grid of SVG images will be displayed. The script in the `index.html` file dynamically loads and displays all 333 SVG files from the `images` folder.

### Note:
The number of images displayed is set by the total number of SVG files in the `images` folder. The script dynamically adapts to the total number of SVG files.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SVG Grid Viewer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            padding: 20px;
            width: 100%;
            max-width: 1200px;
        }

        .grid img {
            width: 100%;
            height: auto;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>

<body>
    <h1>SVG Grid Viewer</h1>
    <div class="grid" id="svgGrid"></div>

    <script>
        const folder = 'images/';
        const totalImages = 333; // Number of images

        const grid = document.getElementById('svgGrid');

        for (let i = 1; i <= totalImages; i++) {
            const img = document.createElement('img');
            img.src = `${folder}${i}.svg`;
            img.alt = `SVG Image ${i}`;
            grid.appendChild(img);
        }
    </script>
</body>

</html>
```

### Troubleshooting:
- **SVG Files Not Showing:** Ensure that the `images` folder is in the same directory as `index.html` and contains the SVG files.
- **Metadata Not Found:** Ensure the `metadata` folder is correctly created and contains the JSON files generated by `generate_metadata.py`.

With these steps, you can generate and view your SVG art along with their metadata. Enjoy creating and exploring your artwork!
