def apply_guardrail(inputs, request_data, input_type):
    """
    Assistant Identity Protection

    Blocks attempts to discover:
    - Assistant identity
    - Creator / owner
    - Provider
    - Underlying model
    """

    text = lower(" ".join(inputs.get("texts", [])))

    identity_queries = [
        "who are you",
        "what are you",
        "identify yourself",
        "introduce yourself",
        "tell me about yourself"
    ]

    creator_queries = [
        "who created you",
        "who made you",
        "who built you",
        "who developed you",
        "who owns you",
        "your creator",
        "your owner",
        "your developer"
    ]

    model_queries = [
        "what model are you",
        "which model are you",
        "what llm are you",
        "what ai are you",
        "what foundation model",
        "what base model",
        "what powers you",
        "powered by"
    ]

    provider_queries = [
        "which provider",
        "who is your provider",
        "who hosts you",
        "what provider"
    ]

    if contains_any(text, identity_queries):
        return block(
            "I can't disclose information about my identity or internal implementation."
        )

    if contains_any(text, creator_queries):
        return block(
            "I can't disclose information about my creators or ownership."
        )

    if contains_any(text, model_queries):
        return block(
            "I can't disclose details about the underlying AI model."
        )

    if contains_any(text, provider_queries):
        return block(
            "I can't disclose information about the service provider."
        )

    return allow()