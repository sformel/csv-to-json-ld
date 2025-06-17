from linkml_runtime.utils.schemaview import SchemaView
import pandas as pd

schema_path = "remote/models/classes.yaml"  # Update if needed
sv = SchemaView(schema_path, merge_imports=True)

results = []

for class_name, class_def in sv.all_classes().items():
    required = []
    if class_def.slots:
        for slot_name in class_def.slots:
            slot = sv.induced_slot(slot_name, class_name)
            if slot.required:
                required.append(slot.name)

    results.append({
        "Table": class_name,
        "Has Required 'id'": "Yes" if "id" in required else "No",
        "Has Required 'metadataPublisherId'": "Yes" if "metadataPublisherId" in required else "No",
        "Has Required 'metadataDescribedForActionId'": "Yes" if "metadataDescribedForActionId" in required else "No"
    })

df = pd.DataFrame(results)
print(df.to_markdown(index=False))

