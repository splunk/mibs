#
# PySNMP MIB module CISCO-LWAPP-SYS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-SYS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappSysCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 3333))
ciscoLwappSysCapability.setRevisions(('2010-08-17 00:00',))
if mibBuilder.loadTexts: ciscoLwappSysCapability.setLastUpdated('201008170000Z')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappSysCapabilityCUWNSR7V0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.0 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setStatus('current')
ciscoLwappSysCapabilityCUWNSR7V2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.2 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-SYS-CAPABILITY", ciscoLwappSysCapabilityCUWNSR7V2=ciscoLwappSysCapabilityCUWNSR7V2, ciscoLwappSysCapabilityCUWNSR7V0=ciscoLwappSysCapabilityCUWNSR7V0, PYSNMP_MODULE_ID=ciscoLwappSysCapability, ciscoLwappSysCapability=ciscoLwappSysCapability)
