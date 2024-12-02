import os
import requests
from typing import Optional

import util

FLOW_ID = os.getenv("ASK_AI_FLOW_ID")
APPLICATION_TOKEN = os.getenv("ASK_AI_APPLICATION_TOKEN")
ENDPOINT = "ask-ai"  # The endpoint name of the flow

# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}


def ask_ai(profile: dict, question: str):

    TWEAKS = {
        "TextInput-Uy3c8": {"input_value": util.dict_to_string(profile)},
        "TextInput-a1tan": {"input_value": question},
    }

    result = util.run_flow(
        "", endpoint=ENDPOINT, tweaks=TWEAKS, application_token=APPLICATION_TOKEN
    )

    return result["outputs"][0]["outputs"][0]["messages"][0]["message"]


if __name__ == "__main__":
    import dotenv
    import pprint

    dotenv.load_dotenv

    result = ask_ai(
        {
            "name": "Gerry",
            "age": 59,
            "weight": 160.0,
            "height": 67.0,
            "gender": "male",
            "activity_level": "moderately active",
        },
        "can you generate a workout routine to enhace mountain biking strength"
    )
    print("#"*50)
    pprint.pprint(result)
