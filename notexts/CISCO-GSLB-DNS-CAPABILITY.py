#
# PySNMP MIB module CISCO-GSLB-DNS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GSLB-DNS-CAPABILITY
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
ciscoGslbDnsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 535))
ciscoGslbDnsCapability.setRevisions(('2009-03-18 00:00', '2007-02-23 00:00',))
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setLastUpdated('200903180000Z')
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setOrganization('Cisco Systems, Inc.')
ciscoGslbDnsCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 535, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV02R00 = ciscoGslbDnsCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV02R00 = ciscoGslbDnsCapabilityV02R00.setStatus('current')
ciscoGslbDnsCapabilityV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 535, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV03R01 = ciscoGslbDnsCapabilityV03R01.setProductRelease('GSS 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV03R01 = ciscoGslbDnsCapabilityV03R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-GSLB-DNS-CAPABILITY", ciscoGslbDnsCapabilityV02R00=ciscoGslbDnsCapabilityV02R00, PYSNMP_MODULE_ID=ciscoGslbDnsCapability, ciscoGslbDnsCapabilityV03R01=ciscoGslbDnsCapabilityV03R01, ciscoGslbDnsCapability=ciscoGslbDnsCapability)
