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

#Study Planner

def study_planner(subject: str, days_until_exam: int) -> str:
    """Creates a day-by-day study plan for a student preparing for an exam.

    Args:
        subject: The subject the student is preparing for.
        days_until_exam: The number of days the student has until their exam.

    Returns:
        A structured day-by-day study schedule with topics and goals.
    """
    return f"""Create a detailed {days_until_exam}-day study plan for {subject}.
    
    Format it exactly like this:
    
    Day 1: [Topic to cover]
    - Goal: [What the student should achieve]
    - Resources: [What to read or watch]
    - Practice: [Exercise to do]
    
    Repeat for each day. End with exam-day tips."""
