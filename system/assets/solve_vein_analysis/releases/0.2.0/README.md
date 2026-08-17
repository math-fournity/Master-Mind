# Solve-side cognitive-role assets 0.2.0

This release separates cognition from filesystem commit. The model may read only
the files named by its task and must return one marked JSON object in its final
response. It must not write files, execute commands, call MCP, or launch agents.

The trusted adapter extracts the marked JSON, parses it, canonicalizes it without
semantic changes, writes the role output, and creates the DONE hash marker.

This release was created in response to POC-VMS-32/33 protocol evidence. It does
not claim live capability until POC-VMS-34 is evaluated.
