import yaml
from copy import deepcopy

backstage_config = {
    "apiVersion": "backstage.io/v1alpha1",
    "kind": "Component",
    "metadata": {
        "name": "example-website"
    },
    "spec": {
        "type": "website",
        "lifecycle": "experimental",
        "owner": "guests",
        "system": "examples",
        "providesApis": ["example-grpc-api"],
        "dependsOn": []
    }
}

# # Save the configurations to a YAML file with document separators
# with open('backstage-config.yaml', 'w') as file:
#     for i in range(1000):
#         config = deepcopy(backstage_config)
#         config['metadata']['name'] = f"example-website-{i}"
#         # Add document separator before each document except the first one
#         if i > 0:
#             file.write('---\n')
#         yaml.safe_dump(config, file, default_flow_style=False, sort_keys=False, allow_unicode=True)

with open('backstage-config-2.yaml', 'w') as file:
    for i in range(1000):
        backstage_config['spec']['dependsOn'].append(f"component:default/example-website-{i}")
    yaml.safe_dump(backstage_config, file, default_flow_style=False, sort_keys=False, allow_unicode=True)