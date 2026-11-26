#
# PySNMP MIB module CISCO-GPRS-GTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GPRS-GTP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cgprsGtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 212))
cgprsGtpCapability.setRevisions(('2001-12-20 16:00', '2001-06-05 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cgprsGtpCapability.setRevisionsDescriptions(('Updated information for cgprsGtpDroppedPktsMonTime.\n                ', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cgprsGtpCapability.setLastUpdated('200112201600Z')
if mibBuilder.loadTexts: cgprsGtpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cgprsGtpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                                Tel: +1 800 553-NETS\n\n                        E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cgprsGtpCapability.setDescription('Agent capabilities for CISCO-GPRS-GTP-MIB')
cgprsGtpCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 212, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R01 = cgprsGtpCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R01 = cgprsGtpCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: cgprsGtpCapabilityV12R01.setDescription('Cisco GPRS GTP MIB capabilities.')
cgprsGtpCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 212, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R02 = cgprsGtpCapabilityV12R02.setProductRelease('Cisco IOS 12.2(7)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R02 = cgprsGtpCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: cgprsGtpCapabilityV12R02.setDescription('Cisco GPRS GTP MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GPRS-GTP-CAPABILITY", cgprsGtpCapability=cgprsGtpCapability, cgprsGtpCapabilityV12R02=cgprsGtpCapabilityV12R02, PYSNMP_MODULE_ID=cgprsGtpCapability, cgprsGtpCapabilityV12R01=cgprsGtpCapabilityV12R01)
