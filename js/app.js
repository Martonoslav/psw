const lowercase = 'abcdefghijklmnopqrstuvwxyz';
const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const numbers = '0123456789';
const special = '!#$%&()*+,-./:;<=>?@[]^_{|}~';

let symbols = [];
let customsymbols = '';

function appendSymbols() {
    symbols = [];
    if (document.getElementById('lowercase').checked) {
        symbols.push(lowercase);
    }
    if (document.getElementById('uppercase').checked) {
        symbols.push(uppercase);
    }
    if (document.getElementById('numbers').checked) {
        symbols.push(numbers);
    }
    if (document.getElementById('special').checked) {
        symbols.push(special);
    }
    if (document.getElementById('custom').checked && customsymbols) {
        symbols.push(customsymbols);
    }
    symbols = symbols.join('');
    generatePasswords();
}

function toggleCustom() {
    const customCheckbox = document.getElementById('custom');
    const customInput = document.getElementById('customsymbols');
    if (customCheckbox.checked) {
        customInput.style.display = 'inline';
    } else {
        customInput.style.display = 'none';
        customsymbols = '';
    }
    appendSymbols();
}

function generatePasswords() {
    const output = document.getElementById('output');
    const length = parseInt(document.getElementById('length').value);
    
    output.value = '';
    
    if (symbols.length === 0) {
        output.value = 'Error: No character sets selected';
        return;
    }
    
    for (let i = 0; i < 10; i++) {
        let password = '';
        for (let j = 0; j < length; j++) {
            const randomChar = symbols[Math.floor(Math.random() * symbols.length)];
            password += randomChar;
        }
        output.value += password + '\n';
    }
}

document.getElementById('customsymbols').addEventListener('input', function() {
    customsymbols = this.value;
    appendSymbols();
});

// Initialize
appendSymbols();
