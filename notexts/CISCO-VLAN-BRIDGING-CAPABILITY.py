#
# PySNMP MIB module CISCO-VLAN-BRIDGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VLAN-BRIDGING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoVlanBridgingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 339))
ciscoVlanBridgingCapability.setRevisions(('2004-06-11 00:00',))
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setLastUpdated('200406110000Z')
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setOrganization('Cisco Systems, Inc.')
cVlanBridgingCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 339, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0101 = cVlanBridgingCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0101 = cVlanBridgingCapCatOSV08R0101.setStatus('current')
cVlanBridgingCapCatOSV08R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 339, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0201 = cVlanBridgingCapCatOSV08R0201.setProductRelease('Cisco CatOS 8.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0201 = cVlanBridgingCapCatOSV08R0201.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-BRIDGING-CAPABILITY", ciscoVlanBridgingCapability=ciscoVlanBridgingCapability, PYSNMP_MODULE_ID=ciscoVlanBridgingCapability, cVlanBridgingCapCatOSV08R0101=cVlanBridgingCapCatOSV08R0101, cVlanBridgingCapCatOSV08R0201=cVlanBridgingCapCatOSV08R0201)
