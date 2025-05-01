# submerge

A CLI tool for DIVE development.

## DIVE system

### Definition of DIVE

DIVE can be many things.

* DIVE := ! (DIVE is a VIBE Experience)

* DIV := DIV is not VIBE

* DIV := DIV Environments

* DIVE (Dynamically Interactive Virtual Environments) is a system for creating interactive environments that can be manipulated by AI agents. It allows for the creation of complex, dynamic environments that can be used for training and testing AI agents.


### Design

`submerge` is a prototype of a DIVE system that is:

- *Composable* (prompt layering)

- *Context-aware* (based on where you call it)
  
- *Reproducible* (full prompt-response chain stored)

- *Human-in-the-loop* (slow mode instead of raw agent autonomy)

- *Auditable* (you can track prompt lineage and decision paths)

- *Git-friendly* (purely file-based, versionable, portable)

A real AI DevOps stack (without making the human obsolete!)
