import os
import json
from azure_metadata import AzureMetadata
#from azure.identity import DefaultAzureCredential
#from azure.mgmt.compute import ComputeManagementClient



managed_identity_id = os.environ.get('MANAGED_IDENTITY_ID')


def get_metadata_value(key):
    metadata = AzureMetadata().compute
    if key in metadata:
        return metadata[key]
    else:
        return None

# Example usage
data_key = "vmId"
value = get_metadata_value(data_key)

if value is not None:
    json_output = json.dumps({data_key: value})
    print(json_output)
else:
    print(f"Metadata key '{data_key}' not found.")

