"""
Refund Scam Prevention & Verification System - Backend
Flask API for scam detection and verification
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from detection_engine import ScamDetectionEngine

app = Flask(__name__, static_folder='../frontend')
CORS(app)  # Enable CORS for frontend-backend communication

# Initialize detection engine
detector = ScamDetectionEngine()

@app.route('/')
def home():
    """Serve the homepage"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory(app.static_folder, path)

@app.route('/api/verify', methods=['POST'])
def verify_refund():
    """
    Main API endpoint for refund verification
    Accepts form data and returns scam analysis
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['platform', 'phone', 'description']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({
                    'error': f'Missing required field: {field}'
                }), 400
        
        # Run detection analysis
        result = detector.analyze(data)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/api/case-studies', methods=['GET'])
def get_case_studies():
    """
    Return educational case studies
    """
    try:
        with open('data/case_studies.json', 'r', encoding='utf-8') as f:
            case_studies = json.load(f)
        return jsonify(case_studies), 200
    except Exception as e:
        return jsonify({
            'error': f'Error loading case studies: {str(e)}'
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """
    Return general statistics about refund scams
    """
    stats = {
        'total_scam_types': 7,
        'helpline': '1930',
        'common_platforms': ['Amazon', 'Flipkart', 'Meesho', 'PhonePe', 'PayTM'],
        'avg_loss': '₹15,000 - ₹50,000'
    }
    return jsonify(stats), 200

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'refund-scam-detector'}), 200

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    print("=" * 60)
    print("🛡️  REFUND SCAM PREVENTION SYSTEM")
    print("=" * 60)
    print("Server running on: http://localhost:5000")
    print("Press CTRL+C to stop")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)