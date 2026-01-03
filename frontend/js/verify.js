/**
 * Verify Form Handler
 * Handles form submission and API communication
 */

// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Get form elements
const form = document.getElementById('verificationForm');
const submitBtn = document.getElementById('submitBtn');
const loadingState = document.getElementById('loadingState');
const errorMessage = document.getElementById('errorMessage');

// Form submission handler
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Hide error message
    errorMessage.style.display = 'none';
    
    // Get form data
    const formData = {
        platform: document.getElementById('platform').value.trim(),
        phone: document.getElementById('phone').value.trim(),
        upi_id: document.getElementById('upi_id').value.trim(),
        bank_name: document.getElementById('bank_name').value.trim(),
        asked_money: document.getElementById('asked_money').checked,
        asked_otp: document.getElementById('asked_otp').checked,
        description: document.getElementById('description').value.trim()
    };
    
    // Validate required fields
    if (!formData.platform || !formData.phone || !formData.description) {
        showError('Please fill in all required fields');
        return;
    }
    
    // Show loading state
    submitBtn.disabled = true;
    loadingState.style.display = 'block';
    
    try {
        // Send data to backend
        const response = await fetch(`${API_BASE_URL}/verify`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            throw new Error('Server error. Please try again.');
        }
        
        const result = await response.json();
        
        // Store result in sessionStorage
        sessionStorage.setItem('verificationResult', JSON.stringify(result));
        sessionStorage.setItem('verificationInput', JSON.stringify(formData));
        
        // Redirect to result page
        window.location.href = 'result.html';
        
    } catch (error) {
        console.error('Error:', error);
        showError('Unable to connect to server. Please ensure the backend is running.');
        submitBtn.disabled = false;
        loadingState.style.display = 'none';
    }
});

/**
 * Show error message
 */
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/**
 * Phone number input validation
 */
const phoneInput = document.getElementById('phone');
phoneInput.addEventListener('input', (e) => {
    // Allow only numbers, +, -, and spaces
    e.target.value = e.target.value.replace(/[^0-9+\-\s]/g, '');
});

/**
 * UPI ID input validation
 */
const upiInput = document.getElementById('upi_id');
upiInput.addEventListener('input', (e) => {
    // Convert to lowercase
    e.target.value = e.target.value.toLowerCase();
});

/**
 * Warning when critical checkboxes are checked
 */
const askedMoneyCheckbox = document.getElementById('asked_money');
const askedOtpCheckbox = document.getElementById('asked_otp');

askedMoneyCheckbox.addEventListener('change', (e) => {
    if (e.target.checked) {
        alert('⚠️ WARNING: Legitimate refunds NEVER require you to send money first. This is a MAJOR red flag for a scam!');
    }
});

askedOtpCheckbox.addEventListener('change', (e) => {
    if (e.target.checked) {
        alert('🚨 CRITICAL WARNING: Never share OTP with anyone! No company ever asks for OTP. This is likely a scam attempt!');
    }
});

/**
 * Character counter for description
 */
const descriptionTextarea = document.getElementById('description');
descriptionTextarea.addEventListener('input', (e) => {
    const length = e.target.value.length;
    const parent = e.target.parentElement;
    
    // Remove existing counter
    const existingCounter = parent.querySelector('.char-counter');
    if (existingCounter) {
        existingCounter.remove();
    }
    
    // Add counter if text exists
    if (length > 0) {
        const counter = document.createElement('small');
        counter.className = 'char-counter';
        counter.style.float = 'right';
        counter.style.color = length > 500 ? 'var(--success-color)' : 'var(--gray)';
        counter.textContent = `${length} characters`;
        parent.appendChild(counter);
    }
});