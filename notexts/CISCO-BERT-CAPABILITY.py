#
# PySNMP MIB module CISCO-BERT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BERT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBertCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 274))
ciscoBertCapability.setRevisions(('2004-08-07 00:00', '2003-12-22 00:00', '2003-09-19 00:00', '2002-10-30 00:00', '2002-06-11 00:00',))
if mibBuilder.loadTexts: ciscoBertCapability.setLastUpdated('200408070000Z')
if mibBuilder.loadTexts: ciscoBertCapability.setOrganization('Cisco Systems, Inc.')
ciscoBertAxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertAxsmeCapabilityV3R00 = ciscoBertAxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertAxsmeCapabilityV3R00 = ciscoBertAxsmeCapabilityV3R00.setStatus('current')
ciscoBertCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R00 = ciscoBertCapabilityV5R00.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R00 = ciscoBertCapabilityV5R00.setStatus('current')
ciscoBertCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R015 = ciscoBertCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R015 = ciscoBertCapabilityV5R015.setStatus('current')
mibBuilder.exportSymbols("CISCO-BERT-CAPABILITY", ciscoBertCapabilityV5R015=ciscoBertCapabilityV5R015, ciscoBertAxsmeCapabilityV3R00=ciscoBertAxsmeCapabilityV3R00, ciscoBertCapability=ciscoBertCapability, PYSNMP_MODULE_ID=ciscoBertCapability, ciscoBertCapabilityV5R00=ciscoBertCapabilityV5R00)
