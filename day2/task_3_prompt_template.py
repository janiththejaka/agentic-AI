#!/usr/bin/env python3
"""
Task 3: Prompt Templates - Dynamic, Reusable Prompts
Show how ONE template can be reused with different variables.

Learning Goal: Master prompt templates for consistent, reusable prompts.


# The copy-paste nightmare (100 files with slight variations):
"Explain quantum computing in simple terms"
"Explain machine learning in simple terms"
"Explain blockchain in simple terms"
# Change "simple terms" to "one sentence"? Edit 100 files!

# One template to rule them all:
template = "Explain {topic} in {style}"
# Use it 1000 times with different values!
template.format(topic="AI", style="5 words")
template.format(topic="crypto", style="a haiku")

"""

import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

def main():
    print("🎯 Task 3: Dynamic Prompt Templates")
    print("=" * 50)

    print("\n📝 Creating a Reusable Template")
    print("=" * 50)

    # TODO 1: Create a versatile template
    template = PromptTemplate(
        input_variables=["___", "___"],  # Replace ___ with: "topic", "style"
        template="___"  # Replace ___ with: "Explain {topic} in {style}"
    )

    # Test with actual LLM to show it works
    print("\n🤖 Testing Template with AI")
    print("=" * 50)

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-5.6-luna",
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE"),
        temperature=0.7
    )

    # TODO 2: Use the template with LLM
    if template and llm:
        # Format the template with specific values
        test_prompt = template.format(
            topic="___",  # Replace ___ with: "artificial intelligence"
            style="___"   # Replace ___ with: "exactly 5 words"
        )

        print(f"📝 Sending to AI: {test_prompt}")

        # Get AI response
        response = llm.invoke(test_prompt)
        print(f"\n🤖 AI Response: {response.content}")

    # Show the benefits
    print("\n💡 Template Benefits:")
    print("  ✓ ONE template, INFINITE uses")
    print("  ✓ Variables make it dynamic")
    print("  ✓ Consistent structure across all prompts")
    print("  ✓ Change inputs, not code!")

    # Create marker for completion
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task3_complete.txt", "w") as f:
        f.write("COMPLETED")

    print("\n✅ Task 3 completed! One template, endless possibilities!")

if __name__ == "__main__":
    main()