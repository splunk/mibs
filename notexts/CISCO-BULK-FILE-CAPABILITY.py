#
# PySNMP MIB module CISCO-BULK-FILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BULK-FILE-CAPABILITY
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
ciscoBulkFileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 188))
ciscoBulkFileCapability.setRevisions(('2006-02-06 00:00', '2003-11-13 00:00', '2002-02-17 00:00', '2000-12-04 00:00',))
if mibBuilder.loadTexts: ciscoBulkFileCapability.setLastUpdated('200602060000Z')
if mibBuilder.loadTexts: ciscoBulkFileCapability.setOrganization('Cisco Systems, Inc.')
ciscoBulkFileCapabilityV1R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV1R0 = ciscoBulkFileCapabilityV1R0.setProductRelease('Cisco IOS mc 1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV1R0 = ciscoBulkFileCapabilityV1R0.setStatus('current')
ciscoBulkFileCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV2R00 = ciscoBulkFileCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                          BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV2R00 = ciscoBulkFileCapabilityV2R00.setStatus('current')
ciscoBulkFileCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV3R00 = ciscoBulkFileCapabilityV3R00.setProductRelease('MGX8850 Release 3.00,\n                          BPX SES Release 3.00,\n                          VXSM  Release 5.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV3R00 = ciscoBulkFileCapabilityV3R00.setStatus('current')
ciscoBulkFileCapCRS1V2R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapCRS1V2R0 = ciscoBulkFileCapCRS1V2R0.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapCRS1V2R0 = ciscoBulkFileCapCRS1V2R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-BULK-FILE-CAPABILITY", PYSNMP_MODULE_ID=ciscoBulkFileCapability, ciscoBulkFileCapCRS1V2R0=ciscoBulkFileCapCRS1V2R0, ciscoBulkFileCapabilityV1R0=ciscoBulkFileCapabilityV1R0, ciscoBulkFileCapabilityV2R00=ciscoBulkFileCapabilityV2R00, ciscoBulkFileCapabilityV3R00=ciscoBulkFileCapabilityV3R00, ciscoBulkFileCapability=ciscoBulkFileCapability)
