# Corpus Audit

## Corpus Scope

The V1 corpus contains 26 curated final investigation reports published by
the Aircraft Accident Investigation Bureau (AAIB), India.

The corpus is intended for the development and evaluation of an
evidence-grounded aviation investigation RAG system.

The corpus is curated for technical and investigative diversity. It is not
intended to represent all aviation accidents or establish statistical trends
across Indian aviation.

## Inclusion Criteria

A report is included when:

- It is an AAIB India investigation report.
- It is a final investigation report.
- It concerns a fixed-wing aircraft.
- It represents a commercial, scheduled, non-scheduled, charter, ambulance,
  government, or other accepted operational context within the finalized scope.
- The complete report PDF is available.
- The report contains sufficient textual evidence for retrieval and question
  answering.
- Its registration and occurrence details can be verified.

## Exclusion Criteria

A report is excluded when:

- Only a preliminary or interim report is available.
- It is a helicopter occurrence.
- It is a glider or microlight occurrence outside the selected scope.
- It is a training-flight occurrence outside the finalized corpus.
- The report is incomplete or unavailable.
- It duplicates another report already in the corpus.
- Its content is unsuitable for reliable evidence-grounded retrieval.

## Audit Checks

Each report must be checked for:

- [x] PDF opens successfully.
- [x] Report is marked as final.
- [x] Aircraft registration matches the manifest.
- [x] Aircraft type matches the manifest.
- [x] Operator matches the manifest.
- [x] Occurrence date matches the manifest.
- [x] Occurrence year matches the manifest.
- [x] Operation type has been verified.
- [x] Phase of flight has been verified.
- [x] Occurrence type has been verified.
- [x] Local filename follows the naming convention.
- [x] Report is not duplicated.
- [x] Official source is recorded.
- [x] Manifest entry is complete.