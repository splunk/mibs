#
# PySNMP MIB module BASIS-RAS-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/BASIS-RAS-DISK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rasDsk = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6, 2))
rasDskStatus = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rasDskStatus.setStatus('mandatory')
dskHealth = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pass", 1), ("fail", 2), ("unknown", 3), ("testInProgress", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskHealth.setStatus('mandatory')
standbyDskHealth = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pass", 1), ("fail", 2), ("unknown", 3), ("testInProgress", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: standbyDskHealth.setStatus('mandatory')
wakeupInterval = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(12, 168)).clone(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wakeupInterval.setStatus('mandatory')
lastTime = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTime.setStatus('mandatory')
numBadSectors = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBadSectors.setStatus('mandatory')
crptdPRIfiles = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crptdPRIfiles.setStatus('mandatory')
crptdFWfiles = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crptdFWfiles.setStatus('mandatory')
mibBuilder.exportSymbols("BASIS-RAS-DISK-MIB", crptdFWfiles=crptdFWfiles, wakeupInterval=wakeupInterval, rasDsk=rasDsk, rasDskStatus=rasDskStatus, lastTime=lastTime, dskHealth=dskHealth, standbyDskHealth=standbyDskHealth, crptdPRIfiles=crptdPRIfiles, numBadSectors=numBadSectors)
