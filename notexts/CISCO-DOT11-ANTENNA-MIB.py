#
# PySNMP MIB module CISCO-DOT11-ANTENNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-ANTENNA-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoDot11AntennaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 384))
ciscoDot11AntennaMIB.setRevisions(('2016-02-15 00:00', '2003-12-08 00:00',))
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setLastUpdated('201602150000Z')
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setOrganization('Cisco System Inc.')
cDot11AntennaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 1))
cDot11AntennaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1))
cDot11AntennaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1), )
if mibBuilder.loadTexts: cDot11AntennaTable.setStatus('current')
cDot11AntennaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cDot11AntennaEntry.setStatus('current')
cDot11AntennaIsGainConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AntennaIsGainConfigured.setStatus('current')
cDot11AntennaResultantGain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AntennaResultantGain.setStatus('current')
cDot11AntennaMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2))
cDot11AntennaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1))
cDot11AntennaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2))
cDot11AntennaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1, 1)).setObjects(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11AntennaMIBCompliance = cDot11AntennaMIBCompliance.setStatus('current')
cDot11AntennaGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2, 1)).setObjects(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaIsGainConfigured"), ("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaResultantGain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11AntennaGlobalGroup = cDot11AntennaGlobalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-ANTENNA-MIB", cDot11AntennaMIBCompliance=cDot11AntennaMIBCompliance, cDot11AntennaGlobalGroup=cDot11AntennaGlobalGroup, cDot11AntennaMIBCompliances=cDot11AntennaMIBCompliances, cDot11AntennaResultantGain=cDot11AntennaResultantGain, cDot11AntennaMIBGroups=cDot11AntennaMIBGroups, cDot11AntennaMIBObjects=cDot11AntennaMIBObjects, cDot11AntennaIsGainConfigured=cDot11AntennaIsGainConfigured, cDot11AntennaTable=cDot11AntennaTable, cDot11AntennaGlobal=cDot11AntennaGlobal, ciscoDot11AntennaMIB=ciscoDot11AntennaMIB, cDot11AntennaMIBConform=cDot11AntennaMIBConform, PYSNMP_MODULE_ID=ciscoDot11AntennaMIB, cDot11AntennaEntry=cDot11AntennaEntry)
