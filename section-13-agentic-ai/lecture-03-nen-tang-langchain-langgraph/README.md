# Section 13 · Lecture 3 — Nền tảng LangChain & LangGraph

_Phần của: **Section 13: Agentic AI**_

**Số slide:** 6

---

## Nội dung slide

### Slide 1

- 03
- SECTION 13 · LECTURE 03
- Nền tảng LangChain & LangGraph
- ~9 phút · 6 slides

### Slide 2

- L03 · LANGCHAIN & LANGGRAPH
- LangChain
- Nối LLM, prompt, tool, memory
- Chain các bước
- Prompt
- →
- LLM
- →
- Tool
- →
- Output

### Slide 3

- L03 · LANGCHAIN & LANGGRAPH
- Các thành phần
- Models · Prompts · Chains
- Tools · Memory
- MODELS
- LLM
- PROMPTS
- Template
- CHAINS
- Nối bước
- TOOLS · MEMORY
- Tool · nhớ

### Slide 4

- L03 · LANGCHAIN & LANGGRAPH
- Hạn chế của chain tuyến tính
- Khó rẽ nhánh, lặp, điều kiện
- Agent cần luồng phức tạp hơn
- Chain thẳng ✕ vòng lặp · điều kiện
- agent cần rẽ nhánh và lặp — chain tuyến tính không đủ

### Slide 5

- L03 · LANGCHAIN & LANGGRAPH
- LangGraph
- Agent dạng đồ thị trạng thái
- Rẽ nhánh, lặp, điều kiện
- State
- ↓
- Node: gọi LLM / tool
- ↓
- Điều kiện → rẽ nhánh / lặp

### Slide 6

- L03 · LANGCHAIN & LANGGRAPH — TÓM TẮT
- Tóm tắt
- LangChain
- components
- LangGraph state graph
- BÀI TIẾP
- LlamaIndex
- →

---

_Slide deck đầy đủ: [../slides.pptx](../slides.pptx)_

_← [Về Section README](../README.md)_