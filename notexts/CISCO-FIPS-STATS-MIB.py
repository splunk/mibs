#
# PySNMP MIB module CISCO-FIPS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FIPS-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFipsStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 999999))
ciscoFipsStatsMIB.setRevisions(('2003-03-10 00:00',))
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setLastUpdated('200303100000Z')
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setOrganization('Cisco Systems, Inc.')
ciscoFipsStatsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 0))
ciscoFipsStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1))
ciscoFipsStatsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2))
cfipsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1))
cfipsStatsGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1))
cfipsPostStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("running", 1), ("passed", 2), ("failed", 3), ("notAvailable", 4))).clone('notAvailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfipsPostStatus.setStatus('current')
ciscoFipsStatsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1))
ciscoFipsStatsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2))
ciscoFipsStatsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1, 1)).setObjects(("CISCO-FIPS-STATS-MIB", "ciscoFipsStatsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFipsStatsMIBCompliance = ciscoFipsStatsMIBCompliance.setStatus('current')
ciscoFipsStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 1)).setObjects(("CISCO-FIPS-STATS-MIB", "cfipsPostStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFipsStatsMIBGroup = ciscoFipsStatsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FIPS-STATS-MIB", ciscoFipsStatsMIBObjects=ciscoFipsStatsMIBObjects, ciscoFipsStatsMIBNotifs=ciscoFipsStatsMIBNotifs, cfipsPostStatus=cfipsPostStatus, PYSNMP_MODULE_ID=ciscoFipsStatsMIB, cfipsStatsGlobal=cfipsStatsGlobal, ciscoFipsStatsMIBGroup=ciscoFipsStatsMIBGroup, ciscoFipsStatsMIBGroups=ciscoFipsStatsMIBGroups, ciscoFipsStatsMIB=ciscoFipsStatsMIB, ciscoFipsStatsMIBCompliances=ciscoFipsStatsMIBCompliances, ciscoFipsStatsMIBConform=ciscoFipsStatsMIBConform, cfipsStats=cfipsStats, ciscoFipsStatsMIBCompliance=ciscoFipsStatsMIBCompliance)
