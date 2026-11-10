const button = document.getElementById("recommendBtn");

button.addEventListener("click", async () => {
  const payload = {
    rainfall: document.getElementById("rainfall").value,
    ph: document.getElementById("ph").value,
    nitrogen: document.getElementById("nitrogen").value
  };

  button.disabled = true;
  button.textContent = "Checking your values…";

  try {
    const response = await fetch("/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Something went wrong.");

    document.getElementById("resultTitle").innerHTML =
      `${result.crop}<br><em>is a match to explore.</em>`;
    document.getElementById("resultText").textContent =
      `Demo suitability score: ${result.score}%. ${result.note}`;
  } catch (error) {
    document.getElementById("resultTitle").textContent = "Please check your inputs.";
    document.getElementById("resultText").textContent = error.message;
  } finally {
    button.disabled = false;
    button.innerHTML = 'Recommend a crop <span>→</span>';
  }
});
