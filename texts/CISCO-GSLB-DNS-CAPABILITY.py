#
# PySNMP MIB module CISCO-GSLB-DNS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GSLB-DNS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbDnsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 535))
ciscoGslbDnsCapability.setRevisions(('2009-03-18 00:00', '2007-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbDnsCapability.setRevisionsDescriptions(('Added ciscoGslbDnsCapabilityV03R01 agent\n        capabilities for Global Site Selector(GSS)\n        release 3.1(0).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setLastUpdated('200903180000Z')
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal:  170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel:  +1 800 553-NETS\n\n            E-mail:  cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setDescription('The capabilities description\n        of CISCO-GSLB-DNS-MIB.')
ciscoGslbDnsCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 535, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV02R00 = ciscoGslbDnsCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV02R00 = ciscoGslbDnsCapabilityV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbDnsCapabilityV02R00.setDescription('GSS 2.0 Cisco GSLB DNS MIB capabilities')
ciscoGslbDnsCapabilityV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 535, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV03R01 = ciscoGslbDnsCapabilityV03R01.setProductRelease('GSS 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV03R01 = ciscoGslbDnsCapabilityV03R01.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbDnsCapabilityV03R01.setDescription('GSS 3.1(0) Cisco GSLB DNS MIB capabilities')
mibBuilder.exportSymbols("CISCO-GSLB-DNS-CAPABILITY", ciscoGslbDnsCapabilityV02R00=ciscoGslbDnsCapabilityV02R00, ciscoGslbDnsCapabilityV03R01=ciscoGslbDnsCapabilityV03R01, ciscoGslbDnsCapability=ciscoGslbDnsCapability, PYSNMP_MODULE_ID=ciscoGslbDnsCapability)
