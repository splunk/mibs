#
# PySNMP MIB module CISCO-IGMP-FILTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IGMP-FILTER-CAPABILITY
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
ciscoIgmpFilterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 331))
ciscoIgmpFilterCapability.setRevisions(('2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setDescription('The capabilities description of\n                 CISCO-IGMP-FILTER-MIB.')
cIgmpFilterCapCatOSV07R0101Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 331, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIgmpFilterCapCatOSV07R0101Cat4k = cIgmpFilterCapCatOSV07R0101Cat4k.setProductRelease('Cisco CatOS 7.1(1) on Catalyst 4000/4500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIgmpFilterCapCatOSV07R0101Cat4k = cIgmpFilterCapCatOSV07R0101Cat4k.setStatus('current')
if mibBuilder.loadTexts: cIgmpFilterCapCatOSV07R0101Cat4k.setDescription('CISCO-IGMP-FILTER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IGMP-FILTER-CAPABILITY", PYSNMP_MODULE_ID=ciscoIgmpFilterCapability, ciscoIgmpFilterCapability=ciscoIgmpFilterCapability, cIgmpFilterCapCatOSV07R0101Cat4k=cIgmpFilterCapCatOSV07R0101Cat4k)
