#
# PySNMP MIB module CISCO-P-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-P-BRIDGE-CAPABILITY
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
TimeInterval, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "DisplayString", "TextualConvention")
ciscoPBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 385))
ciscoPBridgeCapability.setRevisions(('2004-01-14 00:00',))
if mibBuilder.loadTexts: ciscoPBridgeCapability.setLastUpdated('200401140000Z')
if mibBuilder.loadTexts: ciscoPBridgeCapability.setOrganization('Cisco Systems, Inc.')
ciscoPBridgeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 385, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPBridgeCapCatOSV08R0301 = ciscoPBridgeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPBridgeCapCatOSV08R0301 = ciscoPBridgeCapCatOSV08R0301.setStatus('current')
mibBuilder.exportSymbols("CISCO-P-BRIDGE-CAPABILITY", PYSNMP_MODULE_ID=ciscoPBridgeCapability, ciscoPBridgeCapCatOSV08R0301=ciscoPBridgeCapCatOSV08R0301, ciscoPBridgeCapability=ciscoPBridgeCapability)
