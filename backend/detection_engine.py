"""
Scam Detection Engine
Rule-based system for analyzing refund requests
"""

import json
import re
import os

class ScamDetectionEngine:
    def __init__(self):
        """Initialize detection engine with rule datasets"""
        self.load_datasets()
        
    def load_datasets(self):
        """Load detection rules from JSON files"""
        data_dir = 'data'
        
        # Load scam patterns
        patterns_file = os.path.join(data_dir, 'scam_patterns.json')
        if os.path.exists(patterns_file):
            with open(patterns_file, 'r', encoding='utf-8') as f:
                self.scam_patterns = json.load(f)
        else:
            self.scam_patterns = self.get_default_patterns()
            
        # Load legitimate banks
        banks_file = os.path.join(data_dir, 'legitimate_banks.json')
        if os.path.exists(banks_file):
            with open(banks_file, 'r', encoding='utf-8') as f:
                self.legitimate_banks = json.load(f)
        else:
            self.legitimate_banks = self.get_default_banks()
    
    def get_default_patterns(self):
        """Default scam patterns if file doesn't exist"""
        return {
            "urgency_keywords": [
                "urgent", "immediately", "within 24 hours", "expire", 
                "last chance", "act now", "limited time", "hurry",
                "account will be blocked", "legal action"
            ],
            "payment_keywords": [
                "send money", "pay", "transfer", "deposit", "recharge",
                "google pay", "phonepe", "paytm", "upi", "qr code",
                "screen share", "anydesk", "teamviewer"
            ],
            "otp_keywords": [
                "otp", "one time password", "verification code", "cvv",
                "pin", "password", "share otp", "tell me otp"
            ],
            "suspicious_phrases": [
                "refund process", "verification fee", "processing charge",
                "courier charges", "gst payment", "activation fee",
                "wrong payment", "cancelled order", "bank verification"
            ]
        }
    
    def get_default_banks(self):
        """Default legitimate Indian banks"""
        return {
            "major_banks": [
                "SBI", "HDFC", "ICICI", "Axis", "Kotak", "PNB", "BOB",
                "Canara", "Union Bank", "IDBI", "Yes Bank", "IndusInd"
            ],
            "payment_platforms": [
                "Paytm Payments Bank", "Airtel Payments Bank", 
                "Jio Payments Bank", "India Post Payments Bank"
            ]
        }
    
    def analyze(self, data):
        """
        Main analysis function
        Returns risk assessment and recommendations
        """
        risk_score = 0
        red_flags = []
        warnings = []
        
        # Extract data
        platform = data.get('platform', '').strip()
        phone = data.get('phone', '').strip()
        upi_id = data.get('upi_id', '').strip()
        bank_name = data.get('bank_name', '').strip()
        asked_money = data.get('asked_money', False)
        asked_otp = data.get('asked_otp', False)
        description = data.get('description', '').lower()
        
        # Rule 1: Asked to send money for refund (MAJOR RED FLAG)
        if asked_money:
            risk_score += 40
            red_flags.append({
                'severity': 'CRITICAL',
                'flag': 'Payment Required for Refund',
                'explanation': 'Legitimate refunds NEVER require you to send money first. This is a classic scam tactic.'
            })
        
        # Rule 2: Asked for OTP (MAJOR RED FLAG)
        if asked_otp:
            risk_score += 35
            red_flags.append({
                'severity': 'CRITICAL',
                'flag': 'OTP Requested',
                'explanation': 'Never share OTP with anyone. Banks/companies never ask for OTP. This can drain your account.'
            })
        
        # Rule 3: Check for urgency language
        urgency_count = sum(1 for keyword in self.scam_patterns['urgency_keywords'] 
                           if keyword in description)
        if urgency_count >= 2:
            risk_score += 15
            red_flags.append({
                'severity': 'HIGH',
                'flag': 'Urgency Pressure',
                'explanation': f'Message contains {urgency_count} urgency keywords. Scammers create fake urgency to rush victims.'
            })
        
        # Rule 4: Check for payment-related keywords
        payment_count = sum(1 for keyword in self.scam_patterns['payment_keywords'] 
                           if keyword in description)
        if payment_count >= 2:
            risk_score += 20
            red_flags.append({
                'severity': 'HIGH',
                'flag': 'Payment Request Language',
                'explanation': 'Message contains payment/transfer keywords. Refunds are credited, not collected.'
            })
        
        # Rule 5: Check for suspicious phrases
        suspicious_count = sum(1 for phrase in self.scam_patterns['suspicious_phrases'] 
                              if phrase in description)
        if suspicious_count >= 1:
            risk_score += 10 * suspicious_count
            red_flags.append({
                'severity': 'MEDIUM',
                'flag': 'Suspicious Terminology',
                'explanation': f'Detected {suspicious_count} common scam phrases like "verification fee" or "processing charge".'
            })
        
        # Rule 6: Verify phone number format (Indian)
        if phone and not self.is_valid_indian_phone(phone):
            risk_score += 10
            warnings.append('Phone number format looks suspicious')
        
        # Rule 7: Check UPI ID validity
        if upi_id and not self.is_valid_upi(upi_id):
            risk_score += 15
            red_flags.append({
                'severity': 'MEDIUM',
                'flag': 'Invalid UPI Format',
                'explanation': 'UPI ID format appears incorrect. Verify with official platform.'
            })
        
        # Rule 8: Verify bank legitimacy
        if bank_name and not self.is_legitimate_bank(bank_name):
            risk_score += 12
            warnings.append(f'Bank name "{bank_name}" not recognized in major Indian banks list')
        
        # Rule 9: Screen sharing / remote access keywords
        if any(word in description for word in ['anydesk', 'teamviewer', 'remote', 'screen share', 'screenshare']):
            risk_score += 30
            red_flags.append({
                'severity': 'CRITICAL',
                'flag': 'Remote Access Request',
                'explanation': 'NEVER install remote access software or share screen with unknown callers. This gives complete device control.'
            })
        
        # Rule 10: Link/URL detection
        if re.search(r'http[s]?://|www\.|\.(com|in|net|org)', description):
            risk_score += 15
            red_flags.append({
                'severity': 'HIGH',
                'flag': 'Suspicious Links',
                'explanation': 'Message contains links. Do not click links from unknown sources.'
            })
        
        # Determine risk level
        if risk_score >= 60:
            risk_level = 'HIGH'
            risk_color = '#dc2626'
            risk_message = '🚨 LIKELY SCAM - DO NOT PROCEED'
        elif risk_score >= 30:
            risk_level = 'MEDIUM'
            risk_color = '#f59e0b'
            risk_message = '⚠️ SUSPICIOUS - VERIFY CAREFULLY'
        else:
            risk_level = 'LOW'
            risk_color = '#10b981'
            risk_message = '✓ Appears Safer - Still Verify'
        
        # Generate recommendations
        recommendations = self.generate_recommendations(risk_level, red_flags)
        
        # Prepare response
        return {
            'risk_score': min(risk_score, 100),
            'risk_level': risk_level,
            'risk_color': risk_color,
            'risk_message': risk_message,
            'red_flags': red_flags,
            'warnings': warnings,
            'recommendations': recommendations,
            'analysis': {
                'platform': platform,
                'phone_verified': self.is_valid_indian_phone(phone),
                'upi_verified': self.is_valid_upi(upi_id) if upi_id else None,
                'bank_recognized': self.is_legitimate_bank(bank_name) if bank_name else None
            }
        }
    
    def is_valid_indian_phone(self, phone):
        """Validate Indian phone number format"""
        # Remove spaces, dashes, and +91
        phone = re.sub(r'[\s\-+]', '', phone)
        phone = phone.replace('91', '', 1) if phone.startswith('91') else phone
        
        # Check if it's 10 digits starting with 6-9
        return bool(re.match(r'^[6-9]\d{9}$', phone))
    
    def is_valid_upi(self, upi_id):
        """Validate UPI ID format"""
        # Basic UPI format: username@bankname
        return bool(re.match(r'^[\w\.\-]+@[\w]+$', upi_id))
    
    def is_legitimate_bank(self, bank_name):
        """Check if bank name is in legitimate banks list"""
        bank_name = bank_name.upper()
        all_banks = (self.legitimate_banks['major_banks'] + 
                    self.legitimate_banks['payment_platforms'])
        
        return any(bank.upper() in bank_name or bank_name in bank.upper() 
                  for bank in all_banks)
    
    def generate_recommendations(self, risk_level, red_flags):
        """Generate safety recommendations based on risk level"""
        recommendations = []
        
        if risk_level == 'HIGH':
            recommendations = [
                {
                    'title': 'STOP ALL COMMUNICATION',
                    'actions': [
                        'Do not respond to the caller/message',
                        'Block the phone number immediately',
                        'Do not click any links or download files'
                    ]
                },
                {
                    'title': 'REPORT THE SCAM',
                    'actions': [
                        'Report to National Cybercrime Helpline: 1930',
                        'File complaint at cybercrime.gov.in',
                        'Report to your bank if you shared any info'
                    ]
                },
                {
                    'title': 'PROTECT YOUR ACCOUNT',
                    'actions': [
                        'Change passwords if you shared any credentials',
                        'Monitor bank statements for unauthorized transactions',
                        'Enable two-factor authentication on all accounts'
                    ]
                }
            ]
        elif risk_level == 'MEDIUM':
            recommendations = [
                {
                    'title': 'VERIFY INDEPENDENTLY',
                    'actions': [
                        'Contact the platform using official website/app contact',
                        'Do NOT use contact information from the suspicious message',
                        'Check your platform account for any actual refund status'
                    ]
                },
                {
                    'title': 'DO NOT SHARE',
                    'actions': [
                        'Never share OTP, CVV, or PIN',
                        'Never install remote access apps',
                        'Never send money to "receive" a refund'
                    ]
                }
            ]
        else:
            recommendations = [
                {
                    'title': 'STILL BE CAUTIOUS',
                    'actions': [
                        'Verify through official channels before proceeding',
                        'Remember: Refunds are credited, not collected',
                        'Keep records of all communication'
                    ]
                },
                {
                    'title': 'GENERAL SAFETY',
                    'actions': [
                        'Never share OTP with anyone',
                        'Check sender details carefully',
                        'Trust your instincts - if it feels wrong, it probably is'
                    ]
                }
            ]
        
        # Add critical flags as recommendations
        critical_flags = [f for f in red_flags if f['severity'] == 'CRITICAL']
        if critical_flags:
            recommendations.insert(0, {
                'title': '🚨 CRITICAL WARNINGS',
                'actions': [f['explanation'] for f in critical_flags]
            })
        
        return recommendations