#
# PySNMP MIB module CISCO-LWAPP-SYS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-SYS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappSysCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 3333))
ciscoLwappSysCapability.setRevisions(('2010-08-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappSysCapability.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappSysCapability.setLastUpdated('201008170000Z')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setDescription('Agent capabilities for CISCO-LWAPP-SYS-MIB.')
ciscoLwappSysCapabilityCUWNSR7V0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.0 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappSysCapabilityCUWNSR7V0.setDescription('CISCO-LWAPP-SYS-MIB capabilities')
ciscoLwappSysCapabilityCUWNSR7V2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.2 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappSysCapabilityCUWNSR7V2.setDescription('CISCO-LWAPP-SYS-MIB capabilities')
mibBuilder.exportSymbols("CISCO-LWAPP-SYS-CAPABILITY", ciscoLwappSysCapabilityCUWNSR7V0=ciscoLwappSysCapabilityCUWNSR7V0, ciscoLwappSysCapability=ciscoLwappSysCapability, ciscoLwappSysCapabilityCUWNSR7V2=ciscoLwappSysCapabilityCUWNSR7V2, PYSNMP_MODULE_ID=ciscoLwappSysCapability)
