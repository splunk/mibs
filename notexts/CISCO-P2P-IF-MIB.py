#
# PySNMP MIB module CISCO-P2P-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-P2P-IF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoP2PIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 668))
ciscoP2PIfMIB.setRevisions(('2008-08-12 00:00',))
if mibBuilder.loadTexts: ciscoP2PIfMIB.setLastUpdated('200808120000Z')
if mibBuilder.loadTexts: ciscoP2PIfMIB.setOrganization('Cisco Systems, Inc.')
ciscoP2PIfMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 0))
ciscoP2PIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 1))
cp2pIfGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1))
class Cp2pIfCrcMode(TextualConvention, Integer32):
    reference = 'RFC-2615, PPP over SONET/SDH: Section 5. Configuration Details.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("crc16", 1), ("crc32", 2))

class Cp2pIfScramblingMode(TextualConvention, Integer32):
    reference = 'RFC-2615, PPP over SONET/SDH: Section 4. X**43 + 1 Scrambler Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

cp2pIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1), )
if mibBuilder.loadTexts: cp2pIfCfgTable.setStatus('current')
cp2pIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cp2pIfCfgEntry.setStatus('current')
cp2pIfCfgCrcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 1), Cp2pIfCrcMode().clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgCrcMode.setStatus('current')
cp2pIfCfgScramblingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 2), Cp2pIfScramblingMode().clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgScramblingMode.setStatus('current')
cp2pIfCfgTransmitDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 18000))).setUnits('microseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgTransmitDelay.setStatus('current')
cp2pIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2), )
if mibBuilder.loadTexts: cp2pIfStatsTable.setStatus('current')
cp2pIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1), )
cp2pIfCfgEntry.registerAugmentions(("CISCO-P2P-IF-MIB", "cp2pIfStatsEntry"))
cp2pIfStatsEntry.setIndexNames(*cp2pIfCfgEntry.getIndexNames())
if mibBuilder.loadTexts: cp2pIfStatsEntry.setStatus('current')
cp2pIfStatsInCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cp2pIfStatsInCrcErrors.setStatus('current')
ciscoP2PIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3))
ciscoP2PIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1))
ciscoP2PIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2))
ciscoP2PIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1, 1)).setObjects(("CISCO-P2P-IF-MIB", "ciscoP2PIfMIBGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2PIfMIBCompliance = ciscoP2PIfMIBCompliance.setStatus('current')
ciscoP2PIfMIBGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2, 1)).setObjects(("CISCO-P2P-IF-MIB", "cp2pIfCfgCrcMode"), ("CISCO-P2P-IF-MIB", "cp2pIfCfgScramblingMode"), ("CISCO-P2P-IF-MIB", "cp2pIfCfgTransmitDelay"), ("CISCO-P2P-IF-MIB", "cp2pIfStatsInCrcErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2PIfMIBGeneralGroup = ciscoP2PIfMIBGeneralGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-P2P-IF-MIB", ciscoP2PIfMIBNotifs=ciscoP2PIfMIBNotifs, cp2pIfStatsEntry=cp2pIfStatsEntry, PYSNMP_MODULE_ID=ciscoP2PIfMIB, ciscoP2PIfMIBObjects=ciscoP2PIfMIBObjects, cp2pIfStatsTable=cp2pIfStatsTable, Cp2pIfScramblingMode=Cp2pIfScramblingMode, ciscoP2PIfMIBCompliances=ciscoP2PIfMIBCompliances, cp2pIfCfgTransmitDelay=cp2pIfCfgTransmitDelay, cp2pIfGeneralObjects=cp2pIfGeneralObjects, ciscoP2PIfMIBGeneralGroup=ciscoP2PIfMIBGeneralGroup, cp2pIfCfgTable=cp2pIfCfgTable, ciscoP2PIfMIBConformance=ciscoP2PIfMIBConformance, cp2pIfStatsInCrcErrors=cp2pIfStatsInCrcErrors, Cp2pIfCrcMode=Cp2pIfCrcMode, ciscoP2PIfMIB=ciscoP2PIfMIB, ciscoP2PIfMIBCompliance=ciscoP2PIfMIBCompliance, cp2pIfCfgCrcMode=cp2pIfCfgCrcMode, cp2pIfCfgScramblingMode=cp2pIfCfgScramblingMode, ciscoP2PIfMIBGroups=ciscoP2PIfMIBGroups, cp2pIfCfgEntry=cp2pIfCfgEntry)
