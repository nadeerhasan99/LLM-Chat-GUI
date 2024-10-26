import requests

headers = {"Content-Type": "application/json"}
user_input = "What is the capital of France?"

base_url = "https://fec6-34-118-241-84.ngrok-free.app"  # Update this with your actual base URL
endpoint = f"{base_url}/generate"
response = requests.post(endpoint, headers=headers, json={
    "inputs": "\n\n### Instructions:\n" + user_input + "\n\n### Response:\n",  # Use 'inputs'
    "parameters": {"stop": ["\n", "###"]}  # Use 'parameters' for additional options like 'stop'
})

output = response.json()
print(output)
