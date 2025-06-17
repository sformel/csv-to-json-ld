from linkml_runtime.utils.schemaview import SchemaView
import pandas as pd

# Update this to your actual schema path
schema_path = "remote/models/classes.yaml"

sv = SchemaView(schema_path, merge_imports=True)

required_deps = []

for class_name, class_def in sv.all_classes().items():
    if class_def.slots:
        for slot_name in class_def.slots:
            slot = sv.induced_slot(slot_name, class_name)
            if slot.required and slot.range in sv.all_classes():
                required_deps.append({
                    "Table": class_name,
                    "Depends on Table": slot.range,
                    "Field": slot.name,
                    "Multivalued": "Yes" if slot.multivalued else "No"
                })

# Print it as a readable Markdown table
df = pd.DataFrame(required_deps)
print(df.to_markdown(index=False))

