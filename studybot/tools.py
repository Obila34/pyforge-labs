def explain_topic(topic: str, level: str = "beginner") -> str:
    """Explains a study topic at a given difficulty level.

    Args:
        topic: The subject or concept the student wants to understand.
        level: The difficulty level - either 'beginner', 'intermediate', or 'advanced'.

    Returns:
        A structured explanation of the topic at the requested level.
    """
    return f"Please explain {topic} at a {level} level with examples and key points."


# Backward-compatible alias for older references with a typo.
def expalin_topic(topic: str, level: str = "beginner") -> str:
    return explain_topic(topic=topic, level=level)


 #Quiz Tool
def quiz_student(topic: str) -> str:
    """Generates a short quiz to test a student's knowledge on a topic.

    Args:
        topic: The subject the student wants to be quizzed on.

    Returns:
        A set of 3 multiple choice questions with options A, B, C, D.
    """
    return f"""Generate exactly 3 multiple choice questions about {topic}.
    Format each question like this:
    
    Q1: [question]
    A) [option]
    B) [option]  
    C) [option]
    D) [option]
    Answer: [correct letter]
    
    After the student answers, mark them and give encouraging feedback."""   
