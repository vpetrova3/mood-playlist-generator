// Text-based mood detection
async function generateTextPlaylist() {
    const userInput = document.getElementById("moodInput").value;

    if (!userInput.trim()) {
        alert("Please describe your mood.");
        return;
    }

    try {
        const response = await fetch("/get_playlist", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: userInput })
        });
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }
        const data = await response.json();
        document.getElementById("result").innerHTML =
            `<p><strong>Mood Detected from Text:</strong> ${data.mood}</p>
             <a href="${data.playlist}" target="_blank">🎵 Open Spotify Playlist</a>`;
    } catch (err) {
        console.error(err);
        document.getElementById("result").innerHTML =
            `<p>😕 Could not get playlist. Please try again.</p>`;
    }
}

// Face-based mood detection
async function generateFacePlaylist() {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<p>Detecting mood from face...</p>";

    try {
        const response = await fetch("/face_mood");
        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }
        const data = await response.json();
        resultDiv.innerHTML =
            `<p><strong>Mood Detected from Face:</strong> ${data.mood}</p>
             <a href="${data.playlist}" target="_blank">🎵 Open Spotify Playlist</a>`;
    } catch (err) {
        console.error(err);
        resultDiv.innerHTML =
            `<p>😕 Could not detect mood from face. Please try again.</p>`;
    }
}
