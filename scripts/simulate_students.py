import random
import pandas as pd 

# Defined learning types for simulated data for the training phase of the model
learning_types = ['Visual', 'Auditory', 'Reading/Writing', 'Kinesthetic']
resource_types = ['Video', 'Text', 'Interactive']

num_students = 500
num_sessions = 5 # Number of sessions per student
students = []

# Defines engagement ranges for each learning type and resource type 
engagement_ranges = {
    'Visual': {
        'Video': (0.7, 1.0),
        'Quiz': (0.5, 0.8),
        'Interactive': (0.2, 0.5),
        'Time': (30, 60)
    },
    'Auditory': {
        'Video': (0.3, 0.6),
        'Quiz': (0.7, 1.0),
        'Interactive': (0.4, 0.7),
        'Time': (20, 40)
    },
    'Reading/Writing': {
        'Video': (0.2, 0.5),
        'Quiz': (0.6, 0.9),
        'Interactive': (0.3, 0.6),
        'Time': (50, 70)
    },
    'Kinesthetic': {
        'Video': (0.1, 0.4),
        'Quiz': (0.4, 0.7),
        'Interactive': (0.6, 1.0),
        'Time': (40, 80)
    }
}

def simulate_engagement(learning_type, resource_type):
    """
    Simulates student engagement data based on their predefined learning type.

    Args:
        learning_type: The learning type of the student ('Visual', 'Auditory', 'Reading/Writing' or 'Kinesthetic').
        resouce_type: The type of resource accessed in the session ('Video', 'Text', 'Interactive')

    Returns:
        student_dict: A dictionary with simulated engagement metrics.

    Notes:
        - Visual learners engage more with videos, less with interactive tasks.
        - Auditory learners perform better in quizzes and audio materials, less in videos.
        - Kinesthetic learners excel in interactive tasks, less in videos.
        - Reading/Writing learners perform best with written materials, and engage less with videos.

    """
    ranges = engagement_ranges[learning_type]
    noise_level = 0.05 # Small noise level for engagement scores
    session_noise = random.uniform(-0.02, 0.02)  # Small session-level noise
    return {
        'video_engagement': random.uniform(*ranges['Video']) + random.uniform(-noise_level, noise_level) + session_noise,
        'quiz_score': random.uniform(*ranges['Quiz']) + random.uniform(-noise_level, noise_level) + session_noise,
        'interactive_engagement': random.uniform(*ranges['Interactive']) + random.uniform(-noise_level, noise_level) + session_noise,
        'time_spent': random.uniform(*ranges['Time']) + random.uniform(-noise_level * 10, noise_level * 10) + session_noise * 10  
    }


for student_id in range(1, num_students + 1):
    learning_type = random.choice(learning_types)
    student_sessions = []
    for _ in range(num_sessions):
        resource_type = random.choice(resource_types)
        engagement_data = simulate_engagement(learning_type, resource_type)
        session_data = {
            'student_id': student_id, 
            'learning_type': learning_type,
            'resource_type': resource_type,
            **engagement_data
        }
        student_sessions.append(session_data)
    students.append(student_sessions)

df_students = pd.DataFrame(students)
df_students.to_csv('data/simulated_students.csv', index=False)