
# MARCO-BOLO CSV-to-JSON-LD Tool

This repository contains a metadata publishing tool developed for **Work Package 1 (WP1)** of the [**MARCO-BOLO** project](https://marcobolo-project.eu/) (MARine COastal BiOdiversity Long-term Observations). WP1 focuses on data literacy and metadata flow across the project.

Learn more about WP1 here: [https://marcobolo-project.eu/work-packages/work-package-1](https://marcobolo-project.eu/work-packages/work-package-1)

This tool helps researchers and data managers transform metadata from structured CSV files into **JSON-LD** conforming to **Schema.org** and ready for harvesting by the [ODIS Catalog](https://catalog.odis.org/).

## Table of Contents

- [Project Context](#-project-context)
- [How It Works](#️-how-it-works)
- [Workflow Summary](#-workflow-summary)
- [Getting Started (No Installation Required)](#-getting-started-no-installation-required)
- [Hosting and Registration](#-hosting-and-registration)
- [Documentation & Resources](#-documentation--resources)
- [Human Workflow](#-human-workflow)
- [License](#-license)

## Project Context

WP1 of MARCO-BOLO supports the production of high-quality, FAIR metadata. This repository provides the reference toolchain for transforming project metadata into a format compatible with global discovery platforms such as ODIS.

## How It Works

The tool uses:

- **[LinkML](https://linkml.io/)** to define metadata models (e.g., Dataset, Person, Organization)
- **[CSV-W](https://csvw.org/)** metadata files to describe CSV structure
- A **[Makefile](https://opensource.com/article/18/8/what-how-makefile)** and [GitHub Actions](https://github.com/features/actions) to automate validation and transformation steps
- **[W3IDs](https://w3id.org/)** for stable context and schema identifiers of the metadata models.
- **[Schema.org](https://schema.org/)** as the target vocabulary for JSON-LD output

### Workflow Summary

flowchart TD
    A[Fill in CSV templates<br/>(e.g. Dataset.csv, Person.csv)] --> B[Commit changes to GitHub<br/>Triggers GitHub Actions]
    B --> C[Download JSON-LD artifact<br/>from GitHub Actions build]
    C --> D[Host JSON-LD file<br/>at a public web location]
    D --> E[Register JSON-LD endpoint<br/>with ODIS catalog]


1. Fill in CSV templates (e.g. `Dataset.csv`, `Person.csv`)
2. Commit changes; this kicks off GitHub Actions.
3. Download the JSON-LD files as an 'artifact' from the GitHub Action.
4. Make the JSON-LD publicly available on the internet as metadata for your resource (e.g. dataset)
5. Register the JSON-LD endpoint with [ODIS](https://catalog.odis.org)

### Getting Started (No Installation Required)
You can contribute metadata to MARCO-BOLO directly in your browser — no need to install anything locally.

1. Create a GitHub Account
Go to https://github.com/signup and create a free GitHub account.

Contact the Work Package 1 (WP1) team to be added to the MARCO-BOLO organization and granted editing permissions. You won’t be able to contribute metadata until this is done.

2. Set Up Your GitHub.dev Environment
To edit metadata CSV files in a spreadsheet-like view:

Open the recommended GitHub.dev profile.

Click the “Create” button.

If prompted, trust and install the “Excel Viewer” extension from MESCIUS. This enables spreadsheet-style editing of CSV files.

Tick the box: “Use this profile as the default for new windows”.

This configures your browser to open CSVs with a table-based view.

3. Edit Metadata in the Repo
Open the MARCO-BOLO metadata editor:
https://github.dev/marco-bolo/csv-to-json-ld/tree/wp1-playground

Sign in to GitHub when prompted and authorize GitHub.dev to access your account.

Browse to the relevant CSV file (e.g., Dataset.csv, Person.csv) and make edits using the table view.

4. Commit and Push Your Changes
Go to the Source Control view (left-hand sidebar).

Enter a short message describing your edits.

Click the + to stage your changes.

Click “Commit & Push”.

This will trigger an automatic build of your metadata on GitHub Actions.

5. Confirm Your Edits Were Valid
In the GitHub repository, switch to your working branch (e.g., wp1-playground).

Look for a build called validate-csvws-build-jsonld.

A green check mark means your changes passed validation.
A red cross means there were errors — contact the WP1 team for help.

6. Download Your JSON-LD Output
In the build results, click “Details” on the validate-csvws-build-jsonld job.

In the summary view, download the ZIP artifact that contains the generated JSON-LD files.

Note: These artifacts are temporary and will expire after 90 days. Be sure to store the files elsewhere for long-term access.

## Hosting and Registration

To make your metadata discoverable by ODIS:

1. **Host the generated JSON-LD** at a stable public URL (e.g., through GitHub Pages).
2. **Register the URL with ODIS** so it can be harvested and indexed.

## 📚 Documentation & Resources

- [Rendered model documentation](http://lab.marcobolo-project.eu/csv-to-json-ld/index.html)
- CSV template and schema definitions in `/model/` and `/metadata/`
- Examples and outputs in `/examples/` and `/out/`

## Human Workflow

This tool supports, but does not replace, human responsibility:

| Step | Role |
|------|------|
| Fill CSV templates | Data managers |
| Maintain CSV-W metadata | Data managers |
| Run validation and generation | Data managers or CI |
| Host and register JSON-LD | Data managers |

## License

This project is open source and licensed under the MIT License.