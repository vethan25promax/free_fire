# Flask Card Selection App

A Flask web application with card selection, section choice, and registration form.

## Features

- **Homepage**: 5 clickable cards with images
- **Section Selection**: Choose between Section A or B
- **Registration Form**: Collect user details with validation
- **Data Storage**: Saves to CSV file
- **Responsive Design**: Works on mobile, tablet, and desktop

## Local Development

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open http://localhost:5000 in your browser

## Deployment Options

### Option 1: Replit (Recommended)
1. Go to [replit.com](https://replit.com)
2. Click "Import from GitHub"
3. Enter your repository URL: `https://github.com/vethan25promax/free_fire.git`
4. Click "Import" and wait for setup
5. Click "Run" button to start the app
6. Share the generated URL

### Option 2: Glitch
1. Go to [glitch.com](https://glitch.com)
2. Click "New Project" → "Import from GitHub"
3. Enter your repository URL
4. Glitch will automatically install dependencies and start the app

### Option 3: PythonAnywhere
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Create a "Web" app
3. Choose "Flask" framework
4. Upload your files or import from GitHub
5. Configure WSGI file using `pythonanywhere.py` as reference

## Project Structure

```
├── app.py              # Flask application
├── requirements.txt     # Python dependencies
├── templates/
│   ├── index.html      # Homepage with cards
│   ├── select_section.html  # Section selection
│   ├── form.html       # Registration form
│   └── success.html    # Success page
└── students.csv        # Data storage (auto-created)
```

## Data Storage

User submissions are stored in `students.csv` with columns:
- Name
- Mobile Number
- Address
- Selected Card
- Section
