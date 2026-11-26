#
# PySNMP MIB module CISCO-BULK-FILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BULK-FILE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
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
mibBuilder.exportSymbols("CISCO-BULK-FILE-CAPABILITY", ciscoBulkFileCapCRS1V2R0=ciscoBulkFileCapCRS1V2R0, ciscoBulkFileCapability=ciscoBulkFileCapability, ciscoBulkFileCapabilityV2R00=ciscoBulkFileCapabilityV2R00, ciscoBulkFileCapabilityV1R0=ciscoBulkFileCapabilityV1R0, PYSNMP_MODULE_ID=ciscoBulkFileCapability, ciscoBulkFileCapabilityV3R00=ciscoBulkFileCapabilityV3R00)
