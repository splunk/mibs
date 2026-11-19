#
# PySNMP MIB module CISCO-IGMP-FILTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IGMP-FILTER-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIgmpFilterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 331))
ciscoIgmpFilterCapability.setRevisions(('2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setOrganization('Cisco Systems, Inc.')
cIgmpFilterCapCatOSV07R0101Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 331, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIgmpFilterCapCatOSV07R0101Cat4k = cIgmpFilterCapCatOSV07R0101Cat4k.setProductRelease('Cisco CatOS 7.1(1) on Catalyst 4000/4500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIgmpFilterCapCatOSV07R0101Cat4k = cIgmpFilterCapCatOSV07R0101Cat4k.setStatus('current')
mibBuilder.exportSymbols("CISCO-IGMP-FILTER-CAPABILITY", PYSNMP_MODULE_ID=ciscoIgmpFilterCapability, cIgmpFilterCapCatOSV07R0101Cat4k=cIgmpFilterCapCatOSV07R0101Cat4k, ciscoIgmpFilterCapability=ciscoIgmpFilterCapability)
