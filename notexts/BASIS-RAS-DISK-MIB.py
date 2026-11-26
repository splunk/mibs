#
# PySNMP MIB module BASIS-RAS-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/BASIS-RAS-DISK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("BASIS-RAS-DISK-MIB", crptdPRIfiles=crptdPRIfiles, dskHealth=dskHealth, standbyDskHealth=standbyDskHealth, lastTime=lastTime, rasDskStatus=rasDskStatus, rasDsk=rasDsk, crptdFWfiles=crptdFWfiles, numBadSectors=numBadSectors, wakeupInterval=wakeupInterval)
