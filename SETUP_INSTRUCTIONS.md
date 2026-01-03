# 🚀 Complete Setup Instructions

## Step-by-Step Guide to Run Locally

### Prerequisites Check

Before starting, ensure you have:
- ✅ **Python 3.8 or higher** installed
- ✅ **pip** (Python package manager)
- ✅ **Modern web browser** (Chrome, Firefox, Safari, Edge)
- ✅ **Text editor** (VS Code, Sublime, Atom) - Optional but recommended
- ✅ **Git** (for cloning repository) - Optional

---

## 🔧 Installation Steps

### Step 1: Download the Project

#### Option A: Using Git (Recommended)
```bash
git clone https://github.com/yourusername/refund-scam-detector.git
cd refund-scam-detector
```

#### Option B: Download ZIP
1. Download the ZIP file from GitHub
2. Extract to a folder
3. Open terminal/command prompt in that folder

---

### Step 2: Set Up the Backend

#### 2.1 Navigate to Backend Directory
```bash
cd backend
```

#### 2.2 Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt.

#### 2.3 Install Python Dependencies
```bash
pip install -r requirements.txt
```

Expected output:
```
Successfully installed Flask-3.0.0 Flask-CORS-4.0.0 Werkzeug-3.0.1
```

#### 2.4 Create Data Directory and Files

Create the `data` directory if it doesn't exist:
```bash
mkdir data
```

**Create these files in `backend/data/` directory:**

1. **scam_patterns.json**
   - Copy the content from artifacts
   - Contains detection rules

2. **legitimate_banks.json**
   - Copy the content from artifacts
   - List of recognized banks

3. **case_studies.json**
   - Copy the content from artifacts
   - Real scam examples

---

### Step 3: Verify Project Structure

Your project should look like this:

```
refund-scam-detector/
│
├── backend/
│   ├── app.py                 ✓
│   ├── detection_engine.py    ✓
│   ├── requirements.txt       ✓
│   └── data/
│       ├── scam_patterns.json      ✓
│       ├── legitimate_banks.json   ✓
│       └── case_studies.json       ✓
│
├── frontend/
│   ├── index.html            ✓
│   ├── verify.html           ✓
│   ├── result.html           ✓
│   ├── education.html        ✓
│   ├── css/
│   │   └── style.css        ✓
│   └── js/
│       ├── verify.js        ✓
│       └── result.js        ✓
│
├── README.md                 ✓
├── DISCLAIMER.md            ✓
├── FUTURE_SCOPE.md          ✓
└── .gitignore              ✓
```

---

### Step 4: Run the Application

#### 4.1 Start the Backend Server

From the `backend` directory with virtual environment activated:
```bash
python app.py
```

**Expected output:**
```
============================================================
🛡️  REFUND SCAM PREVENTION SYSTEM
============================================================
Server running on: http://localhost:5000
Press CTRL+C to stop
============================================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

#### 4.2 Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

You should see the homepage of the Refund Scam Detector!

---

## 🎯 Testing the Application

### Test Case 1: High-Risk Scam

1. Go to "Verify Refund" page
2. Fill in:
   - Platform: Amazon
   - Phone: 9876543210
   - Check "Asked to send money": ✓
   - Check "Asked for OTP": ✓
   - Description: "They asked me to install AnyDesk and share my OTP to receive refund urgently"
3. Click "Analyze Risk Level"
4. Expected: **HIGH RISK** (90+ score)

### Test Case 2: Medium-Risk

1. Platform: Flipkart
2. Phone: 1234567890
3. UPI ID: unknown@xyz
4. Bank: Unknown Bank
5. Description: "Processing fee required for refund"
6. Expected: **MEDIUM RISK** (30-60 score)

### Test Case 3: Low-Risk

1. Platform: Amazon
2. Phone: 9876543210
3. Description: "Order cancelled, refund will be processed"
4. Expected: **LOW RISK** (<30 score)

---

## 🐛 Troubleshooting

### Problem 1: Python Not Found
**Error:** `'python' is not recognized...`

**Solution:**
- Install Python from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"
- Restart terminal after installation

### Problem 2: Module Not Found
**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### Problem 3: Port Already in Use
**Error:** `Address already in use`

**Solution:**
```bash
# Option 1: Kill process using port 5000 (Windows)
netstat -ano | findstr :5000
taskkill /PID <process_id> /F

# Option 2: Use different port
# Edit app.py, change:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Problem 4: CORS Errors
**Error:** `Access to fetch... has been blocked by CORS policy`

**Solution:**
- Ensure Flask-CORS is installed
- Check that CORS(app) is in app.py
- Access via http://localhost:5000, not file:///

### Problem 5: 404 Errors
**Error:** Pages not loading

**Solution:**
- Ensure you're accessing http://localhost:5000
- Check that frontend folder is in correct location
- Verify app.py has correct static_folder path

### Problem 6: JSON Files Not Found
**Error:** `FileNotFoundError: [Errno 2] No such file or directory: 'data/scam_patterns.json'`

**Solution:**
```bash
# Create data directory
cd backend
mkdir data

# Add JSON files to data directory
# Copy content from artifacts
```

---

## 💻 IDE Setup (Optional)

### Visual Studio Code

1. Install Python extension
2. Open project folder
3. Select Python interpreter (venv)
4. Use integrated terminal

**Recommended Extensions:**
- Python
- Pylance
- HTML CSS Support
- JavaScript (ES6) code snippets

### PyCharm

1. Open project
2. Configure Python interpreter (venv)
3. Mark 'frontend' as resource root
4. Run configuration: Python → app.py

---

## 🔄 Stopping the Server

To stop the Flask server:
- Press `CTRL + C` in the terminal
- Wait for graceful shutdown message

To deactivate virtual environment:
```bash
deactivate
```

---

## 🌐 Accessing from Other Devices

### Same Network Access

1. Find your computer's local IP:

**Windows:**
```bash
ipconfig
# Look for IPv4 Address (e.g., 192.168.1.100)
```

**macOS/Linux:**
```bash
ifconfig
# Look for inet address
```

2. Edit app.py to bind to all interfaces (already done):
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

3. Access from other device:
```
http://192.168.1.100:5000
```

---

## 📦 Production Deployment (Advanced)

### Using Gunicorn (Linux/macOS)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Waitress (Windows)

```bash
pip install waitress
waitress-serve --port=5000 app:app
```

### Environment Variables

Create `.env` file:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

---

## 🧪 Development Mode

### Enable Debug Mode
Already enabled in app.py:
```python
app.run(debug=True)
```

### Auto-reload on Changes
Flask debug mode automatically reloads on code changes.

### View Logs
All logs appear in the terminal where Flask is running.

---

## 📊 Project Verification Checklist

Before submission, verify:

- [ ] All files present in correct structure
- [ ] Backend starts without errors
- [ ] Frontend loads on http://localhost:5000
- [ ] Verification form works
- [ ] Results page displays correctly
- [ ] Education page loads case studies
- [ ] No console errors in browser
- [ ] All links functional
- [ ] Mobile responsive (test in browser)
- [ ] README.md complete
- [ ] DISCLAIMER.md present
- [ ] FUTURE_SCOPE.md present

---

## 🎓 For College Submission

### Documentation to Include

1. **README.md** - Project overview
2. **DISCLAIMER.md** - Legal disclaimer
3. **FUTURE_SCOPE.md** - Enhancement ideas
4. **This file** - Setup instructions
5. **Screenshots** - Include in `/docs/screenshots/`
6. **Demo Video** - 2-3 minute walkthrough
7. **Presentation** - PowerPoint/PDF

### Recommended Screenshots

- Homepage
- Verification form (filled)
- High-risk result
- Low-risk result
- Education page with case studies
- Mobile view

---

## 🤝 Getting Help

### Documentation
- Read README.md thoroughly
- Check DISCLAIMER.md for limitations
- Review FUTURE_SCOPE.md for ideas

### Debugging
- Check terminal for error messages
- Use browser console (F12)
- Verify all files are present
- Ensure correct directory structure

### Community
- Open GitHub issue
- Check existing issues for solutions
- Ask in project discussions

---

## 🎉 Success Indicators

You've successfully set up the project when:
✅ Server starts without errors  
✅ Homepage loads with all styles  
✅ Form submission works  
✅ Results display correctly  
✅ No browser console errors  
✅ Case studies load on education page  

---

## 📝 Next Steps

1. **Test thoroughly** with different scenarios
2. **Customize** detection rules for your use case
3. **Add features** from FUTURE_SCOPE.md
4. **Document** your changes
5. **Present** your project confidently

---

**Congratulations! Your Refund Scam Detector is now running! 🎉**

For questions or issues, refer to the main README.md or open a GitHub issue.

🛡️ Happy Scam Detection!