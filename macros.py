import os
import json

import util

FLOW_ID = os.getenv("MACROS_FLOW_ID")
APPLICATION_TOKEN = os.getenv("MACROS_APPLICATION_TOKEN")
ENDPOINT = "macros"  # The endpoint name of the flow


# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
def get_macros(profile, goals):
    TWEAKS = {
        "TextInput-2QkrV": {"input_value": ", ".join(goals)},
        "TextInput-F5vou": {"input_value": util.dict_to_string(profile)},
    }
    result = util.run_flow(
        "",
        endpoint=ENDPOINT,
        tweaks=TWEAKS,
        application_token=APPLICATION_TOKEN
    )

    return json.loads(
            result["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"])
# result = get_macros(
#         "name: Jerry, age: 59, weight: 170lbs, 68in", "muscle gain")
# print(result)
