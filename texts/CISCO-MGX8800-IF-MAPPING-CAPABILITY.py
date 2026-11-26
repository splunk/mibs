#
# PySNMP MIB module CISCO-MGX8800-IF-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MGX8800-IF-MAPPING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMgx8800IfMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 278))
ciscoMgx8800IfMappingCapability.setRevisions(('2002-08-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setLastUpdated('200208010000Z')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setDescription('The Agent Capabilities for \n            CISCO-MGX8800-IF-MAPPING-MIB.\n\n            - The cmiMappingCapabilityMgxV3R00 is for \n              MGX8850 Release 3.0.00.\n\n            - The cmiMappingCapabilityRpmxfV12R02 is for\n              RPM-XF module.')
cmiMappingCapabilityMgxV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setStatus('current')
if mibBuilder.loadTexts: cmiMappingCapabilityMgxV3R00.setDescription('Agent capabilities for MGX8850.')
cmiMappingCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2(8)T2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setStatus('current')
if mibBuilder.loadTexts: cmiMappingCapabilityRpmxfV12R02.setDescription('Agent capabilities for RPM-XF\nmodule.')
mibBuilder.exportSymbols("CISCO-MGX8800-IF-MAPPING-CAPABILITY", cmiMappingCapabilityRpmxfV12R02=cmiMappingCapabilityRpmxfV12R02, PYSNMP_MODULE_ID=ciscoMgx8800IfMappingCapability, ciscoMgx8800IfMappingCapability=ciscoMgx8800IfMappingCapability, cmiMappingCapabilityMgxV3R00=cmiMappingCapabilityMgxV3R00)
