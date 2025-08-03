from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials

# Replace with your actual credentials
credentials = Credentials(
    url="https://us-south.ml.cloud.ibm.com",
    api_key="t1-SzhGhpPjAFnKtm3nTsrzuIei0T_ivsSMNacoik1ni"
)

client = APIClient(credentials)

# Simple test
try:
    print("Fetching available foundation models...")
    models = client.foundation_models.GE
    
    print("\nAvailable models:")
    for model in models:
        print(f"- {model['model_id']}")
        
except Exception as e:
    print(f"Error fetching foundation models: {e}")