#
# PySNMP MIB module CISCO-MGX8800-IF-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MGX8800-IF-MAPPING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx8800IfMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 278))
ciscoMgx8800IfMappingCapability.setRevisions(('2002-08-01 00:00',))
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setLastUpdated('200208010000Z')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setOrganization('Cisco Systems, Inc.')
cmiMappingCapabilityMgxV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setStatus('current')
cmiMappingCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2(8)T2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX8800-IF-MAPPING-CAPABILITY", cmiMappingCapabilityMgxV3R00=cmiMappingCapabilityMgxV3R00, PYSNMP_MODULE_ID=ciscoMgx8800IfMappingCapability, cmiMappingCapabilityRpmxfV12R02=cmiMappingCapabilityRpmxfV12R02, ciscoMgx8800IfMappingCapability=ciscoMgx8800IfMappingCapability)
