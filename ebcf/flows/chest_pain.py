CHEST_PAIN_FLOW = {
    "presentation": "chest_pain",
    "scope": "non_diagnostic",
    "rules": {
        "allow_unknown": True,
        "no_diagnosis": True,
    },
    "stages": [
        {
            "name": "presence_check",
            "questions": [
                {
                    "id": "cp_present",
                    "text": "Are you currently experiencing chest pain?",
                    "type": "choice",
                    "options": ["yes", "no", "unknown"],
                    "required": True,
                }
            ],
        },
        {
            "name": "symptom_qualification",
            "questions": [
                {
                    "id": "pain_quality",
                    "text": "How would you describe the pain?",
                    "type": "choice",
                    "options": ["pressure", "sharp", "burning", "other", "unknown"],
                },
                {
                    "id": "pain_location",
                    "text": "Where is the pain located?",
                    "type": "choice",
                    "options": ["center", "left", "right", "diffuse", "unknown"],
                },
                {
                    "id": "onset",
                    "text": "Did the pain start suddenly?",
                    "type": "choice",
                    "options": ["yes", "no", "unknown"],
                },
                {
                    "id": "duration",
                    "text": "How long has the pain lasted?",
                    "type": "choice",
                    "options": ["minutes", "hours", "days", "unknown"],
                },
            ],
        },
        {
            "name": "associated_observables",
            "questions": [
                {
                    "id": "associated_symptoms",
                    "text": "Are any of the following present?",
                    "type": "multi_choice",
                    "options": [
                        "shortness_of_breath",
                        "nausea",
                        "sweating",
                        "dizziness",
                        "none",
                    ],
                }
            ],
        },
        {
            "name": "red_flag_check",
            "questions": [
                {
                    "id": "red_flags",
                    "text": "Are any of these true?",
                    "type": "multi_choice",
                    "options": [
                        "severe_pain",
                        "fainting",
                        "confusion",
                        "radiating_pain",
                        "known_heart_disease",
                        "none",
                    ],
                    "hard_stop": True,
                }
            ],
        },
    ],
}
