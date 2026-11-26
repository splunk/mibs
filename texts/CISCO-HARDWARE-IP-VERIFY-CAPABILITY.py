#
# PySNMP MIB module CISCO-HARDWARE-IP-VERIFY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HARDWARE-IP-VERIFY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
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
ciscoHardwareIpVerifyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 623))
ciscoHardwareIpVerifyCapability.setRevisions(('2013-07-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setDescription('Agent capabilities for CISCO-HARDWARE-IP-VERIFY-MIB.')
chivCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 623, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chivCapNxOSV06R0104PN7k = chivCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus \n                        7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chivCapNxOSV06R0104PN7k = chivCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: chivCapNxOSV06R0104PN7k.setDescription('CISCO-HARDWARE-IP-VERIFY-MIB\n        agent capabilities.')
mibBuilder.exportSymbols("CISCO-HARDWARE-IP-VERIFY-CAPABILITY", chivCapNxOSV06R0104PN7k=chivCapNxOSV06R0104PN7k, ciscoHardwareIpVerifyCapability=ciscoHardwareIpVerifyCapability, PYSNMP_MODULE_ID=ciscoHardwareIpVerifyCapability)
