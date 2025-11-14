# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime, timezone
from openai import OpenAI
import os

# ---------------------------
# OpenAI Client
# ---------------------------

# Make sure OPENAI_API_KEY is set in your environment
# Example (Mac/Linux): export OPENAI_API_KEY="your-key-here"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------------------
# Pydantic Models
# ---------------------------

class MathRequest(BaseModel):
    operation: str = Field(
        ...,
        description="Math operation to perform: add, subtract, multiply, divide",
        examples=["add", "subtract", "multiply", "divide"],
    )
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")


class HistoryEntry(BaseModel):
    id: int
    operation: str
    a: float
    b: float
    result: float
    explanation: str
    timestamp: datetime


class MessageResponse(BaseModel):
    message: str


# ---------------------------
# In-Memory "Database"
# ---------------------------

history: List[HistoryEntry] = []
next_id: int = 1  # simple incremental ID


# ---------------------------
# Business Logic
# ---------------------------

def compute(operation: str, *args) -> float:
    operation = operation.lower()
    result = 0
    if operation == "add":
        for num in args:
            result += num
        return result
    elif operation == "subtract":
        for num in args:
            result -= num
        return result
    elif operation == "multiply":
        for num in args:
            result *= num
        return result
    elif operation == "divide":
        for num in args:
            result /= num
    
    else:
        raise ValueError(
            "Invalid operation. Use one of: add, subtract, multiply, divide."
        )


def explain_with_gpt(operation: str, a: float, b: float, result: float) -> str:
    """
    Call OpenAI to get a human-friendly explanation of the calculation.
    """
    prompt = f"""
    Explain the following math calculation in simple, friendly terms
    for someone who is not good at math.

    Operation: {operation}
    Inputs: {a} and {b}
    Result: {result}

    Rules:
    - Use short sentences.
    - Use plain language.
    - Give 2–4 sentences.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a patient math tutor who explains things very simply.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
        )
        explanation = response.choices[0].message.content
        return explanation.strip()
    except Exception as e:
        # In a real app you might log this
        raise RuntimeError(f"Error calling OpenAI API: {e}")


# ---------------------------
# FastAPI App
# ---------------------------

app = FastAPI(
    title="Math Operations API with AI Explanation",
    description=(
        "A simple FastAPI service that performs math operations, "
        "stores calculation history in memory, and uses OpenAI GPT "
        "to generate human-friendly explanations."
    ),
    version="1.0.0",
)


# 1️⃣ POST /calculate
@app.post("/calculate", response_model=HistoryEntry)
def calculate(request: MathRequest):
    global next_id

    # 1. Compute result
    try:
        result = compute(request.operation, request.a, request.b)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    # 2. Get GPT explanation
    try:
        explanation = explain_with_gpt(request.operation, request.a, request.b, result)
    except RuntimeError as re:
        raise HTTPException(status_code=500, detail=str(re))

    # 3. Build history entry
    entry = HistoryEntry(
        id=next_id,
        operation=request.operation.lower(),
        a=request.a,
        b=request.b,
        result=result,
        explanation=explanation,
        timestamp=datetime.now(timezone.utc),
    )

    # 4. Store in history
    history.append(entry)
    next_id += 1

    return entry


# 2️⃣ GET /history
@app.get("/history", response_model=List[HistoryEntry])
def get_history():
    return history


# 3️⃣ GET /history/{id}
@app.get("/history/{entry_id}", response_model=HistoryEntry)
def get_history_item(entry_id: int):
    for entry in history:
        if entry.id == entry_id:
            return entry
    raise HTTPException(status_code=404, detail=f"History entry with id={entry_id} not found.")


# 4️⃣ DELETE /history
@app.delete("/history", response_model=MessageResponse)
def clear_history():
    global history, next_id
    history = []
    next_id = 1  # reset ID counter if you like
    return MessageResponse(message="History cleared successfully.")
