import { useState } from "react";
import axios from "axios";

export default function AIDemo() {
  const [prompt, setPrompt] = useState("");
  const [answer, setAnswer] = useState("");

  const askAI = async () => {
    const response = await axios.post("http://localhost:3001/api/ask-ai", { prompt });
    setAnswer(response.data.answer);
  };

  return (
    <div>
      <input value={prompt} onChange={(e) => setPrompt(e.target.value)} />
      <button onClick={askAI}>Ask AI</button>
      <p>{answer}</p>
    </div>
  );
}