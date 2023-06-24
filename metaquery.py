import os
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient



managed_identity_id = os.environ.get('MANAGED_IDENTITY_ID')



def get_azure_instance_metadata(key=None):
    metadata = {}

    # Retrieve the instance metadata
    try:
        credential = DefaultAzureCredential()
        client = ComputeManagementClient(credential, subscription_id='<Your Azure Subscription ID>')
        vm = client.virtual_machines.get('<Your Resource Group Name>', '<Your VM Name>')
        metadata = vm.__dict__['_attribute_map']
    except Exception as e:
        print(f"Error retrieving Azure instance metadata: {str(e)}")

    # Filter the metadata based on the provided key
    if key is not None:
        metadata = {key: metadata.get(key)}

    # Return the JSON-formatted output
    return json.dumps(metadata, indent=4)

# Example usage:
azure_metadata = get_azure_instance_metadata()
print(azure_metadata)
