#Refund Scam Prevention & Verification System

A comprehensive cybersecurity project that helps users verify whether a refund call, message, or payment request is legitimate or a scam. Built with Flask (Python) backend and vanilla JavaScript frontend.

## 🎯 Project Overview

This system analyzes refund requests using rule-based detection to identify common scam patterns used in India, particularly targeting e-commerce platforms like Amazon, Flipkart, Meesho, and payment apps like PhonePe, PayTM, Google Pay.

### Key Features

- ✅ **Real-time Scam Detection** - Analyzes refund requests using 10+ detection rules
- ✅ **Risk Scoring System** - Assigns risk scores (0-100) and categorizes as LOW/MEDIUM/HIGH
- ✅ **Educational Case Studies** - Real-world scam examples with analysis
- ✅ **Privacy-First Design** - No permanent data storage, all processing local
- ✅ **Instant Recommendations** - Provides immediate safety actions based on risk level
- ✅ **Mobile Responsive** - Works seamlessly on all devices

## 🔍 Detection Capabilities

The system detects:

1. **Payment Requests** - Legitimate refunds never require payment
2. **OTP Phishing** - No company asks for OTP over phone
3. **Remote Access Scams** - AnyDesk/TeamViewer installation requests
4. **QR Code Traps** - QR codes deduct money, never add
5. **Urgency Pressure** - "Act now or lose refund" tactics
6. **Invalid Contact Details** - Unverified phone numbers, UPI IDs
7. **Suspicious Language** - "Processing fee", "verification charge"
8. **Unknown Banks** - Unrecognized bank names
9. **Malicious Links** - URLs in suspicious messages
10. **Wrong Payment Scams** - Claims of mistaken transfers

## 🏗️ Technology Stack

### Backend
- **Python 3.8+** - Core language
- **Flask** - Web framework
- **JSON** - Data storage for rules and case studies
- **Rule-based Detection Engine** - Custom pattern matching system

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with CSS variables
- **Vanilla JavaScript** - No frameworks, pure JS
- **Responsive Design** - Mobile-first approach

## 📁 Project Structure

```
refund-scam-detector/
│
├── backend/
│   ├── app.py                 # Flask application
│   ├── detection_engine.py    # Scam detection logic
│   ├── requirements.txt       # Python dependencies
│   └── data/
│       ├── scam_patterns.json       # Detection rules
│       ├── legitimate_banks.json    # Indian banks list
│       └── case_studies.json        # Real scam cases
│
├── frontend/
│   ├── index.html            # Homepage
│   ├── verify.html           # Verification form
│   ├── result.html           # Analysis results
│   ├── education.html        # Educational content
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   └── js/
│       ├── verify.js        # Form handling
│       └── result.js        # Result display
│
├── README.md                 # This file
├── DISCLAIMER.md            # Legal disclaimer
├── FUTURE_SCOPE.md          # Enhancement ideas
└── .gitignore              # Git ignore rules
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/refund-scam-detector.git
cd refund-scam-detector
```

### Step 2: Set Up Backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Create Data Files

Create the following JSON files in `backend/data/` directory:

**scam_patterns.json** - Contains detection rules (provided in artifacts)
**legitimate_banks.json** - List of recognized Indian banks
**case_studies.json** - Real scam case studies (provided in artifacts)

### Step 4: Run the Application

```bash
# From backend directory
python app.py
```

The server will start on `http://localhost:5000`

### Step 5: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## 📖 How to Use

### For End Users

1. **Visit Homepage** - Learn about refund scams
2. **Go to Verify Page** - Click "Verify Refund Request"
3. **Fill the Form** with details:
   - Platform name (Amazon, Flipkart, etc.)
   - Caller's phone number
   - UPI ID or bank name (if provided)
   - Whether they asked for money or OTP
   - Description of the call/message
4. **Submit** - Get instant risk analysis
5. **Review Results** - See risk level, red flags, and recommendations
6. **Take Action** - Follow safety recommendations

### For Developers

1. **Understand Detection Engine** - Review `detection_engine.py`
2. **Customize Rules** - Edit `scam_patterns.json`
3. **Add New Patterns** - Extend the detection logic
4. **Test Thoroughly** - Use various scam scenarios
5. **Contribute** - Submit pull requests with improvements

## 🎓 Educational Use

This project is perfect for:

- **Cybersecurity Students** - Understanding threat detection
- **Computer Science Projects** - Full-stack development example
- **Awareness Campaigns** - Teaching online safety
- **Hackathons** - Base for enhanced solutions
- **Research** - Studying scam patterns

## 🔒 Security & Privacy

- ✅ **No Data Storage** - No personal information stored permanently
- ✅ **Local Processing** - All analysis done locally
- ✅ **No External APIs** - No third-party data sharing
- ✅ **Open Source** - Transparent code for review
- ✅ **Session-based** - Data cleared when session ends

## 📊 API Endpoints

### POST `/api/verify`
Analyze a refund request

**Request Body:**
```json
{
  "platform": "Amazon",
  "phone": "9876543210",
  "upi_id": "merchant@paytm",
  "bank_name": "HDFC",
  "asked_money": false,
  "asked_otp": true,
  "description": "They asked for my OTP to process refund"
}
```

**Response:**
```json
{
  "risk_score": 75,
  "risk_level": "HIGH",
  "risk_color": "#dc2626",
  "risk_message": "🚨 LIKELY SCAM - DO NOT PROCEED",
  "red_flags": [...],
  "warnings": [...],
  "recommendations": [...]
}
```

### GET `/api/case-studies`
Retrieve educational case studies

### GET `/api/stats`
Get general scam statistics

### GET `/api/health`
Health check endpoint

## 🧪 Testing

### Test Scenarios

1. **High Risk (Scam)**
   - Asked for OTP: ✓
   - Asked for money: ✓
   - Urgency language: ✓
   - Expected: Risk Score 90+

2. **Medium Risk**
   - Unknown bank name
   - Suspicious phrases
   - Invalid phone format
   - Expected: Risk Score 30-60

3. **Low Risk (Legitimate)**
   - No payment requested
   - No OTP asked
   - Standard message
   - Expected: Risk Score <30

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This is an **educational project** for cybersecurity awareness. It should not be considered as:
- Legal advice
- Professional security consultation
- Replacement for official verification channels
- Guaranteed scam detection (100% accuracy not claimed)

Always verify through official channels and report scams to:
- **National Cybercrime Helpline:** 1930
- **Online Portal:** https://cybercrime.gov.in

## 📞 Support & Resources

### Emergency Contacts
- **Cybercrime Helpline:** 1930 (24x7)
- **Online Reporting:** https://cybercrime.gov.in

### Official Resources
- Reserve Bank of India: https://www.rbi.org.in
- National Cyber Security Portal: https://nciipc.gov.in

## 🌟 Acknowledgments

- Inspired by real scam cases reported in India
- Data sources: Cybercrime reports and case studies
- Built for educational purposes to raise awareness

## 📧 Contact

For questions, suggestions, or collaboration:
- Open an issue on GitHub
- Email: shrinivasbiradar@proton.me

