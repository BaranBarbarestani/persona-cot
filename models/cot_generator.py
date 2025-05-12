import openai

openai.api_key = "YOUR_API_KEY"  # Replace this with your OpenAI API key

def generate_cot(prompt, model="gpt-4"):
    """
    Generate Chain-of-Thought reasoning using a GPT model, conditioned on the persona.

    Args:
    - prompt (str): The prompt containing the persona summary and reasoning task.
    - model (str): The OpenAI model to use. Default is "gpt-4".

    Returns:
    - str: The generated response from the model.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,  # Controls creativity
            max_tokens=200    # Limit the output length
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating Chain-of-Thought: {e}")
        return None

