document.addEventListener("DOMContentLoaded", function () {
  // required
  const input = document.getElementById("chatbot-input");
  const sendBtn = document.getElementById("sent");
  const messageBox = document.getElementById("chatbot-messages");

  //send
  sendBtn.addEventListener("click", function () {
    const userMessage = input.value.trim();

    if (userMessage === "") return; // Nếu không nhập gì thì bỏ qua

    // 1. Hiển thị tin nhắn người dùng lên khung chat
    const userDiv = document.createElement("div");
    userDiv.className = "message user";
    userDiv.textContent = userMessage;
    messageBox.appendChild(userDiv);

    // 2. Gửi tin nhắn đến Flask (backend)
    fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userMessage }),
    })
      .then((res) => res.json())
      .then((data) => {
        // 3. Nhận phản hồi từ Flask → hiển thị tin nhắn bot
        const botDiv = document.createElement("div");
        botDiv.className = "message bot";
        botDiv.textContent = data.reply;
        messageBox.appendChild(botDiv);

        // 4. Xoá nội dung input
        input.value = "";

        // 5. Scroll xuống cuối khung chat
        messageBox.scrollTop = messageBox.scrollHeight;
      })
      .catch((err) => {
        console.error("Lỗi khi gửi message:", err);
      });
  });
});
