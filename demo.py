import spacy

from utils import load_json


def demo():
    # Load pre-trained spaCy model
    nlp = spacy.load("en_core_web_sm")

    hospitals = load_json('hospitals.json')

    for hospital in hospitals:
        services = hospital.get("Services")["Specific Clinical Services"]

        # Apply NLP model to extract entities
        doc = nlp(services)

        # Extract noun phrases or entities as services
        services_list = [chunk.text for chunk in doc.noun_chunks]

        print(services_list)

        # [print(service) for service in services_list]
        print("")


demo()