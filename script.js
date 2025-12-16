function generateStory() {
  const genre = document.getElementById("genre").value;
  const characters = document.getElementById("characters").value;
  const theme = document.getElementById("theme").value;

  fetch("http://127.0.0.1:5000/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      genre: genre,
      characters: characters,
      theme: theme
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerText = data.story;
  });
}
