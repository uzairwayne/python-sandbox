import requests
import json
import time

def add_two_numbers(a: int, b: int) -> int:
  return a + b

print(add_two_numbers(1, 2))


def call_node_endpoint(endpoint, method='GET', data=None):
    base_url = "http://localhost:8002"  # Adjust this to your Node.js server's address and port
    url = f"{base_url}{endpoint}"
    
    try:
        if method == 'POST':
            response = requests.post(url, json=data)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.status_code  # Assuming the response has no body
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def process_json_array(json_file_path, endpoint, delay=0.1):
    try:
        # Read the JSON file
        with open(json_file_path, 'r') as file:
            data_array = json.load(file)
        
        if not isinstance(data_array, list):
            raise ValueError("The JSON file should contain an array of objects")
        
        results = []
        index = 0
        for item in data_array:
            result = call_node_endpoint(endpoint, method='POST', data={
                "events": [item],
                "firstEventSequence": 25154,
                "lastEventSequence": 25154,
                "entropy": "JMYJSVOPKZAWOSNPPZPV"
            })
            results.append(result)
            print(f"Processed item: {index} {item}")
            print(f"Result: {index} {result}")
            print("---")
            index += 1

            time.sleep(delay)
        
        return results
    
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    json_file_path = "data.json"  # Path to your JSON file
    endpoint = "/xero/webhook"  # Your Node.js endpoint
    
    results = process_json_array(json_file_path, endpoint, delay=0.1) # delay 100 ms
    print("All results:", results)