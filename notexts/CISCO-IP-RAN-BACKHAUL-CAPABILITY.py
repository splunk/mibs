#
# PySNMP MIB module CISCO-IP-RAN-BACKHAUL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-RAN-BACKHAUL-CAPABILITY
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
ciscoIpRanBhCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 461))
ciscoIpRanBhCapability.setRevisions(('2010-07-14 00:00', '2005-09-15 00:00',))
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setLastUpdated('201007140000Z')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpRanBhCapabilityV12R0402MR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setProductRelease('Cisco IOS 12.4(2)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setStatus('current')
ciscoIpRanBhCapabilityV12R0412MR1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setProductRelease('Cisco IOS 12.4(12)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-RAN-BACKHAUL-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpRanBhCapability, ciscoIpRanBhCapabilityV12R0402MR=ciscoIpRanBhCapabilityV12R0402MR, ciscoIpRanBhCapabilityV12R0412MR1=ciscoIpRanBhCapabilityV12R0412MR1, ciscoIpRanBhCapability=ciscoIpRanBhCapability)
