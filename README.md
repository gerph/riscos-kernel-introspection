# Kernel introspection

This repository contains a RISC OS module that implements selected kernel and
platform-introspection interfaces. It provides `OS_ReadSysInfo`,
`OS_PlatformFeatures`, memory-map, and `OS_Memory` handling, and claims the
corresponding OS SWIs when configured to do so.

The project includes generated CPU-register definitions and regression tests
for the command's output.
