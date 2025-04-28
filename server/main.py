from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv  # 可选，方便本地开发

# 加载 .env 文件（本地开发时）
load_dotenv()

app = FastAPI()

# 更详细的 CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议替换为前端域名（如 "https://your-site.com"）
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

@app.post("/api/ask-ai")
async def ask_ai(prompt: str):
    # 从环境变量读取密钥
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"answer": response.choices[0].message.content}