#
# PySNMP MIB module CISCOSB-LBD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-LBD-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlLbd = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127))
rlLbd.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: rlLbd.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlLbd.setOrganization('Cisco Systems, Inc.')
rlLbdEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdEnable.setStatus('current')
rlLbdDetectionInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdDetectionInterval.setStatus('current')
rlLbdMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("source-mac-addr", 1), ("base-mac-addr", 2), ("broadcast-mac-addr", 3), ("predefined-multicast-mac-addr", 4), ("user-defined-mac-addr", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdMode.setStatus('current')
rlLbdPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4), )
if mibBuilder.loadTexts: rlLbdPortTable.setStatus('current')
rlLbdPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlLbdPortEntry.setStatus('current')
rlLbdPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLbdPortAdminStatus.setStatus('current')
rlLbdPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2), ("loopDetected", 3))).clone('inactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLbdPortOperStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-LBD-MIB", rlLbd=rlLbd, rlLbdDetectionInterval=rlLbdDetectionInterval, rlLbdPortTable=rlLbdPortTable, rlLbdPortOperStatus=rlLbdPortOperStatus, rlLbdMode=rlLbdMode, rlLbdEnable=rlLbdEnable, rlLbdPortEntry=rlLbdPortEntry, rlLbdPortAdminStatus=rlLbdPortAdminStatus, PYSNMP_MODULE_ID=rlLbd)
