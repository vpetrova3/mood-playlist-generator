async function generatePlaylist() {
    const userInput = document.getElementById("moodInput").value;

    const response = await fetch("/get_playlist", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: userInput })
    });

    const data = await response.json();
    document.getElementById("result").innerHTML = `
        <p><strong>Mood Detected:</strong> ${data.mood}</p>
        <a href="${data.playlist}" target="_blank">Open Spotify Playlist</a>
    `;
}
