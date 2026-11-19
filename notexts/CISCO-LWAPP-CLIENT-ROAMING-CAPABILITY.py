#
# PySNMP MIB module CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY
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
TimeInterval, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "DisplayString")
ciscoLwappClientRoamingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 501))
ciscoLwappClientRoamingCapability.setRevisions(('2010-02-06 00:00', '2006-05-09 00:00',))
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setLastUpdated('201002060000Z')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappClientRoamingCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 501, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV4R0 = ciscoLwappClientRoamingCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV4R0 = ciscoLwappClientRoamingCapabilityCUWNSV4R0.setStatus('current')
ciscoLwappClientRoamingCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 501, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV7R0 = ciscoLwappClientRoamingCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV7R0 = ciscoLwappClientRoamingCapabilityCUWNSV7R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY", ciscoLwappClientRoamingCapabilityCUWNSV4R0=ciscoLwappClientRoamingCapabilityCUWNSV4R0, PYSNMP_MODULE_ID=ciscoLwappClientRoamingCapability, ciscoLwappClientRoamingCapability=ciscoLwappClientRoamingCapability, ciscoLwappClientRoamingCapabilityCUWNSV7R0=ciscoLwappClientRoamingCapabilityCUWNSV7R0)
