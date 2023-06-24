import os
import json

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient



managed_identity_id = os.environ.get('MANAGED_IDENTITY_ID')


def get_metadata_value(key):
    credential = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)

    instance = compute_client.virtual_machines.get(resource_group_name, vm_name, expand="instanceView")

    if key in instance.additional_properties:
        return instance.additional_properties[key]
    else:
        return None

# Example usage
subscription_id = "cfd0f032-3c46-4727-8281-a17e0ec067d8"
resource_group_name = "Alisha-tech-challenge"
vm_name = "your-vm-name"
data_key = "vmId"

value = get_metadata_value(data_key)

if value is not None:
    json_output = json.dumps({data_key: value})
    print(json_output)
else:
    print(f"Metadata key '{data_key}' not found.")
