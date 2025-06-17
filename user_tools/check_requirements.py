from linkml_runtime.utils.schemaview import SchemaView
import pandas as pd

# Load the schema
schema_path = "remote/models/classes.yaml"
sv = SchemaView(schema_path, merge_imports=True)

records = []

for class_name, class_def in sv.all_classes().items():
    if class_def.slots:
        for slot_name in class_def.slots:
            slot = sv.induced_slot(slot_name, class_name)
            if slot.range in sv.all_classes():  # Only include cross-table dependencies
                records.append({
                    "Table": class_name,
                    "Depends on Table": slot.range,
                    "Field": slot.name,
                    "Multivalued": "Yes" if slot.multivalued else "No",
                    "Required": slot.required  # Boolean for easier filtering
                })

# Convert to DataFrame and sort
df = pd.DataFrame(records)
df = df.sort_values(by=["Table", "Depends on Table", "Field"])

# Split into two tables
required_df = df[df["Required"] == True].drop(columns=["Required"])
optional_df = df[df["Required"] == False].drop(columns=["Required"])

# Print separately
print("### 📌 Required Cross-Table Dependencies\n")
print(required_df.to_markdown(index=False))

print("\n\n---\n\n")

print("### 🧩 Optional Cross-Table Dependencies\n")
print(optional_df.to_markdown(index=False))

