#
# PySNMP MIB module CISCO-RFC1407-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RFC1407-CAPABILITY
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
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRFC1407Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 102))
ciscoRFC1407Capability.setRevisions(('2001-08-17 00:00', '1996-06-19 00:00',))
if mibBuilder.loadTexts: ciscoRFC1407Capability.setLastUpdated('200108170000Z')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setOrganization('Cisco Systems, Inc.')
ciscoRFC1407CapabilityV11R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV11R02 = ciscoRFC1407CapabilityV11R02.setProductRelease('Cisco IOS 11.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV11R02 = ciscoRFC1407CapabilityV11R02.setStatus('current')
ciscoRFC1407CapabilityV122R12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV122R12 = ciscoRFC1407CapabilityV122R12.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV122R12 = ciscoRFC1407CapabilityV122R12.setStatus('current')
mibBuilder.exportSymbols("CISCO-RFC1407-CAPABILITY", ciscoRFC1407CapabilityV11R02=ciscoRFC1407CapabilityV11R02, ciscoRFC1407Capability=ciscoRFC1407Capability, ciscoRFC1407CapabilityV122R12=ciscoRFC1407CapabilityV122R12, PYSNMP_MODULE_ID=ciscoRFC1407Capability)
