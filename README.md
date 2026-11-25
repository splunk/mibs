# mibs
This MIB Repository is based on the original repository provided by snmplabs with updates from the mib collection from librenms.
This repository was forked from https://github.com/pysnmp/mibs.
In addition, an index is published allowing remote clients to identify a mib based on OID alone. All hosted on github pages.


pysnmplib (formerly pysnmp) applications can retrieve mibs from `https://splunk.github.io/mibs/asn1/@mib@`

## Python and container builds

Use Python 3.13 or 3.14 to compile MIBs and generate the index when building locally. CI builds and container images use Python 3.13 with Poetry 2.5.2.

## IPv6 listeners

IPv6 listener support is disabled by default. Enabling it adds IPv6 listeners while preserving the existing IPv4 listeners on both endpoints:

- MIB content: TCP/8000
- NGINX status and readiness: TCP/8080
