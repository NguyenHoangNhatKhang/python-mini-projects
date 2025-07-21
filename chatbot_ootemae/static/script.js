document.getElementById("sent").addEventListener("click", function () {
  const input = document.getElementById("chatbot-input");
  const message = input.value;
  if (!message.trim()) return;

  // messages display
  const userMsg = document.createElement("div");
  userMsg.className = "message user";
  userMsg.textContent = message;
  document.getElementById("chatbot-messages").appendChild(userMsg);

  input.value = ""; // Clear input

  // sending messages to flask
  fetch("/chat-answer", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: message }),
  })
    .then((response) => response.json())
    .then((data) => {
      // bot response
      const botMsg = document.createElement("div");
      botMsg.className = "message bot";
      botMsg.textContent = data.reply;
      document.getElementById("chatbot-messages").appendChild(botMsg);
    });
});
