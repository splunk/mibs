#
# PySNMP MIB module CISCO-RMON2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RMON2-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
ciscoRmon2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 361))
ciscoRmon2Capability.setRevisions(('2003-10-01 00:00',))
if mibBuilder.loadTexts: ciscoRmon2Capability.setLastUpdated('200310010000Z')
if mibBuilder.loadTexts: ciscoRmon2Capability.setOrganization('Cisco Systems, Inc.')
ciscoRmon2CapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 361, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmon2CapCatOSV08R0101 = ciscoRmon2CapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmon2CapCatOSV08R0101 = ciscoRmon2CapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-RMON2-CAPABILITY", PYSNMP_MODULE_ID=ciscoRmon2Capability, ciscoRmon2Capability=ciscoRmon2Capability, ciscoRmon2CapCatOSV08R0101=ciscoRmon2CapCatOSV08R0101)
