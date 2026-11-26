#
# PySNMP MIB module CISCO-P2P-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-P2P-IF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoP2PIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 668))
ciscoP2PIfMIB.setRevisions(('2008-08-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoP2PIfMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoP2PIfMIB.setLastUpdated('200808120000Z')
if mibBuilder.loadTexts: ciscoP2PIfMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoP2PIfMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W. Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: q-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoP2PIfMIB.setDescription('The Point to Point Interface MIB module.\n        This MIB manages the generic objects for\n        Serial link or SONET/SDH like point to point network \n        interfaces with the encapsulations of PPP \n        (Point to Point Protocol), HDLC (High Level Data Link Control)\n        or cHDLC (CIsco extension to High Level Data Link Control) \n        framing.\n        Acronyms and terms:\n        FCS - Frame Check Sequence. The frame check sequence is \n              used to ensure that the data received is actually \n              the data sent.\n        CRC - Cyclic Redundancy Check. The transmitting system \n              processes the frame check sequence portion of the \n              frame through an algorithm called a CRC (Cyclic \n              Redundancy Check).\n\n        One of the usages of CRC is in the following \n        PPP/HLDC over SONET/SDH example.\n        +----+\n        | PPP|   FCS           Bit                      SONET/SDH\n        |HDLC|=> Generation => Stuffing => Scrambling => Framing\n        +----+   CRC 16,32')
ciscoP2PIfMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 0))
ciscoP2PIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 1))
cp2pIfGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1))
class Cp2pIfCrcMode(TextualConvention, Integer32):
    reference = 'RFC-2615, PPP over SONET/SDH: Section 5. Configuration \n        Details.'
    description = 'Specifies the CRC mode of Cyclic Redundancy Check.\n        crc16 - 16-bit CRC.\n        crc32 - 32-bit CRC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("crc16", 1), ("crc32", 2))

class Cp2pIfScramblingMode(TextualConvention, Integer32):
    reference = 'RFC-2615, PPP over SONET/SDH: Section 4. X**43 + 1 \n        Scrambler Description.'
    description = 'An enumerated value of the Scrambling encryption mode of\n        an interface. \n        on  - scrambling encryption enabled.\n        off - scrambling encryption disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

cp2pIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1), )
if mibBuilder.loadTexts: cp2pIfCfgTable.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgTable.setDescription('The Point to Point generic Configuration Table. It contains\n        the standard configuration information of the Point to Point\n        interface.')
cp2pIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cp2pIfCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgEntry.setDescription('An entry in the configuration table for each Point to Point\n        interface. The entry is created when the Point to Point\n        related interface is created in ifTable.\n        The possible ifType of point to point interface are listed \n        as follows:\n        [1] ppp(23)\n        [2] hdlc(118)\n        [3] propPointToPointSerial(22)')
cp2pIfCfgCrcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 1), Cp2pIfCrcMode().clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgCrcMode.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgCrcMode.setDescription('Specifies the CRC mode for the FCS generation of a packet\n        sending via the Point to point interface.')
cp2pIfCfgScramblingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 2), Cp2pIfScramblingMode().clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgScramblingMode.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgScramblingMode.setDescription('Specifies the scrambling encryption mode of the point\n        to point interface.')
cp2pIfCfgTransmitDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 18000))).setUnits('microseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgTransmitDelay.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgTransmitDelay.setDescription("Specified the minimum delay after sending a packet via\n        the point to point interface. The value of '0' indicates \n        the transmit delay of packet is disabled.")
cp2pIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2), )
if mibBuilder.loadTexts: cp2pIfStatsTable.setStatus('current')
if mibBuilder.loadTexts: cp2pIfStatsTable.setDescription('The Point to Point Interface Statistics Table.  It contains\n        statistics information of a Point to Point interface\n        including the error statistics.')
cp2pIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1), )
cp2pIfCfgEntry.registerAugmentions(("CISCO-P2P-IF-MIB", "cp2pIfStatsEntry"))
cp2pIfStatsEntry.setIndexNames(*cp2pIfCfgEntry.getIndexNames())
if mibBuilder.loadTexts: cp2pIfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cp2pIfStatsEntry.setDescription('An entry in the statistics table for each Point to Point\n        interface.')
cp2pIfStatsInCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cp2pIfStatsInCrcErrors.setStatus('current')
if mibBuilder.loadTexts: cp2pIfStatsInCrcErrors.setDescription('Accumulated number of CRC errors that are detected on\n        the received packets via the Point to Point interface\n        since system startup.')
ciscoP2PIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3))
ciscoP2PIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1))
ciscoP2PIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2))
ciscoP2PIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1, 1)).setObjects(("CISCO-P2P-IF-MIB", "ciscoP2PIfMIBGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2PIfMIBCompliance = ciscoP2PIfMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoP2PIfMIBCompliance.setDescription('The compliance statement for entities which implement\n        the Cisco Point to Point interface MIB')
ciscoP2PIfMIBGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2, 1)).setObjects(("CISCO-P2P-IF-MIB", "cp2pIfCfgCrcMode"), ("CISCO-P2P-IF-MIB", "cp2pIfCfgScramblingMode"), ("CISCO-P2P-IF-MIB", "cp2pIfCfgTransmitDelay"), ("CISCO-P2P-IF-MIB", "cp2pIfStatsInCrcErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2PIfMIBGeneralGroup = ciscoP2PIfMIBGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2PIfMIBGeneralGroup.setDescription('The collection of objects providing general information\n        about the Cisco Point to Point interfaces.')
mibBuilder.exportSymbols("CISCO-P2P-IF-MIB", cp2pIfCfgScramblingMode=cp2pIfCfgScramblingMode, cp2pIfStatsEntry=cp2pIfStatsEntry, ciscoP2PIfMIB=ciscoP2PIfMIB, Cp2pIfScramblingMode=Cp2pIfScramblingMode, PYSNMP_MODULE_ID=ciscoP2PIfMIB, cp2pIfCfgCrcMode=cp2pIfCfgCrcMode, cp2pIfStatsInCrcErrors=cp2pIfStatsInCrcErrors, ciscoP2PIfMIBConformance=ciscoP2PIfMIBConformance, ciscoP2PIfMIBObjects=ciscoP2PIfMIBObjects, ciscoP2PIfMIBGeneralGroup=ciscoP2PIfMIBGeneralGroup, cp2pIfCfgTable=cp2pIfCfgTable, ciscoP2PIfMIBGroups=ciscoP2PIfMIBGroups, cp2pIfCfgEntry=cp2pIfCfgEntry, ciscoP2PIfMIBCompliances=ciscoP2PIfMIBCompliances, cp2pIfStatsTable=cp2pIfStatsTable, ciscoP2PIfMIBCompliance=ciscoP2PIfMIBCompliance, cp2pIfCfgTransmitDelay=cp2pIfCfgTransmitDelay, ciscoP2PIfMIBNotifs=ciscoP2PIfMIBNotifs, Cp2pIfCrcMode=Cp2pIfCrcMode, cp2pIfGeneralObjects=cp2pIfGeneralObjects)
