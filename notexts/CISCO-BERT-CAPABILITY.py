#
# PySNMP MIB module CISCO-BERT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BERT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
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
mibBuilder.exportSymbols("CISCO-BERT-CAPABILITY", ciscoBertAxsmeCapabilityV3R00=ciscoBertAxsmeCapabilityV3R00, PYSNMP_MODULE_ID=ciscoBertCapability, ciscoBertCapabilityV5R00=ciscoBertCapabilityV5R00, ciscoBertCapabilityV5R015=ciscoBertCapabilityV5R015, ciscoBertCapability=ciscoBertCapability)
