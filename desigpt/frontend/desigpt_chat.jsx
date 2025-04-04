import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function DesiGPTChat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { role: "user", content: input };
    setMessages([...messages, userMessage]);
    setInput("");

    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    const botReply = { role: "assistant", content: data.reply };
    setMessages((prev) => [...prev, botReply]);
  };

  return (
    <div className="min-h-screen bg-orange-50 p-4 flex flex-col items-center">
      <h1 className="text-3xl font-bold mb-4 text-orange-700">🧠 DesiGPT</h1>
      <Card className="w-full max-w-2xl p-4 space-y-2 bg-white shadow-xl rounded-2xl">
        <CardContent>
          <div className="h-96 overflow-y-scroll space-y-4">
            {messages.map((msg, i) => (
              <div
                key={i}
                className={`p-2 rounded-xl text-sm whitespace-pre-wrap ${
                  msg.role === "user"
                    ? "bg-orange-100 text-right"
                    : "bg-green-100 text-left"
                }`}
              >
                {msg.content}
              </div>
            ))}
          </div>
          <div className="mt-4 flex items-center gap-2">
            <Input
              placeholder="Ask me anything about India... 🇮🇳"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            />
            <Button onClick={sendMessage}>Send</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
