async function shortenUrl() {
    const urlInput = document.getElementById('url-input');
    const result = document.getElementById('result');
    const url = urlInput.value;

    if (!url) {
        result.textContent = 'Please enter a URL!';
        return;
    }

    try {
        const response = await fetch('/shorten', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();
        if (data.short_url) {
            result.innerHTML = `Short URL: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;
        } else {
            result.textContent = data.error || 'Error occurred!';
        }
    } catch (error) {
        result.textContent = 'Failed to connect to the server.';
    }
}
