#
# PySNMP MIB module CISCO-LWAPP-WEBAUTH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-WEBAUTH-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappWebauthCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 5555))
ciscoLwappWebauthCapability.setRevisions(('2010-07-30 00:00',))
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setLastUpdated('201007300000Z')
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappWebAuthCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 5555, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWebAuthCapabilityCUWNSV7R0 = ciscoLwappWebAuthCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWebAuthCapabilityCUWNSV7R0 = ciscoLwappWebAuthCapabilityCUWNSV7R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-WEBAUTH-CAPABILITY", ciscoLwappWebauthCapability=ciscoLwappWebauthCapability, ciscoLwappWebAuthCapabilityCUWNSV7R0=ciscoLwappWebAuthCapabilityCUWNSV7R0, PYSNMP_MODULE_ID=ciscoLwappWebauthCapability)
