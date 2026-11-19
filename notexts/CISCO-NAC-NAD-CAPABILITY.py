#
# PySNMP MIB module CISCO-NAC-NAD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NAC-NAD-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoNacNadCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 440))
ciscoNacNadCapability.setRevisions(('2008-11-10 00:00', '2008-07-17 00:00', '2006-12-12 00:00', '2005-07-01 00:00',))
if mibBuilder.loadTexts: ciscoNacNadCapability.setLastUpdated('200811100000Z')
if mibBuilder.loadTexts: ciscoNacNadCapability.setOrganization('Cisco Systems, Inc.')
ciscoNacNadCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0501 = ciscoNacNadCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0501 = ciscoNacNadCapCatOSV08R0501.setStatus('current')
ciscoNacNadCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0601 = ciscoNacNadCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0601 = ciscoNacNadCapCatOSV08R0601.setStatus('current')
ciscoNacNadCapCatOSV08R0701 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0701 = ciscoNacNadCapCatOSV08R0701.setProductRelease('Cisco CatOS 8.7(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0701 = ciscoNacNadCapCatOSV08R0701.setStatus('current')
ciscoNacNadCapV12R0246SECat3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapV12R0246SECat3k = ciscoNacNadCapV12R0246SECat3k.setProductRelease('Cisco IOS 12.2(46)SE on Catalyst 3750.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapV12R0246SECat3k = ciscoNacNadCapV12R0246SECat3k.setStatus('current')
mibBuilder.exportSymbols("CISCO-NAC-NAD-CAPABILITY", ciscoNacNadCapCatOSV08R0701=ciscoNacNadCapCatOSV08R0701, ciscoNacNadCapability=ciscoNacNadCapability, ciscoNacNadCapCatOSV08R0501=ciscoNacNadCapCatOSV08R0501, PYSNMP_MODULE_ID=ciscoNacNadCapability, ciscoNacNadCapCatOSV08R0601=ciscoNacNadCapCatOSV08R0601, ciscoNacNadCapV12R0246SECat3k=ciscoNacNadCapV12R0246SECat3k)
