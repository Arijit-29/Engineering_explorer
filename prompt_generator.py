from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    template="""
Please explain the engineering department "{dept_input}" with the following specifications:

Explanation Style: {style_input}  
Explanation Length: {length_input}  

1. Core Overview:
   - Describe what this engineering field focuses on.
   - Mention key subjects or domains involved.

2. Applications:
   - Explain real-world applications and industries where this field is used.

3. Skills Required:
   - List important technical and soft skills needed.

4. Career Opportunities:
   - Mention common job roles and career paths.

5. Examples / Analogies:
   - Use simple, relatable analogies to make concepts easier to understand.

If certain information is not available, respond with: "Insufficient information available" instead of guessing.

Ensure the explanation is clear, structured, and aligned with the provided style and length.
""",
    input_variables=['dept_input', 'style_input', 'length_input'],
    validate_template=True
)

template.save('dept_template.json')