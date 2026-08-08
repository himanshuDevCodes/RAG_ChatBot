// ===============================
// Backend API URL
// ===============================
const API_URL = "http://localhost:8000";


// ===============================
// Upload PDF
// ===============================
const uploadButton = document.getElementById("upload-button");

uploadButton.addEventListener("click", async () => {

    // Get selected PDF
    const fileInput = document.getElementById("pdf-file");
    const status = document.getElementById("upload-status");

    // Validate file selection
    if (fileInput.files.length === 0) {
        alert("Please select a PDF.");
        return;
    }

    // Create FormData (required for UploadFile in FastAPI)
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    status.innerHTML = "Uploading PDF...";

    try {

        // Call Upload API
        const response = await fetch(`${API_URL}/upload`, {
            method: "POST",
            body: formData
        });

        let data = null;
        try {
            data = await response.json();
        } catch (parseError) {
            console.error("Upload response parse failed:", parseError);
        }

        if (response.ok) {
            status.innerHTML = "✅ " + (data?.message || "Upload succeeded");
        } else {
            console.error("Upload API error:", response.status, data);
            status.innerHTML = "❌ " + (data?.detail || response.statusText || "Upload failed.");
        }

    } catch (error) {

        console.error(error);

        status.innerHTML = "Upload Failed!";
    }

});


// ===============================
// Chat
// ===============================
document.getElementById("chat-form").addEventListener("submit", async (e) => {

    e.preventDefault();

    const userInput = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const userMessage = userInput.value.trim();

    // Ignore empty message
    if (userMessage === "") return;

    // Show user message
    chatBox.innerHTML += `
        <div class="user-message">
            ${userMessage}
        </div>
    `;

    try {

        // Call Chat API
        const response = await fetch(`${API_URL}/chat/`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                message: userMessage,
                conversation_id: "001a"

            })

        });

        const data = await response.json();

        // Show bot reply
        chatBox.innerHTML += `
            <div class="bot-message">
                ${data.response}
            </div>
        `;

    } catch (error) {

        console.error(error);

        chatBox.innerHTML += `
            <div class="bot-message">
                Something went wrong.
            </div>
        `;

    }

    // Clear textbox
    userInput.value = "";

    // Scroll to latest message
    chatBox.scrollTop = chatBox.scrollHeight;

});