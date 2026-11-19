#
# PySNMP MIB module CISCO-HARDWARE-IP-VERIFY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HARDWARE-IP-VERIFY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHardwareIpVerifyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 623))
ciscoHardwareIpVerifyCapability.setRevisions(('2013-07-26 00:00',))
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setOrganization('Cisco Systems, Inc.')
chivCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 623, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chivCapNxOSV06R0104PN7k = chivCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus \n                        7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chivCapNxOSV06R0104PN7k = chivCapNxOSV06R0104PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-HARDWARE-IP-VERIFY-CAPABILITY", ciscoHardwareIpVerifyCapability=ciscoHardwareIpVerifyCapability, PYSNMP_MODULE_ID=ciscoHardwareIpVerifyCapability, chivCapNxOSV06R0104PN7k=chivCapNxOSV06R0104PN7k)
