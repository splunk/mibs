#
# PySNMP MIB module CISCO-LWAPP-TSM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-TSM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappTsmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 506))
ciscoLwappTsmCapability.setRevisions(('2006-05-15 00:00',))
if mibBuilder.loadTexts: ciscoLwappTsmCapability.setLastUpdated('200605150000Z')
if mibBuilder.loadTexts: ciscoLwappTsmCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappTsmCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 506, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappTsmCapabilityCUWNSV4R0 = ciscoLwappTsmCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappTsmCapabilityCUWNSV4R0 = ciscoLwappTsmCapabilityCUWNSV4R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-TSM-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappTsmCapability, ciscoLwappTsmCapabilityCUWNSV4R0=ciscoLwappTsmCapabilityCUWNSV4R0, ciscoLwappTsmCapability=ciscoLwappTsmCapability)
