curl -X POST \
    "https://api.langflow.astra.datastax.com/lf/ce2020fd-42fd-4bd3-9b59-2d93aca42c3f/api/v1/run/ask-ai?stream=false" \
    -H 'Content-Type: application/json'\
    -H "Authorization: Bearer $API_AUTHENTICATION_TOKEN"\
    -d '{"input_value": "message",
    "output_type": "chat",
    "input_type": "chat",
    "tweaks": {
  "TextInput-a1tan": {},
  "Prompt-OhHE4": {},
  "OpenAIModel-zooY1": {},
  "ConditionalRouter-x8BFM": {},
  "ToolCallingAgent-QEnqC": {},
  "CalculatorTool-hQFVp": {},
  "OpenAIModel-EnFHm": {},
  "TextOutput-WVeE9": {},
  "Prompt-0fdl3": {},
  "TextInput-Uy3c8": {},
  "AstraDB-SBJk0": {},
  "ParseData-9uSas": {},
  "Prompt-Tdyh6": {},
  "OpenAIModel-4Fx6b": {},
  "TextOutput-M2fDp": {}
}}'
