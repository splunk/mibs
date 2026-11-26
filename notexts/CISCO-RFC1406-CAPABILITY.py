#
# PySNMP MIB module CISCO-RFC1406-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RFC1406-CAPABILITY
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
ciscoRFC1406Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 102))
ciscoRFC1406Capability.setRevisions(('2002-10-22 00:00', '2001-08-17 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRFC1406Capability.setLastUpdated('200210220000Z')
if mibBuilder.loadTexts: ciscoRFC1406Capability.setOrganization('Cisco Systems, Inc.')
ciscoRFC1406CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV10R02 = ciscoRFC1406CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV10R02 = ciscoRFC1406CapabilityV10R02.setStatus('current')
ciscoRFC1406CapabilityV122R12T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12T = ciscoRFC1406CapabilityV122R12T.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12T = ciscoRFC1406CapabilityV122R12T.setStatus('obsolete')
ciscoRFC1406CapabilityV122R12TRev2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12TRev2 = ciscoRFC1406CapabilityV122R12TRev2.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1406CapabilityV122R12TRev2 = ciscoRFC1406CapabilityV122R12TRev2.setStatus('current')
mibBuilder.exportSymbols("CISCO-RFC1406-CAPABILITY", ciscoRFC1406CapabilityV122R12T=ciscoRFC1406CapabilityV122R12T, PYSNMP_MODULE_ID=ciscoRFC1406Capability, ciscoRFC1406Capability=ciscoRFC1406Capability, ciscoRFC1406CapabilityV122R12TRev2=ciscoRFC1406CapabilityV122R12TRev2, ciscoRFC1406CapabilityV10R02=ciscoRFC1406CapabilityV10R02)
