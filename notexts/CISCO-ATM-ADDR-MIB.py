#
# PySNMP MIB module CISCO-ATM-ADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-ADDR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoAtmAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 12))
ciscoAtmAddrMIB.setRevisions(('1996-05-06 00:00',))
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setLastUpdated('9605060000Z')
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setOrganization('Cisco Systems, Inc.')
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
ciscoAtmAddrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 1))
ciscoAtmIfAdminAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1), )
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrTable.setStatus('current')
ciscoAtmIfAdminAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrAddress"))
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrEntry.setStatus('current')
ciscoAtmIfAdminAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 1), AtmAddr())
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrAddress.setStatus('current')
ciscoAtmIfAdminAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrRowStatus.setStatus('current')
ciscoAtmIfAdminAddrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3))
ciscoAtmIfAdminAddrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1))
ciscoAtmIfAdminAddrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2))
ciscoAtmIfAdminAddrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1, 1)).setObjects(("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfAdminAddrMIBCompliance = ciscoAtmIfAdminAddrMIBCompliance.setStatus('current')
ciscoAtmIfAdminAddrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2, 1)).setObjects(("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfAdminAddrMIBGroup = ciscoAtmIfAdminAddrMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-ADDR-MIB", ciscoAtmIfAdminAddrTable=ciscoAtmIfAdminAddrTable, ciscoAtmIfAdminAddrAddress=ciscoAtmIfAdminAddrAddress, ciscoAtmAddrMIB=ciscoAtmAddrMIB, ciscoAtmIfAdminAddrMIBConformance=ciscoAtmIfAdminAddrMIBConformance, ciscoAtmIfAdminAddrMIBCompliance=ciscoAtmIfAdminAddrMIBCompliance, ciscoAtmAddrMIBObjects=ciscoAtmAddrMIBObjects, ciscoAtmIfAdminAddrEntry=ciscoAtmIfAdminAddrEntry, AtmAddr=AtmAddr, ciscoAtmIfAdminAddrMIBCompliances=ciscoAtmIfAdminAddrMIBCompliances, ciscoAtmIfAdminAddrMIBGroup=ciscoAtmIfAdminAddrMIBGroup, PYSNMP_MODULE_ID=ciscoAtmAddrMIB, ciscoAtmIfAdminAddrRowStatus=ciscoAtmIfAdminAddrRowStatus, ciscoAtmIfAdminAddrMIBGroups=ciscoAtmIfAdminAddrMIBGroups)
