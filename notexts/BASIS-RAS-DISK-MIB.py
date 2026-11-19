#
# PySNMP MIB module BASIS-RAS-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/BASIS-RAS-DISK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("BASIS-RAS-DISK-MIB", lastTime=lastTime, crptdFWfiles=crptdFWfiles, rasDsk=rasDsk, dskHealth=dskHealth, standbyDskHealth=standbyDskHealth, crptdPRIfiles=crptdPRIfiles, numBadSectors=numBadSectors, rasDskStatus=rasDskStatus, wakeupInterval=wakeupInterval)
