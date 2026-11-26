#
# PySNMP MIB module CISCO-MOBILE-IP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MOBILE-IP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoMobileIPCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 449))
ciscoMobileIPCapability.setRevisions(('2005-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMobileIPCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMobileIPCapability.setLastUpdated('200509090000Z')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setContactInfo('       Cisco Systems\n                         Customer Service\n                        \n                 Postal: 170 West Tasman Drive\n                         San Jose, CA  95134\n                         USA\n                        \n                    Tel: +1 800 553-NETS\n                        \n                 E-mail: cs-mobileip@cisco.com')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setDescription('Agent capabilities for CISCO-MOBILE-IP-MIB \n                 (MobileIP MIB).')
ciscoMobileIPCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 449, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobileIPCapabilityV12R04 = ciscoMobileIPCapabilityV12R04.setProductRelease('Cisco IOS 12.4(3)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobileIPCapabilityV12R04 = ciscoMobileIPCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoMobileIPCapabilityV12R04.setDescription('Cisco MobileIP mib capabilities')
mibBuilder.exportSymbols("CISCO-MOBILE-IP-CAPABILITY", PYSNMP_MODULE_ID=ciscoMobileIPCapability, ciscoMobileIPCapability=ciscoMobileIPCapability, ciscoMobileIPCapabilityV12R04=ciscoMobileIPCapabilityV12R04)
