// helper: render a list of Spotify embeds
function renderPlaylists(embeds) {
    return embeds
      .map(
        src => `
      <div class="col-lg-6 mb-4">
        <div class="ratio ratio-1x1 shadow-sm rounded">
          <iframe 
            src="${src}" 
            allow="encrypted-media" 
            loading="lazy">
          </iframe>
        </div>
      </div>`
      )
      .join('');
  }
  
  // Text-based
  async function generateTextPlaylist() {
    const text = document.getElementById("moodInput").value.trim();
    if (!text) return alert("Please describe your mood.");
    document.getElementById("result").innerHTML = `<p class="text-center">😴 Loading…</p>`;
  
    try {
      const res = await fetch("/get_playlist", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
      });
      if (!res.ok) throw new Error(res.status);
      const { mood, playlists } = await res.json();
      document.getElementById("result").innerHTML = `
        <h4 class="mb-4 text-center">Detected: <span class="badge bg-info">${mood}</span></h4>
        <div class="row">${renderPlaylists(playlists)}</div>
      `;
    } catch {
      document.getElementById("result").innerHTML =
        `<p class="text-danger text-center">Failed to load playlists.</p>`;
    }
  }
  
  // Face-based
  async function generateFacePlaylist() {
    document.getElementById("result").innerHTML = `<p class="text-center">😴 Loading…</p>`;
    try {
      const res = await fetch("/face_mood");
      if (!res.ok) throw new Error(res.status);
      const { mood, playlists } = await res.json();
      document.getElementById("result").innerHTML = `
        <h4 class="mb-4 text-center">Detected: <span class="badge bg-info">${mood}</span></h4>
        <div class="row">${renderPlaylists(playlists)}</div>
      `;
    } catch {
      document.getElementById("result").innerHTML =
        `<p class="text-danger text-center">Could not detect face.</p>`;
    }
  }
  