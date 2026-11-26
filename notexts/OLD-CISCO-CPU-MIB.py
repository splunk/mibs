#
# PySNMP MIB module OLD-CISCO-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/OLD-CISCO-CPU-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lcpu = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 1))
busyPer = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyPer.setStatus('mandatory')
avgBusy1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgBusy1.setStatus('mandatory')
avgBusy5 = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgBusy5.setStatus('mandatory')
idleCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 59), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleCount.setStatus('mandatory')
idleWired = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 60), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleWired.setStatus('mandatory')
mibBuilder.exportSymbols("OLD-CISCO-CPU-MIB", lcpu=lcpu, avgBusy5=avgBusy5, avgBusy1=avgBusy1, idleWired=idleWired, idleCount=idleCount, busyPer=busyPer)
