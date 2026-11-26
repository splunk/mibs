#
# PySNMP MIB module CISCO-RS-232-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RS-232-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoRS232Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 115))
ciscoRS232Capability.setRevisions(('2002-05-16 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRS232Capability.setLastUpdated('200205160000Z')
if mibBuilder.loadTexts: ciscoRS232Capability.setOrganization('Cisco Systems, Inc.')
ciscoRS232CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setStatus('current')
ciscoRS232CapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setProductRelease('MGX8850 Release 2.0,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-RS-232-CAPABILITY", ciscoRS232Capability=ciscoRS232Capability, ciscoRS232CapabilityV10R02=ciscoRS232CapabilityV10R02, PYSNMP_MODULE_ID=ciscoRS232Capability, ciscoRS232CapabilityV2R00=ciscoRS232CapabilityV2R00)
