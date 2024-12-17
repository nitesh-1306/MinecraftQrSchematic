# Minecraft Schematic Generator

## Overview

This Flask application allows users to generate Minecraft schematic files from any links. The tool provides a simple web interface to convert various sources into Minecraft-compatible schematic files.

## Features

- Web-based interface for schematic generation
- Converts input to Minecraft .schematic format

## Prerequisites

- Python 3.8+
- Flask
- Pillow
- qrcode library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nitesh-1306/MinecraftQrSchematic.git
cd MinecraftQrSchematic
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
flask run
```

Navigate to `http://localhost:5000` in your web browser.
