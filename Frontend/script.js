const analyzeBtn = document.getElementById("analyzeBtn");
const urlInput = document.getElementById("urlInput");
const loading = document.getElementById("loading");
const resultDiv = document.getElementById("result");
const errorDiv = document.getElementById("error");

analyzeBtn.addEventListener("click", async () => {
    const url = urlInput.value.trim();
    if (!url) {
        alert("Please enter a URL");
        return;
    }

    analyzeBtn.disabled = true;
    loading.classList.remove("hidden");
    resultDiv.classList.add("hidden");
    errorDiv.classList.add("hidden");

    try {
        const response = await fetch("https://crystlfly-cybersec-api.hf.space/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ payload: url }) 
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        document.getElementById("payload").textContent = data.payload;
        document.getElementById("attackType").textContent = data.prediction; 
        document.getElementById("confidence").textContent = (data.confidence * 100).toFixed(2) + "%";
        
        console.log("Status:", data.status);

        resultDiv.classList.remove("hidden");
    } catch (err) {
        errorDiv.textContent = "Error: " + err.message;
        errorDiv.classList.remove("hidden");
    } finally {
        analyzeBtn.disabled = false;
        loading.classList.add("hidden");
    }
});