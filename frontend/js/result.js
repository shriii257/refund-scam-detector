/**
 * Result Page Handler
 * Displays analysis results from backend
 */

// Load and display results on page load
document.addEventListener('DOMContentLoaded', () => {
    // Get data from sessionStorage
    const resultData = sessionStorage.getItem('verificationResult');
    const inputData = sessionStorage.getItem('verificationInput');
    
    if (!resultData) {
        // No data found, redirect to verify page
        window.location.href = 'verify.html';
        return;
    }
    
    try {
        const result = JSON.parse(resultData);
        const input = JSON.parse(inputData);
        
        displayResults(result, input);
    } catch (error) {
        console.error('Error parsing results:', error);
        document.getElementById('riskMessage').textContent = 'Error loading results';
    }
});

/**
 * Display all results
 */
function displayResults(result, input) {
    // Display risk banner
    displayRiskBanner(result);
    
    // Display analysis summary
    displaySummary(result, input);
    
    // Display red flags
    displayRedFlags(result.red_flags);
    
    // Display warnings if any
    if (result.warnings && result.warnings.length > 0) {
        displayWarnings(result.warnings);
    }
    
    // Display recommendations
    displayRecommendations(result.recommendations);
}

/**
 * Display risk banner
 */
function displayRiskBanner(result) {
    const banner = document.getElementById('riskBanner');
    const scoreElement = document.getElementById('riskScore');
    const messageElement = document.getElementById('riskMessage');
    const levelElement = document.getElementById('riskLevel');
    
    // Set background color
    banner.style.backgroundColor = result.risk_color;
    
    // Set content
    scoreElement.textContent = `${result.risk_score}/100`;
    messageElement.textContent = result.risk_message;
    levelElement.textContent = `Risk Level: ${result.risk_level}`;
}

/**
 * Display analysis summary
 */
function displaySummary(result, input) {
    const summaryContent = document.getElementById('summaryContent');
    
    const html = `
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong>Platform:</strong><br>
                ${escapeHtml(input.platform)}
            </div>
            <div>
                <strong>Phone Verified:</strong><br>
                ${result.analysis.phone_verified ? '✓ Valid Format' : '✗ Invalid Format'}
            </div>
            ${input.upi_id ? `
            <div>
                <strong>UPI Verified:</strong><br>
                ${result.analysis.upi_verified ? '✓ Valid Format' : '✗ Invalid Format'}
            </div>
            ` : ''}
            ${input.bank_name ? `
            <div>
                <strong>Bank Recognized:</strong><br>
                ${result.analysis.bank_recognized ? '✓ Known Bank' : '⚠ Unknown Bank'}
            </div>
            ` : ''}
        </div>
        <div style="margin-top: 1.5rem; padding: 1rem; background: var(--light); border-radius: 8px;">
            <strong>Critical Indicators:</strong><br>
            <span style="color: ${input.asked_money ? 'var(--danger-color)' : 'var(--success-color)'};">
                ${input.asked_money ? '⚠ Asked to send money' : '✓ No payment requested'}
            </span><br>
            <span style="color: ${input.asked_otp ? 'var(--danger-color)' : 'var(--success-color)'};">
                ${input.asked_otp ? '⚠ Asked for OTP' : '✓ No OTP requested'}
            </span>
        </div>
    `;
    
    summaryContent.innerHTML = html;
}

/**
 * Display red flags
 */
function displayRedFlags(redFlags) {
    const content = document.getElementById('redFlagsContent');
    
    if (!redFlags || redFlags.length === 0) {
        content.innerHTML = '<p>No major red flags detected based on the information provided.</p>';
        return;
    }
    
    let html = '';
    redFlags.forEach(flag => {
        const severityClass = flag.severity.toLowerCase();
        html += `
            <div class="red-flag-item ${severityClass}">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div style="flex: 1;">
                        <div style="font-weight: bold; margin-bottom: 0.5rem;">
                            <span style="background: ${getSeverityColor(flag.severity)}; color: white; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.75rem; margin-right: 0.5rem;">
                                ${flag.severity}
                            </span>
                            ${escapeHtml(flag.flag)}
                        </div>
                        <p style="margin: 0; color: var(--gray);">
                            ${escapeHtml(flag.explanation)}
                        </p>
                    </div>
                </div>
            </div>
        `;
    });
    
    content.innerHTML = html;
}

/**
 * Display warnings
 */
function displayWarnings(warnings) {
    const section = document.getElementById('warningsSection');
    const content = document.getElementById('warningsContent');
    
    section.style.display = 'block';
    
    let html = '<ul style="list-style: none; padding: 0;">';
    warnings.forEach(warning => {
        html += `<li style="padding: 0.5rem 0; border-bottom: 1px solid var(--border);">⚠️ ${escapeHtml(warning)}</li>`;
    });
    html += '</ul>';
    
    content.innerHTML = html;
}

/**
 * Display recommendations
 */
function displayRecommendations(recommendations) {
    const content = document.getElementById('recommendationsContent');
    
    let html = '';
    recommendations.forEach(rec => {
        html += `
            <div class="recommendation-group">
                <h3>${escapeHtml(rec.title)}</h3>
                <ul>
                    ${rec.actions.map(action => `<li>${escapeHtml(action)}</li>`).join('')}
                </ul>
            </div>
        `;
    });
    
    content.innerHTML = html;
}

/**
 * Get color for severity level
 */
function getSeverityColor(severity) {
    switch (severity.toUpperCase()) {
        case 'CRITICAL':
            return '#dc2626';
        case 'HIGH':
            return '#f59e0b';
        case 'MEDIUM':
            return '#f59e0b';
        default:
            return '#6b7280';
    }
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Print-friendly styling
 */
window.addEventListener('beforeprint', () => {
    document.body.style.background = 'white';
});

window.addEventListener('afterprint', () => {
    document.body.style.background = '';
});