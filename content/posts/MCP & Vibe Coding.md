---
title: MCP & Vibe Coding
date: 2025-09-03
draft: false
tags:
  - AI
---
## General MCP work flow

!![Image Description](/images/Pasted%20image%20202509041.png.png)
## MCP in IDE

歡迎凱大跟子勤!

### IDE

1. Claude [https://www.cursor.com/](https://www.cursor.com/)  
2. Windsurf [https://windsurf.com/pricing](https://windsurf.com/pricing)  
3. TRAE [https://www.trae.ai/](https://www.trae.ai/)  
4. FireStudio [https://firestudio.space/](https://firestudio.space/)  

### LLM Model

1. Claude-3.7 
2. GPT-4o
3. DeepSeek-V3  
4. Gemini-2.5 pro

!![Image Description](/images/Pasted%20image%20202509042.png.png)

## Flow - IDE with LLM

!![Image Description](/images/Pasted%20image%20202509043.png.png)
## Flow - IDE with LLM and MCP

!![Image Description](/images/Pasted%20image%20202509045.png.png)

### Config example for get doc content  
[https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)  

{  
  "mcpServers": {  
    "LarkDocs": {  
      "command": "npx",  
      "args": [  
        "-y",  
        "--registry",  
        "http://bnpm.byted.org/",  
        "@byted/mcp-lark-docs@latest"  
      ],  
      "env": {  
        "LARK_APP_ID": "ididid",  
        "LARK_APP_SECRET": "secret",  
        "AUTH_CALLBACK_PORT": "",  
        "AUTH_CALLBACK_ENDPOINT": ""  
      }  
    }  
  }  
}

#### IDE在背後做什麼

將所有的MCP config丟給LLM  
→ 判斷哪一個api是最適合的  
→ 將api及呼叫方法回傳給IDE  
→ IDE呼叫api拿資料  
→ 將MCP api回傳的資料整理成prompt丟給LLM  
→ code implementation