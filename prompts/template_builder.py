def build_prompt(persona_summary, question):
    """
    Constructs a persona-conditioned CoT prompt.

    Args:
        persona_summary (str): A string describing the persona.
        question (str): The reasoning question.

    Returns:
        str: The final prompt string.
    """
    prompt = f"Persona Summary:\n{persona_summary}\n\n"
    prompt += f"Q: {question}\nA:"
    return prompt

