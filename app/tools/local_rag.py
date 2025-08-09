from typing import List, Dict, Optional
import os
import json

from google.adk.tools import FunctionTool

# Simple local RAG over JSONL or Markdown directory.
# This is a placeholder lexical search to integrate with the agent schema.

DEFAULT_KNOWLEDGE_DIR = os.getenv("KNOWLEDGE_DIR", "knowledge")


def _list_knowledge_files(base_dir: str) -> List[str]:
    paths: List[str] = []
    if not os.path.isdir(base_dir):
        return paths
    for root, _dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith((".md", ".txt", ".json", ".jsonl")):
                paths.append(os.path.join(root, f))
    return paths


def _read_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except Exception:
        return ""


def rag_query(query: str, top_k: int = 3, knowledge_dir: Optional[str] = None) -> Dict:
    """Naive local RAG: search files in knowledge_dir and return top_k chunks.

    Args:
        query: The user question.
        top_k: Number of contexts to return.
        knowledge_dir: Directory containing knowledge sources.

    Returns:
        Dict with matched contexts.
    """
    base_dir = knowledge_dir or DEFAULT_KNOWLEDGE_DIR
    files = _list_knowledge_files(base_dir)
    if not files:
        return {
            "status": "error",
            "error_message": f"No knowledge files found in {base_dir}",
            "query": query,
        }

    # Very naive scoring by substring count, for placeholder purposes.
    scored: List[Dict] = []
    q_lower = query.lower()
    for path in files:
        text = _read_text(path)
        if not text:
            continue
        score = text.lower().count(q_lower)
        if score > 0:
            scored.append({"path": path, "score": score, "excerpt": text[:2000]})

    if not scored:
        # Return first files to avoid empty context, but mark low score
        fallback = [{"path": p, "score": 0, "excerpt": _read_text(p)[:2000]} for p in files[:top_k]]
        return {"status": "success", "matches": fallback, "note": "No direct match; returning fallback contexts"}

    scored.sort(key=lambda x: x["score"], reverse=True)
    return {"status": "success", "matches": scored[:top_k]}


local_rag_tool = FunctionTool(func=rag_query)
